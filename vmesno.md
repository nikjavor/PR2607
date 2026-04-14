# Vmesno poročilo
## 0.Uvod 
Cilj našega projekta je razvoj modela strojnega učenja za napovedovanje zmagovalcev teniških dvobojev na turnirjih serije ATP. V tej fazi smo raziskali in primerjali učinkovitost štirih različnih metod klasifikacije: naključni gozd (Random Forest), logistična regresija (Logistic Regression), nevronske mreže (Neural Networks) in gradientno povečevanje (XGBoost). Modele smo ovrednotili s pomočjo matrike zmede (confusion matrix), ROC krivulje, AUC vrednosti in lift krivulje.
### 1. Confusion matrix
Matrika zmede nam omogoča vpogled v natančnost napovedi za oba razreda (zmaga/poraz).
#### 1.1 Random forest
<img width="290" height="165" alt="image" src="https://github.com/user-attachments/assets/19da17a1-1fe2-48d1-a5e3-5c696da8d4cc" />

Metoda naključnega gozda temelji na združevanju napovedi velikega števila odločitvenih dreves, kar zmanjšuje tveganje za prilagajanje učnim podatkom (overfitting).. Napove true negative vrednost 67,40% časa in true positive vrednost 67,5% vseh primerov.

#### 1.2 Logistic Regression
<img width="293" height="156" alt="image" src="https://github.com/user-attachments/assets/fe72241d-7a89-4c28-93d6-e353b447797b" />

Logistična regresija je statistični model, ki se uporablja za napovedovanje verjetnosti pripadnosti določenemu razredu. Napove true negative vrednost 70,48% časa in true positive vrednost 70,49% vseh primerov.

#### 1.3 Neural network
<img width="288" height="155" alt="image" src="https://github.com/user-attachments/assets/0f85730a-7fa0-4845-85b8-0a4d3e2437d0" />

Nevronske mreže posnemajo delovanje možganov z uporabo več skritih plasti in uteži, ki se prilagajajo med procesom učenja. Napove true negative vrednost 70,80% časa in true positive vrednost 71,04% vseh primerov.

#### 1.4 Gradient boosting(xgboost)
<img width="293" height="160" alt="image" src="https://github.com/user-attachments/assets/7ffd64b8-ead7-4013-9515-d0201164e9de" />

XGBoost je napreden algoritem, ki zaporedno gradi odločitvena drevesa, kjer vsako naslednje drevo popravlja napake predhodnih. Napove true negative vrednost 70,61% časa in true positive vrednost 71,62% vseh primerov.

#### 1.5 Evaluation results
<img width="350" height="119" alt="image" src="https://github.com/user-attachments/assets/bd6b46bf-823f-4940-a048-a35f0ef2af0c" />

Kot smo že videl v Confusion matrix obeh modelov, nam zdaj še AUC in klasifikacijska točnost povesta, da je Neural network najboljši pri klasifikaciji in potem sledita Gradient boosting(xgboost) za njim pa sta Logistic Regression in Random forest.

### 2. ROC
<img width="1920" height="1017" alt="image" src="https://github.com/user-attachments/assets/8eb4efef-2ff7-40c3-8026-64d5782f322e" />

ROC krivulja prikazuje razmerje med deležem pravilnih pozitivnih napovedi in deležem napačnih pozitivnih napovedi pri različnih mejnih vrednostih.
Ugotovitve iz prejšne točke še podane vizualno kjer oranžna je Logistic Regression, zelena Random forest in vijolična Neural network.

### 3. Lift curve
<img width="1919" height="1011" alt="image" src="https://github.com/user-attachments/assets/cc1d03e5-d774-4bd5-b239-5af433775869" />

Lift krivulja prikazuje, kolikokrat je naš model uspešnejši od naključnega ugibanja (baseline).

### 4. Explain model

Je model. ki prikazuje kako podatki vplivajo na odločanje. Modra barva prikazuja vrednosti, ki zmanjšujejo verjetnost p1 za zmago, redeča barva pa prikazuje ravno obratno.

#### 4.1 Neural network
<img width="1920" height="1011" alt="image" src="https://github.com/user-attachments/assets/8db7fe1a-313e-40ad-99e1-f0c6a0e7fb7e" />

#### 4.2 Gradient boosting(xgboost)
<img width="1920" height="1016" alt="image" src="https://github.com/user-attachments/assets/68b855b2-246a-45ce-a3b4-7d2befd30762" />

