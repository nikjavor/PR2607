# Napovedovanje zmagovalcev ATP teniških tekem

**Avtorji:** Nik Javor, Nika Labazan, Anže Barle Čuk, Irna Nuhić  
**Predmet:** Podatkovno rudarjenje  
**Študijsko leto:** 2025/2026  

---

## 1. Uvod

Cilj projekta je bil izdelati model, ki na podlagi podatkov, znanih pred začetkom teniške tekme, napove zmagovalca ATP dvoboja. Problem smo obravnavali kot binarno klasifikacijo, kjer za vsako tekmo napovedujemo, ali bo zmagal igralec `p1` ali igralec `p2`.

Pri modeliranju smo posebej pazili, da nismo uporabili podatkov, ki so znani šele med tekmo ali po njej, saj bi to povzročilo uhajanje informacij. Zato iz podatkov nismo vključili statistik, kot so rezultat, trajanje tekme, asi, dvojne napake, število servisnih točk in podobno.

---

## 2. Podatki in priprava

Podatke smo pridobili iz repozitorija `JeffSackmann/tennis_atp`. Uporabili smo ATP tekme iz obdobja 2000–2026, pri čemer so podatki za leti 2025 in 2026 služili kot dodatni preizkus modela na novejših tekmah.

Vsaka vrstica predstavlja eno tekmo in vsebuje podatke o turnirju, igralni površini, datumu, igralcih, rankingu, starosti, višini in drugih predtekmovalnih značilkah.

Izločili smo tekme, ki niso bile običajno zaključene, na primer walkoverje, predaje in default tekme. Odstranili smo tudi vrstice brez ključnih podatkov, kot so identifikator igralca, ranking ali igralna površina.

Ker so izvorni podatki zapisani v obliki `winner` in `loser`, smo jih za modeliranje pretvorili v obliko `p1`, `p2`, `target`. Igralca `p1` smo določili naključno, da model ne bi mogel sklepati iz samega položaja igralca v tabeli. Če je zmagal `p1`, je ciljna spremenljivka `target = 1`, sicer `target = 0`.

Po čiščenju je v končnem datasetu ostalo **68.779 tekem**. Razreda sta bila skoraj popolnoma uravnotežena: `target = 0` v 50,21 % in `target = 1` v 49,79 % tekem, zato točnost 50 % predstavlja približno naključno ugibanje.

---

## 3. Analiza podatkov

Osnovna analiza je pokazala, da je ranking igralcev močan napovedni signal. Bolje rangirani igralec je v celotnem datasetu zmagal v **63,50 %** tekem. Ta rezultat predstavlja tudi pomemben baseline model, s katerim smo primerjali naprednejše pristope.

Delež zmag favorita se med igralnimi površinami ni zelo razlikoval:

| Površina | Delež zmag favorita |
|---|---:|
| Hard | 65,90 % |
| Grass | 65,56 % |
| Clay | 64,46 % |
| Carpet | 62,34 % |

Ranking je torej uporaben signal na vseh površinah, vendar sam po sebi ni dovolj za natančnejše napovedovanje. Analiza razlike v rankingu je pokazala pričakovan vzorec: večja kot je razlika med igralcema, večja je verjetnost zmage favorita. Pri zelo majhnih razlikah v rankingu pa je izid bližje naključnemu.

![Delež zmag bolje rangiranega igralca](Slike/bolje_rangirani.png)

---

## 4. Izdelava značilk

Osnovne značilke smo izračunali kot razlike med igralcema `p1` in `p2`. Mednje sodijo:

- `rank_diff`
- `rank_points_diff`
- `age_diff`
- `height_diff`
- `p1_better_ranked`
- `abs_rank_diff`

Dodali smo tudi značilke turnirja:

- `surface`
- `tourney_level`
- `best_of`
- `round`
- `hand_matchup`

Najpomembnejši del projekta pa je bila izdelava zgodovinskih značilk. Te smo računali kronološko, kar pomeni, da smo za vsako tekmo uporabili samo informacije iz tekem, ki so se zgodile pred njo. S tem smo preprečili uhajanje informacij iz prihodnosti.

Med zgodovinske značilke smo vključili:

- `elo_diff`
- `surface_elo_diff`
- `last10_winrate_diff`
- `surface_winrate_diff`
- `matches_played_diff`
- `surface_matches_played_diff`
- `h2h_matches`
- `h2h_winrate_diff`
- `surface_h2h_matches`
- `surface_h2h_winrate_diff`
- `last_h2h_result`

Elo in surface Elo sta se izkazala kot najmočnejša signala. Korelacija značilke `elo_diff` s ciljno spremenljivko je znašala **0,391**, korelacija `surface_elo_diff` pa **0,375**. Ko je imel `p1` višji Elo od `p2`, je zmagal v **65,85 %** primerov, ko je imel nižji Elo, pa le v **33,75 %** primerov.

