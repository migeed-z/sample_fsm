from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from Automata import Automaton
from Population import Population
import random

def make_random_automaton(n):
    """
    builds an n states x k inputs automation
    with a random transition table
    :param n:
    :return: Automation
    """
    seed = random.randrange(n)
    table = []
    for i in range(0, n):
        trans = random.sample(xrange(n), n)
        table = table + [trans]
    return Automaton(seed, 0, table, seed)


def build_random_population(n):
    """
    for even n, build a population of size n
    :param n: Natural
    :return: Population
    """
    DEF_COO = 2
    v = []
    for i in range(n):
        v = v + [make_random_automaton(DEF_COO)]
    return Population(v)









