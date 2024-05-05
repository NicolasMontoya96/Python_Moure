# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.80, "Nicolas", "Montoya", "Nicolas")
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])


print(my_tuple.count("Nicolas")) 
print(my_tuple.index("Montoya")) 
print(my_tuple.index("Nicolas"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Verde")
print(tuple(my_tuple))


del my_tuple
print(my_tuple)