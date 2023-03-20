import random


def uniform_distribution(lower_limit, upper_limit, iterations):
    data = [[0 for _ in range(3)] for _ in range(iterations)]
    for i in range(iterations):
        ri = random.random()
        data[i][0] = i
        data[i][1] = str("{:.5f}".format(ri))
        data[i][2] = str("{:.5f}".format((lower_limit + (upper_limit - lower_limit) * ri)))
    return data


if __name__ == '__main__':
    data = uniform_distribution(0, 10, 1000)
    print(data)
