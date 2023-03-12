class MultiplicativeCongruence:

    def __init__(self, x0, t, g) -> None: 
        self.x0 = x0
        self.a = 8*t+3
        self.m = int(2 ** g)

    def multiplicative_congruence(self, minium, maxium, iterations):
        data = [[0 for x in range(4)] for y in range(iterations)]
        for i in range(iterations):
            pass
