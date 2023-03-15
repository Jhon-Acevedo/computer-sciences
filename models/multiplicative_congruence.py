class MultiplicativeCongruence:

    def __init__(self, x0, t, g) -> None: 
        self.x0 = x0
        self.a = 8*t+3
        self.m = int(2 ** g)

    def multiplicative_congruence(self, minium, maxium, iterations):
        data = [[0 for x in range(4)] for y in range(iterations)]
        for i in range(iterations):
            x_i = (self.a * self.x0) % self.m
            x_i_d = x_i
            number_ri = x_i_d / (self.m - 1)
            number_ni = minium + (maxium - minium) * number_ri
            data[i][0] = i + 1
            data[i][1] = x_i
            data[i][2] = number_ri
            data[i][3] = number_ni
            self.x0 = x_i
        return data

if __name__ == "__main__":
    multiplicative = MultiplicativeCongruence(5, 2, 10)
    datas = multiplicative.multiplicative_congruence(8, 10, 10)
    print(datas)