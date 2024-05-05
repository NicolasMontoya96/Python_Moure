# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [28,30,53,44,30,17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.80, 'Nicolas', 'Montoya']

print(type(my_other_list))


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))


agre, height, name, surname = my_other_list
print(name)


my_other_list.append('MoureDev')
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Verde"
print(my_other_list)

my_other_list.remove("Verde")
print(my_other_list)


my_list.remove(30)
print(my_list)


print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)

del my_list[0]
print(my_list)

my_list.clear()
print(my_list)