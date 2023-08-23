fruit = "Pineapple"

# displays all characters
print(fruit[:])
# displays all characters from 0 to 0 1 is excluded
print(fruit[:1])
# displays all characters from 0 to 1 2 is excluded
print(fruit[:2])

print(fruit[1:3])

print(fruit[4:7])

len_fruit = len(fruit)
print('len_fruit', len_fruit)

# length of string is 9 .subtract 9-5=4 so slicing start from 4 and end at 9-1=8
print(fruit[-5:-1])

print(fruit[0:-3])