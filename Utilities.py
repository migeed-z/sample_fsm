from random import random, sample

def choose_randomly(probabilities, speed):
    indicies = sample(range(0, len(probabilities)), speed)
    # s = accumulated_s(probabilities)
    # for i in range(speed):
    #     r = q or random()
    #     indicies = []
    #     counter = 0
    #     for percent in s:
    #         if percent >= r:
    #             indicies = indicies + [counter]
    #         counter=+1

    return indicies

# def accumulated_s(probabilities):
#     total = sum(probabilities)
#     payoffs = probabilities
#     result = []
#     next = 0
#     for element in payoffs:
#         next += element
#         result = result + [next/total]
#     return result

def relative_average(l, w):
    return sum(l) / w / len(l)

