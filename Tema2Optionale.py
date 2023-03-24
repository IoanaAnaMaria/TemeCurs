#11.Verifica daca x are minim 4 cifre (x e int) (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x=int(input('Alege un numar pentru valoarea x '))
if (x/1000>=1):
    print('X are 4 cifre')
else:
    print('X nu are 4 cifre')

#12.Verifica daca x are exact 6 cifre

if (x/10**5>=1):
    print('X are 6 cifre')
else:
    print('X nu are 6 cifre')

#13.Verifica daca x este numar par sau impar (x e int)

if (x%2==0):
    print('X este numar par')
else:
    print('X nu este numar par')

#14.x, y, z (int) Afiseaza care este cel mai mare dintre ele?

y=int(input('Alege un numar pentru valoarea y '))
z=int(input('Alege un numar pentru valoarea z '))
if (x>y and x>z):
    print('X este cel mai mare')
elif (y>x and y>z):
    print('Y este cel mai mare')
elif (z>x and z>y):
    print('Z este cel mai mare')

#15.X, y, z - reprezinta unghiurile unui triunghi.Verifica si afiseaza daca triunghiul este valid sau nu

latura_1=int(input('Alege latura1 a triunghiului '))
latura_2=int(input('Alege latura2 a triunghiului '))
latura_3=int(input('Alege latura3 a triunghiului '))
if(x+y+z==180 and (latura_1+latura_3>latura_2 or latura_1+latura_2>latura_3 or latura_2+latura_3>latura_1) ):
    print('Triunghiul este valid')
else:
    print('Nu se poate forma un triunghi')

#16.
'''Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte' '''

x=int(input('Alege un numar pentru valoarea x '))
propozitie = 'Coral is either the stupidest animal or the smartest rock'
litere=len(propozitie)-x
print(propozitie[0:litere])

#17.Acelasi string,declara un string nou care sa fie format din primele 5 caractere + ultimele 5

ultimele5=len(propozitie)-5
fraza= propozitie[0:5] + propozitie[ultimele5:-1] + propozitie[-1]
print(fraza)

#18.
'''acelasi string
salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest '  '''

index_start=propozitie.find('rock')
print(index_start)
print(propozitie[0:index_start])

#19.
'''citeste de la tastatura un string
verifica daca primul si ultimul caracter sunt la fel
se va folosi un assert
atentie: se doreste ca programul sa fie case insensitive
'apA' e acceptat '''

propoz_tastatura= str(input('Scrie o propozitie '))
assert propoz_tastatura[0].upper()==propoz_tastatura[-1].upper()

#20.
'''avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)'''

numere='0123456789'
print(numere[::2])
print(numere[1::2])
numere=numere.removeprefix('0')
print(numere[::2])


#Bonus la cerere:
#21.
'''Verificare imbarcare persoane
Tineti urmatoarele date
Varsta
Insotit de mama
Insotit de tata
Pasaport
Act permisiune mama
Act permisiune tata

Conditii de imbarcare
Daca pers are varsta peste 18 ani si are pasaport
Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

Aici vreau sa testati codul cu toate variantele posibile
Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results

Ex:
Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
Etc '''

varsta=int(input('Introducti varsta '))
insotit_de_mama= bool(input('Sunteti insotit de mama? '))
insotit_de_tata= bool(input('Sunteti insotit de tata? '))
pasaport= bool(input('Aveti pasaportul? '))
act_permisiune_mama= bool(input('Aveti act permisiune mama? '))
act_permisiune_tata= bool(input('Aveti act permisiune tata? '))

if (varsta>=18 and pasaport==True):
    print('Puteti incepe imbarcarea')
else:
    if(pasaport==True and insotit_de_mama==True and insotit_de_tata==True):
        print('Puteti incepe imbarcarea')
    else:
        if((pasaport==True and insotit_de_mama==False and insotit_de_tata==True and act_permisiune_mama==True) or (pasaport==True and insotit_de_mama==True and insotit_de_tata==False and act_permisiune_tata==True) ):
            print('Puteti incepe imbarcarea')
        else:
            print('Nu puteti incepe imbarcarea')


#22. Joc ghicit zarul
'''Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
Luati un nr ghicit de la utilizator
Verificati si afisati daca utilizatorul a ghicit
3 optiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
Ai ghicit. Felicitari? Ai ales x si zarul a fost y'''

import random
zar = [1, 2, 3, 4, 5, 6]
dice_roll = random.choice(zar)
# print(dice_roll)
optiune_ghicita= int(input('Cat pica zarul ? '))

if (optiune_ghicita==dice_roll):
    print('Ai castigat')
else:
    if(optiune_ghicita<dice_roll):
        print(f'Din pacate ai pierdut, ai ales un numar mai mic decat {dice_roll}')
    else:
        print(f'Din pacate ai pierdut, ai ales un numar mai mare decat {dice_roll}')