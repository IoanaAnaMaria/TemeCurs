#1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else

'''O functie de tipul if else ruleaza secvential ,
intai verifica daca se indeplineste comanda din if si o ruleaza,
iar daca aceasta nu se indeplineste ignora if si verifica daca se indeplineste conditia din else si o ruleaza.'''

#2.Verifica si afiseaza daca x este numar natural sau nu

x = int(input('Alege un numar '))
if (x>=0 and type(x)==int ):
    print('x este numar natural')
else:
    print('x nu este numar natural')

#3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

if ( x > 0 ):
    print('x este un numar pozitiv')
elif ( x ==0 ):
    print('x este un numar neutru')
else:
    print('x este un numar negativ')

#4. Verifica si afiseaza daca x este intre -2 si 13

if (x >= -2 and x <= 13):
    print('x este intre -2 si 13')
else:
    print('x NU este intre -2 si 13')

#5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

y=int(input('Alege un numar'))
if (x-y<5):
    print('Diferenta este mai mica de 5')
else:
    print('Diferenta este mai mare de 5')
#5a.
'''Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs'''


#6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

if not (5 <= x <= 27):
    print('x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')

#7.
'''x si y (int)
 Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare'''

y=int(input('Alege un numar'))
if (x==y):
    print('Sunt egale')
elif(x>y):
    print('X este mai mare decat y')
elif(y>x):
    print('Y este mai mare decat x')

#8.
'''X, y, z - laturile unui triunghi
 Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.'''

x=int(input('Alege latura 1 '))
y=int(input('Alege latura 2 '))
z=int(input('Alege latura 3 '))
if (x==y and x==z and y==z):
    print('Triunghi echilateral')
elif (x == y or x == z or y == z):
    print('Triunghi isoscel')
else:
    print('Triunghi oarecare')

#9.
'''Citeste o litera de la tastatura
Verifica si afiseaza daca este vocala sau nu'''

litera = input('Alege o litera ')
vocale = [ 'a', 'e', 'i', 'o', 'u', 'ă', 'â', 'î']
if(vocale.count(litera)>0):
    print('Litera este o vocala')
else:
    print('Litera este o consoana')

#10.
'''Transforma si printeaza notele din sistem romanesc in  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 5 => E
4 sau sub => F '''

nota = int(input('Alege o nota '))
if (nota >= 9 ):
    nota='A'
    print(nota)
elif (nota >= 8):
    nota = 'B'
    print(nota)
elif (nota >= 7):
    nota = 'C'
    print(nota)
elif (nota >= 6):
    nota = 'D'
    print(nota)
elif (nota >= 5):
    nota = 'E'
    print(nota)
elif (nota <= 4):
    nota = 'F'
    print(nota)



