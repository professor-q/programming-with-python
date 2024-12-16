# It is possible to assign values to multiple variables in one line
x, y, z = 'Orange', 'Banana', 'Cherry'
print(x, y, z)
print(x + y + z)

# Assigning same value into multiple variables
x = y = z = 67
print(x, y, z)

# Unpack a Collection
fruits = ['Apple', 'Banana', 'Cherry']
x, y, z = fruits
print(x, y, z)
