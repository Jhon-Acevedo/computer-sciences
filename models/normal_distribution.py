import random


class NormalDistribution:
    def __init__(self, mean, std_dev):
        self.mean = mean
        self.std_dev = std_dev

    def sample(self, iterations=10):
        data = [[0 for x in range(3)] for y in range(iterations)]
        for i in range(iterations):
            r_i = random.gauss(mu=0.0, sigma=1.0)
            n_i = self.mean + self.std_dev * r_i
            data[i][0] = i + 1
            data[i][1] = r_i
            data[i][2] = n_i
        return data


if __name__ == "__main__":
    normal = NormalDistribution(0.0, 1.0)
    print(normal.sample(50))
