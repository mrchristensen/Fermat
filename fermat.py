import random


def prime_test(N, k):
    return fermat(N, k), miller_rabin(N, k)


# Algorithm from Figure 1.4
def mod_exp(x, y, N):  # Time Complexity: O(n(n^2+n^2)) = O(n^3)
    if y == 0:  # Time Complexity: Runs y times, let it be n
        return 1

    z = mod_exp(x, y // 2, N)  # Time Complexity: division = O(n^2)
    if y % 2 == 0:  # If y is even
        return (z ** 2) % N  #
    else:  # If y is odd
        return (x * (z ** 2)) % N  # Time Complexity: mult and exp = O(n^2 + n^2) = O(n^2)


# From pg todo
def fprobability(k):
    return 1 - (1 / 2) ** k  # Time Complexity: Divide and power = O(n^2 + n^2) = O(n^2)


# From pg 28
def mprobability(k):
    return 1 - (1 / 4) ** k  # Time Complexity: Divide and power = O(n^2 + n^2) = O(n^2)


# Algorithm from Figure 1.8 (pg 27)
def fermat(N, k):  # Time Complexity: O(k(n^3)) = O(n^3)
    if N == 1:
        return "composite"

    randomNums = random.sample(range(1, N), min(k, N - 1))  # Generate k random nums (with no repeats) where 0 < a < n and is unique

    # Time Complexity: runs k times
    for a in randomNums:  # Iter through a1, a2, ... , ak
        if mod_exp(a, N - 1, N) != 1:  # Time Complexity: O(n^3)
            return "composite"

    return 'prime'


def miller_rabin(N, k): # Time Complexity: O(k(n^3 + n(n^2))) = O(n^3)
    randomNums = random.sample(range(1, N), min(k, N - 1))  # todo: check this

    # Time Complexity: runs k times
    for a in randomNums:

        # Equivalent to the Fermat Test
        res = mod_exp(a, N - 1, N)  # Time Complexity: O(n^3)
        if res != 1:
            return "composite"

        listofSqrt = []
        n = (N - 1)
        # Square root until you get to an odd exponent
        while (n % 2 == 0):  # Time Complexity: runs (1/2)n times
            listofSqrt.append(mod_exp(a, n / 2, N))
            n = n // 2  # Time Complexity: division = O(n^2)

        # Go through list of squares
        for sqrt in listofSqrt:  # Time Complexity: run todo times
            if sqrt != 1:  # If it's not 1
                if sqrt == N - 1:  # subtraction = O(1)
                    break
                else:  # And if it's not N-1 (or -1 % N - they are equivalent)
                    return "composite"  # Than it's composite

    return 'prime'  # We've gone through the a's and it look prime