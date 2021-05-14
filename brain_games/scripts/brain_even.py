#!/usr/bin/env python3

from brain_games.engine import play, welcome_user
from brain_games.games.even import generate_question, is_even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play(name, generate_question, is_even)


if __name__ == '__main__':
    main()
