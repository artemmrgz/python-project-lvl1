#!/usr/bin/env python3

from brain_games.engine import welcome_user, play
from brain_games.games import gcd


def main():
    name = welcome_user()
    print(gcd.TASK)
    play(name, gcd)


if __name__ == '__main__':
    main()
