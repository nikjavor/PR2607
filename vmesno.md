# Vmesno poročilo
## 0.Uvod 
Mi smo se odločili, da bomo naredili model, ki bo napodoval zmagovalce prihodnjih tekem ATP turnirjev. V vmesnem poročilu smo raziskali katre napodedovalne metode so najuspešnejše za naš problem. Najprej smo analizirali kako primerna sta Random forest in Logistic Regression ter to tudi prikazali z ROC krivuljo in confusion matrix.
### 1. Confusion matrix
#### 1.1 Random forest
<img width="290" height="165" alt="image" src="https://github.com/user-attachments/assets/19da17a1-1fe2-48d1-a5e3-5c696da8d4cc" />

Random forest je metoda  kjer med učenjem se kreira več oddločtivenih dreves med učenjem. Napove true negative vrednost 67,40% časa in true positive vrednost 67,5% vseh primerov.

#### 1.2 Logistic Regression
<img width="293" height="156" alt="image" src="https://github.com/user-attachments/assets/fe72241d-7a89-4c28-93d6-e353b447797b" />

Logistic Regression je metoda  kjer proba napovedati v katero izmed devh kategorij spada. Napove true negative vrednost 70,48% časa in true positive vrednost 70,49% vseh primerov.

#### 1.3 Neural network
<img width="288" height="155" alt="image" src="https://github.com/user-attachments/assets/0f85730a-7fa0-4845-85b8-0a4d3e2437d0" />

Neural network je metoda, ki ima input in output vmes pa je več skritih plasti z različnimi utežim ki probajo napovedati output. Napove true negative vrednost 70,80% časa in true positive vrednost 71,04% vseh primerov.

#### 1.4 Evaluation results
<img width="352" height="96" alt="image" src="https://github.com/user-attachments/assets/13310e69-2c9b-480b-961c-5331ab25e775" />

Kot smo že videl v Confusion matrix obeh modelov, nam zdaj še AUC in klasifikacijska točnost povesta, da je Neural network najboljši pri klasifikaciji in potem sledita Logistic Regression in Random forest.

### 2. ROC
<img width="1634" height="986" alt="image" src="https://github.com/user-attachments/assets/723c54f4-5f4b-4509-8d57-0f5203951c21" />

Ugotovitve iz prejšne točke še podane vizualno kjer oranžna je Logistic Regression, zelena Random forest in vijolična Neural network.

### 3. Lift curve
<img width="541" height="461" alt="image" src="https://github.com/user-attachments/assets/516443c3-d552-4a3b-8748-287355597af6" />

Prikazuje koliko uspešni so modeli v primerjavi z naključnim ugibanjem.
