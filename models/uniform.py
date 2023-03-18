import random
import statistics


def uniform_distribution(lower_limit, upper_limit, iterations):
    data = [[0 for _ in range(3)] for _ in range(iterations)]
    for i in range(iterations):
        ri = random.uniform(lower_limit, upper_limit)
        data[i][0] = i
        data[i][1] = str("{:.5f}".format(ri))
        data[i][2] = str("{:.5f}".format((lower_limit + (upper_limit - lower_limit) * ri)))
        # data[1][2] = statistics.NormalDist.inv_cdf(ri)
    return data


if __name__ == '__main__':
    # print(uniform_distribution(-3.6978, 3.6978, 15000))
    # data = statistics.NormalDist.inv_cdf(p=0.806449788)
    # dist = statistics.NormalDist(mu=5, sigma=2)
    # value = dist.inv_cdf(p=0.8)
    # print(value)
    print(uniform_distribution(0, 10, 1000))
