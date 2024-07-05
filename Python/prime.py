# create an algorithm that returns a list of primes up until a given number x
def get_primes(x):
    primes = [True] * (x + 1)

    primes[0] = False
    primes[1] = False

    for i in range(2, x + 1):
        # if a num is prime...
        if primes[i]:
            # then mark all of its multiplies as non-prime
            for j in range(i + 1, x + 1):
                if j % i == 0:
                    primes[j] = False

    return [i for i in range(x + 1) if primes[i]]

print(get_primes(23))
print(get_primes(50))
