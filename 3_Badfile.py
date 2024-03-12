Leo = {'name':'Leo','breed':'Golden Retriever','age':3, 'commands':['sit', 'up', 'roll-over', 'jump', 'paw']}
MAX = {'name': 'Max', 'breed': 'German Shepherd', 'age': 4, 'commands': ['stay', 'lie-down', 'heel', 'speak']}
luna = {'name': 'Luna', 'breed': 'Poodle', 'age': 1, 'commands': ['twirl', 'beg', 'crawl', 'quiet']}
def F(x):
    return 'name: ' + x['name'] + ', ' + 'breed: ' + x['breed'] + ', ' + 'age: ' + str(x['age'])
print('--------------------------')
def P(x):
    print(x)
I = input('What\'s your dog\'s name?: ' )
O = {'name': I, 'breed': 'Poodle', 'age': 1, 'commands': ['twirl', 'beg', 'crawl', 'quiet']}
P(F(O))
print('\n--')
print('\nBark Park: Welcome to the dog-park '+I +'.  We\'ll have lots of fun!', end='\n\n')
P(F(Leo))# show Leo
P(F(MAX)) # show Max
P(F(luna)) # show Luna
print('\nIn the whimsical canine haven of Bark Park, established in 1887, playful pups and their owners have forged lasting friendships, creating a legacy of tail-wagging joy and delightful chaos.')
print('\n--')
print('\nMeow Wow: Welcome to the cat-park '+I +'.  We\'ll have lots of fun!', end='\n\n')
Lily = {'breed': 'Persian cat', 'commands': ['knock-over-cup'], 'name': 'Lily', 'age': 1}
Tom = {'age': 2, 'commands': ['sit'], 'breed': 'Ragdoll cat', 'name': 'Tom'}
CattyMcCatFace = {'age': 10, 'commands': ['quiet'], 'breed': 'Bengal cat', 'name': 'Luna'}
P(F(Lily) + '\n' + F(Tom) + '\n' + F(CattyMcCatFace))
print('\nIn the whimsical cat haven of Meow Wow, established in 1999, playful cats and their owners have forged lasting friendships, creating a legacy of tail-wagging joy and delightful chaos.')
print('\n--------------------------')
w = int(input('Where would you like to go (1-Bark Park, 2-Meow Wow): '))
if w==1:
    print(f'{I} loves it here!', f"{I} became best friends with Tom!")
else:
    print(f'{I} dislikes it here; {I} didn\'t make any new friends :(')
