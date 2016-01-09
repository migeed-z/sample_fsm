from Automata import Automaton
from Population import Population
from Utilities import rand


def make_random_automaton(n: int):
    """
    builds an n states x k inputs automation
    with a random transition table
    :param n:
    :return: Automation
    """

    index = next(i for i in range(0, 10000) if rand[i] <= n)
    seed = rand[index]

    table = []
    for i in range(n):
        trans = [i for i in rand if (i <= n)][:n]

        #trans = random.sample(xrange(n), n)
        table = table + [trans]
    return Automaton(seed, 0, table, seed)


#TODO: cannot add return type due to bug
def build_random_population(n: int):
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