Značilke head-to-head so bile manj uporabne, saj ima le **45,9 %** tekem vsaj en predhodni medsebojni dvoboj, samo **30,7 %** tekem pa predhodni dvoboj na isti površini.

---

## 5. Modeliranje

Podatke smo razdelili časovno, saj smo želeli simulirati realno napovedovanje prihodnjih tekem.

| Del | Leta | Število tekem |
|---|---:|---:|
| Train | 2000–2021 | 57.281 |
| Validation | 2022 | 2.620 |
| Test | 2023–2024 | 5.389 |
| Future test | 2025–2026 | 3.489 |

Primerjali smo več modelov:

1. baseline model, ki vedno napove zmago bolje rangiranega igralca,
2. logistično regresijo z osnovnimi značilkami,
3. logistično regresijo z zgodovinskimi značilkami,
4. naključni gozd z zgodovinskimi značilkami,
5. XGBoost z zgodovinskimi značilkami.

Modele smo vrednotili z metrikami **accuracy**, **AUC** in **log loss**.

---

## 6. Rezultati

Na testnem obdobju 2023–2024 so bili rezultati naslednji:

| Model | Accuracy | AUC | Log loss |
|---|---:|---:|---:|
| XGBoost - historical | 0,6495 | **0,7209** | **0,6122** |
| Random Forest - historical | **0,6498** | 0,7178 | 0,6141 |
| Logistic Regression - historical | **0,6498** | 0,7173 | 0,6162 |
| Logistic Regression - basic | 0,6343 | 0,6962 | 0,6359 |
| Baseline: better ranked player | 0,6350 | 0,6350 | / |

Logistična regresija z osnovnimi značilkami je dosegla AUC **0,6962**, z dodatkom zgodovinskih značilk pa **0,7173**. To potrjuje, da zgodovinske značilke, predvsem Elo, surface Elo in forma, izboljšajo napovedno moč modela.

Najboljši rezultat po AUC in log loss je dosegel **XGBoost z zgodovinskimi značilkami**. Ker sta AUC in log loss pomembni metriki za verjetnostne napovedi, smo ga izbrali kot končni model.

![Primerjava modelov](Slike/primerjava.png)

![ROC krivulje](Slike/ROC_krivulje.png)

---

## 7. Interpretacija

Analiza pomembnosti značilk je pokazala, da so najpomembnejše zgodovinske in ranking značilke. Pri naključnem gozdu so bile najpomembnejše:

| Značilka | Pomembnost |
|---|---:|
| `elo_diff` | 0,176 |
| `surface_elo_diff` | 0,165 |
| `rank_points_diff` | 0,144 |
| `rank_diff` | 0,126 |
| `surface_winrate_diff` | 0,092 |
| `last10_winrate_diff` | 0,055 |

Koeficienti logistične regresije potrjujejo podobno sliko. Pozitiven koeficient pri `elo_diff` in `surface_elo_diff` pomeni, da višji Elo igralca `p1` poveča verjetnost njegove zmage. Negativen koeficient pri `rank_diff` je pričakovan, saj večja številka rankinga pomeni slabšega igralca.

Značilke, povezane s turnirjem, kot so površina, nivo turnirja in krog, so imele manjši vpliv kot zgodovinske značilke igralcev. To kaže, da je za napovedovanje izida pomembnejša ocena trenutne moči igralcev kot sama informacija o turnirju.

![Pomembnost značilk](Slike/znacilke_rforest.png)

---

## 8. Omejitve

Model ne vključuje vseh dejavnikov, ki vplivajo na izid teniške tekme. Med pomembnimi manjkajočimi informacijami so poškodbe, utrujenost, dnevna forma, vremenske razmere, motivacija in psihološki pritisk. Prav zato model težko napove velika presenečenja, kjer favorit izgubi kljub močni zgodovinski statistiki.

Dodatna omejitev je, da imajo mladi igralci ali igralci z malo preteklimi tekmami manj zanesljive zgodovinske značilke. Podobno so head-to-head značilke uporabne samo pri igralcih, ki so se v preteklosti že večkrat srečali.

---

## 9. Zaključek

V projektu smo izdelali model za napovedovanje zmagovalcev ATP teniških tekem. Najpomembnejša ugotovitev je, da zgodovinske značilke bistveno izboljšajo napovedno moč modela v primerjavi z uporabo samo osnovnih podatkov, kot je ranking.

Najboljši model je bil **XGBoost z zgodovinskimi značilkami**, ki je dosegel najvišji AUC in najnižji log loss. Kljub temu so bile razlike med modeli z zgodovinskimi značilkami majhne, kar kaže, da je kakovost značilk pomembnejša od izbire kompleksnega modela.

Elo rating, Elo rating po površini in forma igralcev so se izkazali kot ključni signali za napovedovanje izidov. Model tako dobro zajame dolgoročno moč igralcev, ne more pa zanesljivo napovedati nenadnih presenečenj, poškodb ali slabega dneva posameznega igralca.