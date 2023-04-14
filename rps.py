import random
import math


your_choice = input("type r for rock, p for paper, or s for scissors: ")

r1 = random. random()
r2 = math.floor(r1*3)

d = {}
d[0] = 'r'
d[1] = 'p'
d[2] = 's'

cpu_choice = d[r2]

if your_choice == 'r':
    if cpu_choice == 'r':
        print('tie')
    elif cpu_choice == 'p':
        print('you lose')
    else:
        print('you win')

if your_choice == 'p':
    if cpu_choice == 'r':
        print('you win')
    elif cpu_choice == 'p':
        print('tie')
    else:
        print('you lose')

if your_choice == 's':
    if cpu_choice == 'r':
        print('you lose')
    elif cpu_choice == 'p':
        print('you win')
    else:
        print('tie')



