def mean_square_implementation(seed, minimum, maximum, iterations):
    seed = int(seed)
    minimum = int(minimum)
    maximum = int(maximum)
    iterations = int(iterations)

    seed_extension = len(str(seed))
    x_i = seed
    data = [[0 for x in range(7)] for y in range(iterations)]
    i = 0
    while i < iterations:
        x_i_square = pow(x_i, 2)
        square_seed = str(x_i_square)
        square_extension = len(square_seed)
        primerc = (square_extension - seed_extension) / 2
        extraction = square_seed[int(primerc):int(primerc + seed_extension)]
        number_ri = int(extraction) / pow(10, seed_extension)
        number_ni = minimum + (maximum - minimum) * number_ri
        data[i][0] = i
        data[i][1] = x_i
        data[i][2] = x_i_square
        data[i][3] = square_extension
        data[i][4] = extraction
        data[i][5] = number_ri
        data[i][6] = number_ni
        x_i = int(extraction)
        i += 1
    return data
