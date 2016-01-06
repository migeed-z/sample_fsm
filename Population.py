from random import shuffle
from Utilities import choose_randomly

class Population:
    """
    Populations of Automata
    """

    def __init__(self, a):
        self.a = a

    def payoffs(self):
        result = []
        for element in self.a:
            result = result + [element.pay()]
        return result

    def match_up(self, r):
        """
        matches up neighboring pairs of
        automata in this population for r rounds
        :return: Population
        """
        self.reset()
        for i in range(0, round(len(self.a)/2)):
            p1 = self.a[i]
            p2 = self.a[i+1]
            [a1, a2] = p1.interact(p2, r)
            self.a[i] = a1
            self.a[i+1] = a2
        return self

    #how do we union types in retic?
    def regenerate(self, rate, q=False):
        """
        Replaces r elements of p with r 'children' of randomly chosen
        fittest elements of p, also shuffle constraint (r < (len p))
        :param rate: Number of elements to replace in a
        :param q: threshold
        :return: Population
        """
        payoffs = self.payoffs()
        substitutes = choose_randomly(payoffs, rate)
        # clone all automata in a at substitues
        b = self.a.copy()
        # then "move" these clones into the first "rate" slots of a
        for i in range(rate):
            index = substitutes[i]
            self.a[i] = b[index]
        shuffle(self.a)
        return self

    def reset(self):
        """
        Reset all automata in a
        :return: None
        """
        for element in self.a:
            element.reset()


