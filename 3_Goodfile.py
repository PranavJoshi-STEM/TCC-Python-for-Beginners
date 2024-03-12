"""
Description:
    This program presents the user with 2 options of parks to choose from.  If
    they put their dog in the dog park, their dog will be happy.  Else, their
    dog will be sad if kept with all the cats!
Date:
    February 21st, 2024
"""

# ------ Imports (there are none) ------
# Example: import time


# ------ Constants------ 
# Dogs
LEO = {'name':'Leo', 'breed':'Golden Retriever', 'age':3,
       'commands':['sit', 'up', 'roll-over', 'jump', 'paw'],
    }
MAX = {'name':'Max', 'breed':'German Shepherd', 'age':4,
       'commands':['stay', 'lie-down', 'heel', 'speak'],
    }
LUNA = {'name':'Luna', 'breed':'Poodle', 'age':1, 
        'commands':['twirl', 'beg', 'crawl', 'quiet'],
    }
# Cats
LILY = {'name':'Lily', 'breed':'Persian cat', 'age':1,
        'commands':['knock-over-cup'],
    }
TOM = {'name':'Tom', 'breed':'Ragdoll cat', 'age':2,
       'commands':['sit'],
    }
CATTY_MC_CAT_FACE = {'name':'Luna', 'breed':'Bengal cat', 'age':10,
                     'commands': ['quiet'],
    }


# ----- Functions ------
# Returns a string of the animal's stats
def return_stats(animal):
    STATS_STR = f"name: {animal['name']}, breed: {animal['breed']}, \
age: {str(animal['age'])}"
    return STATS_STR


# prints out the animal (could be formatted if wanted)
def print_animal(animal):
    print(animal)


# ------ Input ------
def main():
    print('--------------------------')
    DOG_NAME = input("What's your dog's name?: ")


    # ------ Process ------
    DOG_STATS = {'name':DOG_NAME, 'breed':'Poodle', 'age':1,
                'commands':['twirl', 'beg', 'crawl', 'quiet'],
        }
    print_animal(return_stats(DOG_STATS))


    # ------ Output ------
    # Print Dog Park
    print()
    print('--')
    print()
    print(f"Bark Park: Welcome to the dog-park {DOG_NAME}.  We'll have lots of fun!")
    print()
    print()
    # Stats
    print_animal(return_stats(LEO))
    print_animal(return_stats(MAX))
    print_animal(return_stats(LUNA))
    # Description
    print()
    print('In the whimsical canine haven of Bark Park, established in 1887,',
    'playful pups and their owners have forged lasting friendships, creating a',
    'legacy of tail-wagging joy and delightful chaos.')

    # Print Cat Park
    print()
    print('--')
    print()
    print(f"Meow Wow: Welcome to the cat-park {DOG_NAME}.  We'll have lots of fun!")
    print()
    print()
    # Stats
    print_animal(return_stats(LILY))  # Changed this to be multiple lines because
    print_animal(return_stats(TOM))   # Consistency is *key*
    print_animal(return_stats(CATTY_MC_CAT_FACE))
    # Description
    print()
    print('In the whimsical cat haven of Meow Wow, established in 1999, playful',
          'cats and their owners have forged lasting friendships, creating a'
          'legacy of tail-wagging joy and delightful chaos.')

    # Display response towards where the dog is going
    print()
    print('--------------------------')
    # Ask for location
    LOCATION = int(input('Where would you like to go \
(1-Bark Park, 2-Meow Wow): '))
    # Return Response
    if LOCATION == 1:
        print(f'{DOG_NAME} loves it here!',
            f'{DOG_NAME} became best friends with Tom!')
    else:
        # Consistency
        print(f'{DOG_NAME} dislikes it here;',
            f"{DOG_NAME} didn't make any new friends :(")


# ------ Entry point of script ------
if __name__ == '__main__':
    main()