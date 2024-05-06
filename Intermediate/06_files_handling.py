### File Handling ###

import os

# .txt file
txt_file = open('Intermediate/my_file.txt', 'w+') # Leer y escribir

txt_file.write('Mi nombre es Nicolas\nMi apellido es Montoya\n27 años\nLenguaje preferido es python')
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines(): # Leer cada línea con for
    print(line)

txt_file.write('\nAunque también me gusta Kotlin')
print(txt_file.readline())

txt_file.close()

# os.remove('Intermediate/my_file.txt') # Eiminar fichero


# .json file

import json

json_file = open('Intermediate/my_file.json', 'w+')

json_test = {   
    "name":"Nicolas",
    "surname":"Montoya",
    "age":27,
    "language": ["Python","Switf","Kotlin"],
    "website":"moure.dev"}

json.dump(json_test, json_file, indent=2)

json_file.close()


with open('Intermediate/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)
    


json_dict = json.load(open('Intermediate/my_file.json'))
print(json_dict)
print(type(json_dict))

print(json_dict["name"])

# .csv file
import csv

csv_file = open('Intermediate/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Nicolas", "Montoya", 27, "Python", "moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open('Intermediate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file
# import xlrd # Debe instalarse el módulo 


# .xml file
import xml