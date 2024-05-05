## Loops ##

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 

else: # Es opcional
    print('Mi condición es mayor o igual que 10')
     
print('La ejecución continúa')

while my_condition <20:
    
    my_condition += 1 
    if my_condition == 15:
        print('Se detiene la ejecución')
        break

    print(my_condition)



print('La ejecución continúa')

# For

my_list = [28,30,53,44,30,17]
for element in my_list:
    print(element)

my_tuple = (35, 1.80, "Nicolas", "Montoya", "Nicolas")
for element in my_tuple:
    print(element)


my_set = {"Nicolas", "Montoya", 27}
for element in my_set:
    print(element)


my_dict = {"Nombre":"Nicolas", "Apellido":"Montoya", "Edad":27}
for element in my_dict:
    print(element)
    if element == 'Edad':
        continue
    print('Se ejecuta')
else:
    print('El bucle For para mi diccionario a finalizado')

print('La ejecución continúa')