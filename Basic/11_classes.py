### Classes ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.fullname = f'{name} {surname} {alias}'

    def walf(self):
        print(f'{self.fullname} está caminando')

my_person = Person('Nicolas', 'Montoya')
print(my_person.fullname)
my_person.walf()

my_other_person = Person('Nicolas', 'Montoya','NicolasRX')

print(my_other_person.fullname)
my_person.walf()
my_other_person.fullname = 'Héctor de león El loco de los perros'
print(my_other_person.fullname)


my_other_person.fullname = 666
print(my_other_person.fullname)