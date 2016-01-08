from random import random, sample

rand = (list(map(int, [line.strip() for line in open('random-numbers.txt')])))

def choose_randomly(speed):
    #indicies = sample(range(0, len(probabilities)), speed)
    indicies = [i for i in rand if (i <= speed)][:speed]
    return indicies

def relative_average(l, w):
    return sum(l) / w / len(l)

