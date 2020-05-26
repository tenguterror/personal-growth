# Long way of typing it

name = 'Duard'
age = 36
print('Hello, \nMy name is ' + name + '. \nI am ' + str(age) + ' years old.')

# This is using string interpolation. Notice the %s will call the variable

print('Hello, \nMy name is %s. \nI am %s years old.' % (name, age))

# As of python 3.6 f strings are now available. This is the perfered method. use f'fdasdfasdf{defined variable}'. I think the cleaner way of doing it.

print(f'Hello, \nMy name is {name}. \nNext year I will be {age + 1} years old.')
