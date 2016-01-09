from retic import List

#TODO: add type to variable
rand = (list(map(int, [line.strip() for line in open('random-numbers.txt')])))

def choose_randomly(speed: int) -> List(int):
    indicies = [i for i in rand if (i <= speed)][:speed]
    return indicies

def relative_average(l: List(float), w: float) -> float:
    return sum(l) / w / len(l)

