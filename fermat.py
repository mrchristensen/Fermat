import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    if y == 0:
        return 1

    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:  # If y is even
        return (z ** 2) % N
    else:  # If y is odd
        return (x * (z ** 2)) % N


def fprobability(k):
    return 1 / 2 ** k


def mprobability(k):
    return (3 / 4) ** k  # todo: check to see if this is right


def fermat(N, k):
    randomNums = random.sample(range(1, N - 1),
                               k)  # todo: figure out if we need to handle when the user want to sample more than is possible (with mathfclamp or something)

    for a in randomNums:
        if mod_exp(a, N - 1, N) != 1:
            return "composite"

    return 'prime'


def miller_rabin(N, k):
    randomNums = random.sample(range(1, N - 1),
                               k)  # todo: figure out if we need to handle when the user want to sample more than is possible (with mathfclamp or something)

    for a in randomNums:

        res = mod_exp(a, N - 1, N)  # Equivalent to the Fermat Test
        if res != 1:
            return "composite"

        listofSqrt = []
        n = (N - 1)
        while (n % 2 == 0):  # Square root until you get to an odd exponent
            listofSqrt.append(mod_exp(a, n / 2, N))
            n = n // 2

        for sqrt in listofSqrt:  # Go through list of squares
            if sqrt != 1:  # If it's not 1
                if sqrt == N - 1:
                    break
                else:  # And if it's not N-1 (or -1 % N - they are equivalent)
                    return "composite"  # Than it's composite

    return 'prime'  # We've gone through the a's and it look prime
