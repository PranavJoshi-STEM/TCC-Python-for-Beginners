# Conditionals (if, elif, else)
# + error-handling (try, except, finally)
"""
If their mark is:
  1) 100 --> print('A+)
  2) 99-90 --> print('A')
  3) 89-75 --> print('B')
  4) 74-60 --> print('C')
  5) 60-50 --> print('D')
  6) 50> --> print('F')

"""
done = False
while not done:
    try:
        mark = int(input())
        done = True
        if mark == 100:
            print('A+')
        elif mark >= 90:
            print('A')
        elif mark >= 75:
            print('B')
        elif mark >= 60:
            print('C')
        elif mark >= 50:
            print('D')
        else:
            print('F')
    except:
        print('Code failed!  Input was not a valid integer.')

print('Program is finished')