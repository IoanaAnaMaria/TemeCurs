#1. Functie care sa calculeze si sa returneze suma a 2 numere

def suma_2numere(x,y):
    suma= x+y
    return suma
print(suma_2numere(2,3))
print(suma_2numere(2,8))

#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def nr_parimpar(y):
    if y%2==0:
        return True
    else:
        return False

print(nr_parimpar(2))
print(nr_parimpar(5))

#3. Functie care returneaza numarul total de caractere din numele tau complet.(nume, prenume, nume_mijlociu)

def nr_caractere_nume(nume,prenume,nume_mijlociu):
    nr_caractere= len(nume)+len(prenume)+len(nume_mijlociu)
    return nr_caractere

print(nr_caractere_nume('Toma','Ioana','Ana-Maria'))
print(nr_caractere_nume('Toma','Ana','Maria'))

#4. Functie care returneaza aria dreptunghiului
def arie_dreptunghi(lungime,latime):
    arie=lungime*latime
    return arie

print(arie_dreptunghi(10,5))
print(arie_dreptunghi(2,4))

#5. Functie care returneaza aria cercului
def arie_cerc(raza):
    aria= 3.14159 * (raza**2)
    return aria

print(arie_cerc(5))
print(arie_cerc(7))

#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def gasit(string):
    contorizare_litera= string.count('x')
    if contorizare_litera != 0:
        return True
    else:
        return False

print(gasit('Ana are mere'))
print(gasit('Ana are x mere'))

#7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y
print('________________ex7__________')
def nr_caractere_mici_si_mari(string1):
    upper = 0
    lower = 0
    for i in string1:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f'Nr de caractere lower case este {lower}')
    print(f'Nr de caractere upper case este {upper}')

print(nr_caractere_mici_si_mari('Ana Are Mere'))

#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

def lista(*args):
    list = []
    for i in args:
        if i>0 :
            list.append(i)
    return list

print(lista(-5,1,2,3,4,-2))

#9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
'''Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale.'''

def comparatie_numere(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif x<y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale.')

comparatie_numere(2,3)
comparatie_numere(3,2)
comparatie_numere(3,3)

#10. Functie care primeste un numar si un set de numere.
'''Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''

def numere(num, set):
    if num in set:
        print('Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        set.add(num)
        print('Am adaugat numarul nou in set')
        return True

print(numere(1,{1,2,3}))
print(numere(12,{1,2,3}))

#11. Functie care primeste o luna din an si returneaza cate zile are acea luna
from calendar import monthrange
def zile_luna(an, luna):
    return monthrange(an, luna)[1]
#am folosit [1] deoarece functia returneaza 2 valori , prima fiind indexul zilei din saptamana in care a inceput luna respectiva, si a2a numraul de zile ale lunii
print(zile_luna(2022, 9))
print(zile_luna(2023, 1))
print(zile_luna(2023, 3))

#12. Functie calculator care sa returneze 4 valori Suma, diferenta, inmultirea, impartirea a 2 numere.
'''In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)'''

def calculator(x,y):
    suma=a=x+y
    diferenta=b=x-y
    inmultirea=c=x*y
    impartirea=d=x/y
    return suma,diferenta,inmultirea,impartirea

a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

#13. Functie care primeste o lista de cifre (adica doar 0-9)
'''Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {0: 0,1 :2,2: 0,3: 1,4: 0,5: 3,6: 0,7: 2,8: 0,9: 1}'''

def num_recurenta(lst):
   count = {}
   for i in lst:
    count[i] = count.get(i, 0) + 1
   return count

print(num_recurenta([1, 3, 1, 5, 9, 7, 7, 5, 5])) #m-am inspirat de pe internet insa nu am inteles-o foarte bine

print(num_recurenta([1, 2, 1, 2, 1, 3, 4, 5, 6]))

#14. Functie care primeste 3 numere.Returneaza valoarea maxima dintre ele

def val_max(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    elif z>x and z>y:
        return z

print(val_max(5,8,3))
print(val_max(10,8,3))
print(val_max(10,8,12))

#15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
'''Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)'''

def suma_nr_dinainte(x):
    lista_nr_dinainte=[]
    suma=0
    for i in range(0,x+1):
        lista_nr_dinainte.append(i)
    for y in lista_nr_dinainte:
        suma+=y
    return suma
print(suma_nr_dinainte(5))
print(suma_nr_dinainte(3))

#16. Funcție care primește 2 liste de numere (numerele pot fi dublate).Returnati numerele comune

def numere_comune(list1,list2):
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

print(numere_comune([1,2,3,4],[2,3,4]))
print(numere_comune([6,5,3,4],[1,2,3,4]))

#17. Functie care sa aplice o reducere de pret
'''Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalid'''

def reducere_pret(pret,reducere):
    pret_final=0
    if pret>0 and reducere<100:
        pret_final=pret-(reducere/100*pret)
        return pret_final
    else:
        print('Reducere invalida')

print(reducere_pret(100,10))
print(reducere_pret(130,120))

#18. Functie care sa afiseze data si ora curenta din ro.(bonus: afisati si data si ora curenta din China)

from datetime import datetime, timedelta, timezone
def data_ora_curenta():
    now = datetime.now()
    print(f"Data si ora curenta in Romania: {now}")
    print(f"Data si ora curenta in China: {now + timedelta(hours=5)}")

data_ora_curenta()

#19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

from datetime import date
def zile_ramase_pana_la_ziua_mea(ziua_mea):
    azi=date.today()
    return (ziua_mea-azi).days
ziua_mea = date(2024, 1, 14)
print(date.today())
print(zile_ramase_pana_la_ziua_mea(ziua_mea), 'zile') #ce e gresit aici de nu returneaz numarul corect ?

from datetime import date
def num_zile(data1, data2):
    return (data2-data1).days
data1 = date(2023, 10, 3)
data2 = date(2024, 1, 14)
print(num_zile(data1, data2), 'zile')


















