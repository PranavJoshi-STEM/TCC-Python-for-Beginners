# Conditionals
a = int(input())
b = int(input())

if a==b:
    print('a and b are the same!')
elif a<b:
    print('b is greater than a!')
else:
    print('a is greater than b!')


# try-except
try:
    print(10/0)
except:
    print("Whoa, that didn't work!")
finally:
    print('Finally block executed!')


# loops
spells = ['Fire', 'Water', 'Wind', 'Earth']
for i in range(10):
    print(i)

i = 0
while i < 10:
    i+=1
    print(i)