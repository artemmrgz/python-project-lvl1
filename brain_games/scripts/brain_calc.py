#!/usr/bin/env python3

from brain_games.engine import play, welcome_user
from brain_games.games import calc


def main():
    name = welcome_user()
    print(calc.TASK)
    play(name, calc)


if __name__ == '__main__':
    main()
