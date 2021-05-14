import random


def generate_question():
    number = random.randint(0, 100)
    print(f'Question {number}')
    return number


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
