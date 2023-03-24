# Exercitiul 1

# O variabila reprezinta un container ce memoreaza mai multe tipuri de date

# Exercitiul 2

nume_pisica = 'Fluffy'
varsta_pisica = 3
greutate_pisica = 3.2
castrata = True

# Exercitiul 3

print(type(nume_pisica))
print(type(varsta_pisica))
print(type(greutate_pisica))
print(type(castrata))

# Exercitiul 4

greutate_pisica = round(greutate_pisica)
print(greutate_pisica)
print(type(greutate_pisica))
# variabila greutate_pisica de tip float a fost transformata intr-o variabila de tip int

# Exercitiul 5

print( ' Eu am o pisica pe nume ' + nume_pisica + ' care este castrata ' + str(castrata) )
print( ' Pisica mea pe nume ' + nume_pisica + ', are o greutate de ' + str(greutate_pisica) + ' kg')
varsta_pisica = str (varsta_pisica)
castrata = str(castrata)
print( ' Pisica mea cu varsta de ' + varsta_pisica + ' ani ' + ' este castrata ' + castrata )
print( f' Am o pisica numita {nume_pisica} , care are {greutate_pisica} kg si o varsta de {varsta_pisica} ani , iar aceasta este castrata {castrata}')

# Exercitiul 6

nume = input('Introduceti numele ')
prenume = input('Introduceti prenumele ')
print(len(nume))
print(len(prenume))
caractere_nume_complet = len(nume) + len(prenume)
print(f'Numele complet are {caractere_nume_complet} caractere ')

# Exercitiul 7

lungimea = int(input( ' Introduceti lungimea '))
latimea = int(input('Introduceti latimea '))
print(f' Aria dreptunghiului este {lungimea*latimea}')

# Exercitiul 8

propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count(' the '))

# Exercitiul 9

propozitie = 'Coral is either the stupidest animal or the smartest rock'
print('Coral is either ' + propozitie[16:19].upper() + ' stupidest animal or ' + propozitie[40:44].upper() + 'smartest rock ' )
print(propozitie.replace(' the ',' THE '))

#Exercitiul 10

propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert isinstance(propozitie , int )

#Exercitiul 11

string_dimensiune_impara = input('Alege stringul ')
x = int(len(string_dimensiune_impara) / 2 + 1)
print(string_dimensiune_impara[x-1])

# #Exercitiul 12

palindrom = 'ana are mere '
assert palindrom == palindrom[::-1]



