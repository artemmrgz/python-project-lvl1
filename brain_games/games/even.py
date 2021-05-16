import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    number = random.randint(0, 100)
    return number


def ask_question(number):
    print(f'Question: {number}')


def solve(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
