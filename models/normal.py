import random


def normal_distribution(iterations, mean, std_dev):
    mean = float(mean)
    std_dev = float(std_dev)
    ri = 0.0
    ni = 0.0
    data = [[0 for _ in range(3)] for _ in range(iterations)]
    for i in range(iterations):
        ri = random.gauss(mean, std_dev)
        ni = mean + std_dev * ri
        data[i][0] = i
        data[i][1] = str("{:.5f}".format(ri))
        data[i][2] = str("{:.5f}".format(ni))
    return data


# if __name__ == '__main__':
    # print(normal_distribution(1000))
