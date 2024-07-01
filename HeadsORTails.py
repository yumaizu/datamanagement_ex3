#!/bin/python

import random

class Coin:
    sides = ['Heads', 'Tails']

    def flip():
        return random.choice(Coin.sides)

if __name__ == '__main__':
    name = input("Who are you?\n")
    print("Hello, {}!".format(name))

    num_rounds = 3
    num_heads = 0
    num_tails = 0

    for i in range(num_rounds):
        flip = Coin.flip()
        if flip == 'Heads':
            num_heads += 1
        else:
            num_tails += 1
        print("Round {}: {}".format(i+1, flip))
    print("Heads: {}, Tails: {}".format(num_heads, num_tails))
    print(name+ (" won!" if num_heads > num_tails else " lost!"))