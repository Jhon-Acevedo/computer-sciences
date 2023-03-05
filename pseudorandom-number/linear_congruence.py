class LinearCongruence:
    
    def __init__(self,x0,k,c,g) -> None:
        self.x0 = x0
        self.a = 1 + 2 * k
        self.c = c
        self.m = int(2 ** g)
    

    def implementation(self,minium, maximum, iterations):
        
        data = [[0 for x in range(4)] for y in range(iterations)]
        for i in range(iterations):
            x_i = ((self.a * self.x0) + self.c) % self.m
            aux_x_i = x_i
            number_r_i = aux_x_i / (self.m - 1)
            number_n_i = minium + (maximum - minium) * number_r_i
            self.x0 = x_i
            data[i][0] = i + 1
            data[i][1] = x_i
            data[i][2] = number_r_i
            data[i][3] = number_n_i
        return data


if __name__ == "__main__":
    linear = LinearCongruence(1,4,3,7)
    datas = linear.implementation(1,50,10)
    print(datas)
