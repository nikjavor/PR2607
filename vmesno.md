# Vmesno poročilo
## 0.Uvod 
Mi smo se odločili, da bomo naredili model, ki bo napodoval zmagovalce prihodnjih tekem ATP turnirjev. V vmesnem poročilu smo raziskali katre napodedovalne metode so najuspešnejše za naš problem. Najprej smo analizirali kako primerna sta Random forest in Logistic Regression ter to tudi prikazali z ROC krivuljo in confusion matrix.
### 1. Confusion matrix
#### 1.1 Random forest
<img width="290" height="165" alt="image" src="https://github.com/user-attachments/assets/19da17a1-1fe2-48d1-a5e3-5c696da8d4cc" />

Random forest  napove true negative vrednost 67,40% časa in true positive vrednost 67,5% vseh primerov.

#### 1.2 Logistic Regression
<img width="293" height="156" alt="image" src="https://github.com/user-attachments/assets/fe72241d-7a89-4c28-93d6-e353b447797b" />

Logistic Regression  napove true negative vrednost 70,48% časa in true positive vrednost 70,49% vseh primerov.

#### 1.3 Evaluation results
<img width="346" height="73" alt="image" src="https://github.com/user-attachments/assets/7d1af18c-9a91-4369-8b05-6f30bfc824dd" />

Kot smo že videl v Confusion matrix obeh modelov, nam zdaj še AUC in klasifikacijska točnost povesta, da je Logistic Regression boljši od Random forest pri klasifikaciji.

### 2. ROC
<img width="421" height="446" alt="image" src="https://github.com/user-attachments/assets/3f095a51-8820-4509-b045-7ddcf05b10f9" />

Ugotovitve iz prejšne točke še podane vizualno kjer oranžna je Logistic Regression in zelena Random forest.
