#!/usr/bin/env python3

from brain_games.engine import play, welcome_user
from brain_games.games.calc import generate_question, calculate


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    play(name, generate_question, calculate)


if __name__ == '__main__':
    main()
