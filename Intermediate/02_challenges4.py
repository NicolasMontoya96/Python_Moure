## 

"""
¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""



def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisble = False
 
            for index in range(2, number):
                if number % index == 0:
                    is_divisble = True
                    break

            if not is_divisble:
                print(number)
    
is_prime()