from random import random

random_number=round(random() * 100)

hints=[
        f'The sum of the random number and 5 is {random_number + 5}',
        f'The mystery number divided by 10 is {random_number/10}',
        f'The multiplication of the random number with 14 is {random_number * 14}'
]

def game_start():
    while True:
        guest_number=int(input('Please guess a number between 0 and 100: '))
        if guest_number == random_number:
            print(f'Congratulation! You guessed right. The random number is {random_number}')
            
            quit()
        else:
            print('Incorrect! Please try again with a different number')
            x=round(random() * 2)
            print(f'{hints[x]}')
   
game_start()