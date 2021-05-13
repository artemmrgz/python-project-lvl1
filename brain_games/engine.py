from brain_games.welcome import welcome_user
from brain_games.functions import is_even
import random


def play():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_rounds = 3
    while game_rounds:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        if is_even(number) == answer:
            print('Correct!')
            game_rounds -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
                    Correct answer was '{is_even(number)}'.")
            print(f'Let\'s try again, {name}!')
            break
    if not game_rounds:
        print(f'Congratulations, {name}!')
