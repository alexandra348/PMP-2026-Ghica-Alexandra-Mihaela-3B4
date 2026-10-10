import pymc as pm
import numpy as np
import matplotlib.pyplot as plt
import arviz as az
import random

#punctul a)simulare in python
def experiment():

    urna=['R','R','R','A','A','A','A','N','N']

    zar=random.randomint(1,6)

    if zar in [2,3,5]:
        urna.append('N')
    if zar in [1,4]:
        urna.append('A')
    elif zar in [6]:
        urna.append('R')

    bila_extrasa=random.choise(urna)

    return bila_extrasa

#punctul b)prob sa obtinem bila rosie la extragere

N=1000000
bile_rosii=0

for i in range(N):

    bila=experiment  #simulam experimentul de mai multe ori 

    if bila=='R':
       bile_rosii=bile_rosii+1

probabilitate_estimata=bile_rosii/N
print("Probabilitatea estimata este:", probabilitate_estimata)

#punctul c)probabilitate teoretica VS probabilitate estimata

probabilitate_teoretica=(1/6)*(4/10)+(5/6)*(3/10)
print("Probabilitatea teoretica este:", probabilitate_teoretica)

print("Diferenta dintre probabilitati este",abs(probabilitate_estimata-probabilitate_teoretica))




       


