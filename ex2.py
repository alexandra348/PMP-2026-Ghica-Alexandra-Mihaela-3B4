#Să presupunem că investigăm o boală (B), care afectează doar un procent din populaţie (P(B) = 0.01). Avem un test de
#diagnosticare pentru această boală, care are următoarele caracteristici:
#● Sensibilitate (probabilitatea ca testul să fie pozitiv dacă persoana este bolnavă): P(Test = Pozitiv∣B) = 0.95
#● Specificitate (probabilitatea ca testul să fie negativ dacă persoana nu este bolnavă): P(Test = Negativ∣¬B) = 0.90
#a) Dacă o persoană este testată şi rezultatul este pozitiv, care este probabilitatea ca aceasta să fie efectiv bolnavă?
#Cum explicaţí rezultatul?
#b) Modelaţi în Python probabilitatea de mai sus şi comparaţi cu cea obţinută teoretic la punctul anterior.
#c) Care ar trebui să fie specificitatea minimă pentru ca probabilitatea de mai sus să ajungă la 50%?
#Încărcaţi argumentul fie în Markdown/Latex, fie ca foto la foia de lucru.

import numpy as np

N=10000

#persoane bolnave, cu probabilitatea 0.01
bolnav=np.random.random(N)<0.01

#rezultat test
test_pozitiv=np.zeros(N,dtype=bool)

#teste pozitive pentru cei bolnavi
test_pozitiv[bolnav]=np.random.random(np.sum(bolnav))<0.95

#teste pozitive pentru cei sanatosi
test_pozitiv[~bolnav]=np.random.random(np.sum(~bolnav))<0.10

#cei cu testul pozitiv, cati au de fapt boala
probabilitate=np.sum(bolnav & test_pozitiv)/np.sum(test_pozitiv)

print(probabilitate)