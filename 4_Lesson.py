# ------ Strings ------
# Essentials
print(('Whoa' + ' ')*12)  # String concatenation
print(len('ᕕ( ᐛ )ᕗ'))  # Get the length of a string
# convert things to string
print(type(str(123)), str(123))
print(type(str([1, 2, 3])), str([1, 2, 3]))
print(type(str({1, 2, 3})), str({1, 2, 3}))

# indexes
# strings are accessed through slices
s = 'Hey there!'
# access through square brackets
# string[first_index(inclusive):last_index(exclusive):step]
# for example
# A string has indexes like this:
# 'example' --> 'e' 'x' 'a' 'm' 'p' 'l' 'e'
#                0   1   2   3   4   5   6
#               -7  -6  -5  -4  -3  -2  -1   
print(s[0:3])
# strings are immutable so you cant overwrite certain sections,
# only the entire thing
print(s[::2])  # step skips characters
print(s[::-1])  # negative step can go backwards

# functions
s = 'qwertyuiopasdfghjklzxcvbnm1234567890q'  # create new string
s.find('q')
s.rfind('q')
s.replace('qwerty', 'HI!!!!!', -1)
('aaaaaaaaaa').count('aa') # only non-overlapping occurences
print(s)


# ------ Lists ------
spells = ['Fire', 'Ice', 'Lightning', 'Wind']  # 🧙‍♂️
# access a certain element or a list of elements
print(spells[0])
print(spells[0:2])
# replace certain elements in lists
spells[0:2] = ['Hi', 'Car']
print(spells)
# changing the list
# get index
spells.index('Fire') # returns error if item is not found
spells.insert(0, 'Earth') # puts item in index, error if index is out of range
spells.pop(3) # error if index is out of range
spells.remove('Fire')
# you can do some mathematical operations
ages = [8, 10, 18, 12, 13, 2, 80]
ages.sort(reverse=False)
ages = sorted(ages)
ages = ages.reverse()
# calculate the minimum value, maximum value, or sum
min(ages)
max(ages)
sum(ages)


# ------ Dictionaries ------
spell_dmg = {'Fire':10, 'Dark':20, 'Wind':20}

spell_dmg.update({'Fire':15})

spell_dmg.pop('Fire')

spell_dmg['Fire']

print(list(spell_dmg.values()))
print(list(spell_dmg.keys()))
print(list(spell_dmg.items()))