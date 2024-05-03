my_string_variable = "My String variable"

print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)


#Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Nicolas", "Montoya", "NicolasRX", 28
print("Mellamo:", name, surname, "Mi edad es:", age, ". Y mi alias es:", alias)


# Inputs
""""
name = input('Cuál es tu nombre?: ')
age = input('Cuál es tu edad? ')

print(name)
print(age)

"""

# Cambiamos su tipo         
name = 35
age = "Brais"
print(name)
print(age)

# Forzamos en tipo
address:  str = "Mi dirección"

address = 32

print(address)
