#1.
'''Clasa Cerc

Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()'''

print('________EX1____________')

class Cerc():

    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}')

    def aria(self):
        return 3.14 * (self.raza**2)
    def diametru(self):
        return self.raza*2
    def circumferinta(self):
        return 3.14 * (self.raza*2)

cerc1= Cerc(2,'alb')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

#2
'''Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''
print('________EX2____________')

class Dreptunghi():
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptulnghiul are culoarea {self.culoare} , lungimea {self.lungime} si latimea {self.latime}')

    def aria(self):
        return self.lungime*self.latime

    def perimetrul(self):
        return (self.lungime+self.latime)*2

    def schimba_culoarea(self,noua_culoare):
        self.culoare= noua_culoare

dreptunghi1= Dreptunghi(1,2,'negru')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())
dreptunghi1.schimba_culoarea('alb')
dreptunghi1.descrie()

#3
'''Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
'''
print('________EX3____________')

class Angajat():
    def __init__(self,nume,prenume,salariu):
        self.nume=nume
        self.prenume=prenume
        self.salariu=salariu

    def descrie(self):
        print(f'Angajatul {self.nume} {self.prenume} are salariul {self.salariu} de lei')

    def nume_complet(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul unui angajat este {self.salariu} de lei')

    def salariu_anual(self):
        return self.salariu*12

    def marire_salariu(self,marire):
        self.salariu=self.salariu+marire

angajat1=Angajat('Toma','Ioana',5000)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
print(angajat1.salariu_anual())
angajat1.marire_salariu(500)
angajat1.salariu_lunar()

#4
'''Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)'''

print('________EX4____________')

class Cont():
    def __init__(self,iban,titular_cont,sold):
        self.iban=iban
        self.titular_cont=titular_cont
        self.sold=sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self,suma):
        self.sold= self.sold-suma

    def creditare_cont(self,suma):
        self.sold=self.sold+suma

cont1=Cont('RO24TREZ00220010101XXXXX','Toma Ioana',8000)
cont1.afisare_sold()
cont1.debitare_cont(2000)
cont1.afisare_sold()
cont1.creditare_cont(15000)
cont1.afisare_sold()

#5
'''Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc

Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs  | cantitate    | pret bucata     | Total 
Telefon |      7       |       700       | 49000 
'''
print('________EX5____________')
class Factura():

    seria= 'ITF'

    def __init__(self,numar,nume_produs, cantitate, pret_buc):
        self.numar=numar
        self.nume_produs=nume_produs
        self.cantitate=cantitate
        self.pret_bucata=pret_buc

    def schimba_cantitatea(self,produse_primite):
        self.cantitate=self.cantitate+produse_primite

    def schimba_pretul(self,pret_nou):
        self.pret_bucata=pret_nou

    def schimba_nume_produs(self,nume):
        self.nume_produs=nume

    def total(self):
        return self.cantitate * self.pret_bucata

    def genereaza_factura(self):
        print(f'Factura seria {self.seria} numar {self.numar}')
        from datetime import date
        today=date.today()
        print(f'Data: {today}')

        table = [['Produs', 'Cantitate', 'pret bucata', 'total'], [self.nume_produs, self.cantitate, self.pret_bucata, Factura.total(self) ]]
        for row in table:
            print('| {:1} | {:^4} | {:>4} | {:<3} |'.format(*row)) #nu prea am inteles cum reuseste sa transforme in tabel aceasta formula

factura1= Factura(12,'Telefon',7,700)
factura1.genereaza_factura()
factura1.schimba_cantitatea(10)
factura1.schimba_pretul(500)
factura1.schimba_nume_produs('Televizor')
factura1.genereaza_factura()

#6
'''Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''

print('________EX6____________')

class Masina():
    culoare='gri'
    viteza_actuala=0
    culori_disponibile=['alb','negru','auriu','rosu','albastru','verde']
    marca='BMW'
    inmatriculata=False

    def __init__(self,model,viteza_maxima):
        self.model=model
        self.viteza_maxima=viteza_maxima

    def descriere(self):
        print(f'Masina marca {self.marca} are viteza actuala de {self.viteza_actuala} , culoarea {self.culoare} si este inmatriculata {self.inmatriculata}')

    def masina_inmatriculata(self):
        if self.inmatriculata is False:
            self.inmatriculata=True
        return self.inmatriculata

    def vopseste(self,culoare_noua):
        if culoare_noua in self.culori_disponibile:
            self.culoare=culoare_noua
        else:
            print('Eroare')

    def accelereaza(self,viteza):
        if viteza >0 and viteza > self.viteza_maxima:
            self.viteza_actuala=self.viteza_maxima
        elif viteza >0 and viteza < self.viteza_maxima:
            self.viteza_actuala = viteza
        elif viteza < 0:
            print('Eroare')

    def franeaza(self):
        self.viteza_actuala=0

masina1=Masina('Seria 5',300)
masina1.descriere()
print(masina1.masina_inmatriculata())
masina1.vopseste('lila')
masina1.descriere()
masina1.accelereaza(-2)
masina1.descriere()
masina1.franeaza()
masina1.descriere()

#7
'''Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''
print('________EX7____________')

class TodoList():
    todo={}

    def adauga_task(self,nume,descriere):
        self.todo[nume]=descriere

    def finalizeaza_task(self,nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print(self.todo.keys())

    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task in self.todo.keys():
            print(self.todo.get(nume_task))
        else:
            print('Do you want to add this task to your list ? ')
            raspuns=bool(input('')) #nu imi amintesc cum trebuia formatat astfel incat cand scriam in output true sau false sa le interpreteze corect
            if raspuns is False :
                print('La revedere!')
            else:
                detalii=input('Descrierea task-ului ')
                self.todo[nume_task] = detalii
                print(self.todo)

todolist1= TodoList()
todolist1.adauga_task('curatenie pardoseala','da cu aspiratorul')
todolist1.adauga_task('curatenie pardoseala si gresie','da cu mopul')
todolist1.finalizeaza_task('curatenie pardoseala')
todolist1.afiseaza_todo_list()
todolist1.afiseaza_detalii_suplimentare('curatenie pardoseala')
