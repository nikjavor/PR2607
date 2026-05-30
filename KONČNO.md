# Napovedovanje zmagovalcev ATP teniških tekem

**Avtorji:** Nik Javor, Nika Labazan, Anže Barle Čuk, Irna Nuhić  
**Predmet:** Podatkovno rudarjenje  
**Študijsko leto:** 2025/2026

## 1. Uvod
Cilj projekta je bil izdelati model, ki na podlagi podatkov o tekmovalcih pred začetkom teniške tekme napove, kdo bo najverjetneje zmagal ATP dvoboj. 
Problem, kako analizirati podatke, smo obravnavali kot binarno klasifikacijo: za vsako tekmo napovedujemo, ali bo zmagal igralec `p1` ali igralec `p2`.

Projekt izdelave modela smo razdelili na tri glavne dele:

1. Priprava in analiza podatkov,
2. Izdelava značilk,
3. Treniranje in primerjava modelov.

Pri učenju modela smo posebej pazili, da se ne uporablja podatkov, ki so znani šele po začetku ali koncu tekme, saj bi to povzročilo uhajanje informacij.

## 2. Podatki
Podatke za učenje modela smo pridobili iz GitHub repozitorija [JeffSackmann/tennis_atp](https://github.com/JeffSackmann/tennis_atp). Uporabili smo datoteke s tekmami ATP turnirjev, ki so najvišja raven profesionalnega tenisa med leti 2000 in 2024. Podatki zadnjih dveh ATP sezon (2025, 2026) so bili predvideni kot dodaten preizkus modela na novejših podatkih.

Vsaka vrstica v datotekah predstavlja eno tekmo in vsebuje podatke o turnirju, igralni površini, datumu, zmagovalcu, poražencu, rankingu, starosti, višini in drugih značilkah igralcev.

V model nismo vključili podatkov o statistiki, ki nastanejo po začetku tekme, kot so:

```text
score, minutes, w_ace, l_ace, w_df, l_df, w_svpt, l_svpt, ...
```

Te vrednosti so znane šele med tekmo ali po njej, zato niso primerne za napoved pred tekmo.

## 3. Priprava podatkov
Najprej smo združili podatke iz več let v enoten dataset. Stolpec `tourney_date` smo pretvorili v datumski format in iz njega izračunali leto tekme.

Izločili smo tekme, ki niso bile običajno zaključene, na primer walkoverje, predaje in default tekme. Odstranili smo tudi vrstice brez ključnih podatkov, kot so identifikator igralca, ranking ali igralna površina.

Izvorni podatki so zapisani v obliki `winner` in `loser`. Za modeliranje smo jih pretvorili v obliko:

```text
p1, p2, target
```

Če je zmagal igralec `p1`, je `target = 1`, sicer je `target = 0`. Igralca `p1` smo določili naključno, da model ne bi mogel sklepati iz samega položaja igralca v tabeli.

Po čiščenju je v končnem datasetu ostalo **68.779 tekem** iz let 2000–2026 (samo nivoji Grand Slam, Masters, ATP in Finals). Po naključni dodelitvi p1/p2 je razred dejansko uravnotežen: `target = 0` v 50,21 % in `target = 1` v 49,79 % tekem, zato točnost 50 % ustreza naključnemu ugibanju.

Porazdelitev rok igralcev (`hand_matchup`) je močno asimetrična: `R_vs_R` 51.947 tekem, `L_vs_R` 7.822, `R_vs_L` 7.760 in `L_vs_L` le 1.137 tekem. Levičarji so torej zastopani v okoli 25 % vseh dvobojev.
