### Python Package Manager ###

# pip https://pypi.org

import numpy

import my_package.arithmetics # pip installa numpy

print(numpy.version.version)

numpy_array = numpy.array([28,30,53,44,30,17])
print(type(numpy_array))

print(numpy_array * 2)


# import pandas # pip install pandas
# pip list
# pip uninstall pandas

# pip install requests
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())


# Arithmetics Package
from my_package import arithmetics

print(my_package.arithmetics.sum_two_values(1, 4))


