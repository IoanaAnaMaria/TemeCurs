#1.
'''Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.'''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in range(len(mașini)):
    print(f'Masina mea preferata este {mașini[x]}')

for x in mașini:
    print(f'Masina visurilor mele este {x}')

a=0
while a < len(mașini):
    a+=1
    print(mașini[a-1])

#2.
'''Aceeași listă:
Folosește un for else
În for- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.'''
print('ex2')

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in range (len(mașini)):
    if x != 0 and x !=len(mașini)-1:
        mașini[x]=mașini[x].upper()
    print(mașini[x])
else:
    print(mașini)

#3.
'''Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘ '''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in range(len(mașini)):
    if mașini[x] == 'Mercedes' :
        print('AM GASIT MASINA DORITA DE DVS')
        break
    else:
        print(f'Am găsit mașina {mașini[x]} ,mai cautam')

#4.
'''Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.'''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for x in mașini:
    if x=='Trabant' or x=='Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {x}')

#5.
'''Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).● Printează Modele vechi: x.
● Modele noi: x.'''

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masini_vechi=[]
for x in range (len(mașini)):
    if mașini[x]=='Trabant' or mașini[x]=='Lăstun':
        masini_vechi.append(mașini[x])
        mașini[x] = 'Tesla'
print(f'Modele vechi : {masini_vechi}')
print(f'Modele noi : {mașini}')

#6.
'''Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.'''

pret_masini = {'Dacia': 6800,'Lăstun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000 }
for x in pret_masini:
    pret=pret_masini.get(x)
    if pret < 15000:
        print(x)
        print(f'{x} cu pretul de {pret_masini.get(x)}' )
        print(f'Pentru un buget de sub 15000 euro puteți alege mașina {x}')


#7.
'''Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numarul3=[]
for x in numere:
    if x == 3:
        numarul3.append(x)
print(len(numarul3))

#8.
'''Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).'''
print('             ex 8                ')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for numar in numere:
    suma += numar
print (f'\n Suma tuturor cifrelor este {suma}')


#9.
'''Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).'''
print('             ex 9                ')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max=0
for numar in numere:
    if numar>nr_max:
        nr_max=numar
print(f' Numarul maxim este {nr_max}')

#10.
'''Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.'''
print('             ex 10                ')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for x in range(len(numere)):
    if numere[x] > 0 :
        numere[x]=-numere[x]
print(numere)
