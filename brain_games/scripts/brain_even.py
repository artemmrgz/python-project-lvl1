#!/usr/bin/env python3

from brain_games.engine import play, welcome_user
from brain_games.games import even


def main():
    name = welcome_user()
    print(even.TASK)
    play(name, even)


if __name__ == '__main__':
    main()
