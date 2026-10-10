import csv
import random

# Ex. 1. Scrieţi un program în Python care să preia ca input un fişier .csv cu o listă oarecare şi să aibă ca output un număr
#predeterminat de elemente din acea listă, fără repetiţie. Aplicaţi pe lista studenţilor din grupa dumneavoastră care nu
#au prezentat încă o temă.
#lista de studenti care nu au prezentat tema

studenti=[]

with open(r"D:\PMP\PMP-2026-Ghica-Alexandra-Mihaela-3B4\studenti.csv", "r", encoding="utf-8") as fis:
    
    reader = csv.reader(fis)
    for rand in reader:
        studenti.append(rand[0]) #adaugam studentii din fisier in lista 

    print(studenti)

    nr_studenti = 5
    alesi=random.sample(studenti,nr_studenti)

    print("Studentii alesi sunt:")
    for student in alesi:
        print(student)
    

#Ex. 2. Doi prieteni joacă următorul joc, după următoarele reguli:
#Pasul 1. Primul jucător aruncă cu o monedă.
#● Dacă pică stemă, cel de-al doilea trebuie să arunce cu zarul şi să-i dea primului o sumă egală z − 3 $, unde z
#este rezultatul aruncării cu zarul (a da o sumă negativă este echivalent cu a lua opusul acelei sume). Jocul
#se încheie aici.
#● Dacă pică ban, atunci primul jucător trebuie să-i dea celui de-al doilea 0.5 $.
#Pasul n. În caz că jocul nu s-a încheiat, se reia pasul 1.
#Astfel, jocul se opreşte la pasul corespunzător obţinerii stemei de către primul jucător.

#a) este o distributie geemtrica deoarece se repeta experimentul pana la primul succes si numaram cate incercari au fost necesare

#b) simulare joc
import random


def experiment():
    N = 0
    S = 0

    while True:
        moneda = random.choice(["stema", "ban"])

        if moneda == "stema":
            N =N + 1
            rez_zar=random.randint(1,6)
            if(rez_zar-3 < 0): #daca suma este negativa, luam opusul
                S = S - (rez_zar - 3)
            else:
                S = S + rez_zar - 3
            break
        else:
            N = N + 1
            S = S - 0.5

    return N, S

N, S = experiment()
print("N =",N,"S =",S )

#c)simulare joc de mai multe ori + media S + histograma

import matplotlib.pyplot as plt

valori_S = []

for i in range(1000):
    N, S = experiment()
    valori_S.append(S)

media_S = sum(valori_S) / len(valori_S)
print("Media lui S =", media_S)

#histograma
plt.hist(valori_S)
plt.xlabel("S")
plt.ylabel("Frecventa")
plt.title("Distributia lui S")
plt.show()

#d)Ce se întâmplă dacă moneda este măsluită? Încercaţi să refaceţi pct. c) cu o probabilitate de apariţie a stemei
#p = 0.3, respectiv p = 0.7.


def experiment_masluit(p):
    N = 0
    S =  0

    while True:
        N = N + 1

        if random.random() < p: #se genereaza un numar aleator intre 0 si 1
            rez_zar = random.randint(1, 6)
            if(rez_zar-3 < 0): #daca suma este negativa, luam opusul
                S = S - (rez_zar - 3)
            else:
                S = S + rez_zar - 3
            break
        else:
            S = S - 0.5

    return N, S

#p=0.3
valori_S = []

for i in range(1000):
    N, S = experiment_masluit(0.3)
    valori_S.append(S)

media_S = sum(valori_S) / len(valori_S)
print("Media lui S pentru p = 0.3:", media_S)

plt.hist(valori_S) #construieste histograma
plt.xlabel("S")
plt.ylabel("Frecventa")
plt.title("Distributia lui S pentru p = 0.3")
plt.show()

#p=0.7

valori_S = []

for i in range(1000):
    N, S = experiment_masluit(0.7)
    valori_S.append(S)

media_S = sum(valori_S) / len(valori_S)
print("Media lui S pentru p = 0.7:", media_S)

plt.hist(valori_S)
plt.xlabel("S")
plt.ylabel("Frecventa")
plt.title("Distributia lui S pentru p = 0.7")
plt.show()

#Ex. 3. Într-o frizerie, trei frizeri îşi tund clienţii cu următoarele viteze medii: primul cu 3 clienţi pe oră, al doilea cu 6 pe
#oră iar al treilea cu 4 pe oră. Astfel, timpul de servire al unui client este modelat de distribuţii exponenţiale cu parametrii λ1 = 3 h−1 , λ2 = 6 h−1
#, respectiv λ3 = 4 h−1, iar probabilităţile de preluare a unui client de către un anumit frizer sunt
#3/13, 6/13, respectiv 4/13 (de ce?). Fie X timpul de servire pentru un client.
#Generaţi 10000 de valori pentru X, şi în felul acesta estimaţi media şi deviaţia standard a lui X. Realizaţi un grafic
#aproximativ al densităţii distribuţiei lui X.
#Notă: Distribuţia Exp(λ) se poate apela prin random.exponential(scale=1/λ) în Numpy, sau cu stats.expon(scale=1/λ)
#în Scipy. Având în vedere că X are o distribuţie continuă, densitatea aproximativă acesteia se poate vizualiza folosind
#funcţia plot_kde din librăria Arviz.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def experiment_frizerie():
    frizer = np.random.choice([1, 2, 3], p=[3/13, 6/13, 4/13])
    #X timpul necesar de servire a unui client 

    if frizer == 1:
        X = np.random.exponential(scale=1/3)
    elif frizer == 2:
         X = np.random.exponential(scale=1/6)
    else:
        X = np.random.exponential(scale=1/4)

    return X


valori_X = []

for i in range(10000):
    X = experiment_frizerie()
    valori_X.append(X)

media_X = np.mean(valori_X)
dev_X = np.std(valori_X)

print("Media lui X =", media_X)
print("Deviatia standard a lui X =", dev_X)

densitate = gaussian_kde(valori_X)

x = np.linspace(0, max(valori_X), 500)
y = densitate(x)

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Densitate")
plt.title("Densitatea aproximativa a lui X")
plt.show()