### Functions ###

def my_function ():
    print('Esto es una función')

my_function()
my_function()
my_function()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5,5)
sum_two_values(66,10)
sum_two_values("5","5")
sum_two_values(1.4,5.2)


def sum_two_values_with_return(firs_value, second_value):
    my_sum =  firs_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name('Nicolas', 'Montoya')

    

    