'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

3. Actualizează proiectul pe github facand un push la noul cod
În Foldereul de teme ajunge să pui doar linkul cu proiectul tău public
Curs git/github
https://bit.ly/3yfFvqL - VIDEO 4’'''

from abc import abstractmethod

class FormaGeometrica:
    PI=3.14
    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):

    def __init__(self,latura):
        self.__latura=latura

    @property
    def latura(self):
        return self.__latura
    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura} ')
        return self.__latura
    @latura.setter
    def latura(self,latura_noua):
        print(f'Setter: Latura noua este {latura_noua} ')
        self.__latura=latura_noua

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura ')
        self.__latura = None

    def aria(self):
        return self.__latura**2

class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza=raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza} ')
        return self.__raza
    @raza.setter
    def raza(self,raza_noua):
        print(f'Setter: Raza noua este {raza_noua} ')
        self.__raza=raza_noua
    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza ')
        self.__raza=None

    def aria(self):
        return (self.__raza**2)*self.PI

    def descrie(self):
        print('Eu nu am colturi')

print('---------------patrat---------')
patrat=Patrat(2)
patrat.descrie()
print(patrat.aria())
patrat.latura
patrat.latura=3
patrat.latura
del patrat.latura
patrat.latura

print('-------------cerc--------')
cerc=Cerc(1)
cerc.descrie()
print(cerc.aria())
cerc.aria()
cerc.raza
cerc.raza=2
cerc.raza
del cerc.raza
cerc.raza












