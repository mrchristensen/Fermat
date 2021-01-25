import random


def prime_test(N, k):
    return fermat(N, k), miller_rabin(N, k)


# Time Complexity: O(n(n^2+n^2)) = O(n^3)
# Space Complexity: O(n(3n)) = O(n^2)
def mod_exp(x, y, N):  # Algorithm from Figure 1.4
    if y == 0:  # Time Complexity: Runs y times, let it be n
        return 1

    z = mod_exp(x, y // 2, N)  # Time Complexity: division = O(n^2)
    if y % 2 == 0:  # If y is even
        return (z ** 2) % N  #
    else:  # If y is odd
        return (x * (z ** 2)) % N  # Time Complexity: mult and exp = O(n^2 + n^2) = O(n^2)


# Time Complexity: Divide and power = O(n^2 + (k)n^2) = O(n^2)
# Space Complexity: O(1)
def fprobability(k):  # From pg todo
    return 1 - (1 / 2) ** k


# Time Complexity: Divide and power = O(n^2 + (k)n^2) = O(n^2)
# Space Complexity: O(1)
def mprobability(k):  # From pg 28
    return 1 - (1 / 4) ** k


# Time Complexity: O(k(n^3)) = O(n^3)
# Space Complexity: O(k(n^2))
def fermat(N, k):  # Algorithm from Figure 1.8 (pg 27)
    if N == 1:
        return "composite"
    if N == 2:
        return "prime"

    # Time Complexity: runs k times
    for a in random.sample(range(2, N), min(k, N - 2)):  # Iter through a1, a2, ... , ak | 1 < a < n, and a is unique and random
        if mod_exp(a, N - 1, N) != 1:  # Time Complexity: O(n^3), Space Complexity: O(n^2)
            return "composite"

    return 'prime'

# Time Complexity: O(k(n^3 + log(exp)(n^3 + n^2))) = O(n^3 + log(exp)(n^3)) = O(log(exp)n^3)
# Space Complexity: O(k(n^2 + log(exp)n^2)) = O(log(exp)n^2)
def miller_rabin(N, k):
    if N == 1:
        return "composite"
    if N == 2:
        return "prime"

    # Time and Space Complexity: runs k times
    for a in random.sample(range(2, N), min(k, N - 2)):  # Iter through a1, a2, ... , ak | 1 < a < n, and a is unique and random

        # Equivalent to the Fermat Test
        res = mod_exp(a, N - 1, N)  # Time Complexity: O(n^3)
        if res != 1:
            return "composite"

        listofSqrt = []
        exp = (N - 1)

        # Time and Space Complexity: runs log(exp) times
        while (exp % 2 == 0):  # Square root until you get to an odd exponent
            listofSqrt.append(mod_exp(a, exp // 2, N))  # Space Complexity: n^2, Time Complexity: n^3
            exp = exp // 2  # Time Complexity: division = O(n^2)

        # Time Complexity: will be neglectable, because at most we just do a subtraction
        for sqrt in listofSqrt:  # Go through list of squares
            if sqrt != 1:  # If it's not 1
                if sqrt == N - 1:  # subtraction = O(1)
                    break  # May be prime, lets keep going
                else:  # And if it's not N-1 (or -1 % N - they are equivalent)
                    return "composite"  # Than it's composite

    return 'prime'  # We've gone through the a's and it look prime

# test
# for i in range(1,100):
#     if miller_rabin(i, 3) == "prime":
#         print(i)