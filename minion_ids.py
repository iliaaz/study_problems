from timeit import timeit


def generateprimes(upper_bound):
    return generateprimes_boolvector(upper_bound)


def generateprimes_filter(upper_bound=100000):
    primes = list(range(2, upper_bound + 1))

    i = 0
    while primes[i] < upper_bound**0.5:
        primes = list(filter(lambda x: x == primes[i] or x % primes[i] != 0, primes))
        i += 1

    return list(primes)


def generateprimes_boolvector(upper_bound=100000):
    primes = [True] * (upper_bound + 1)
    primes[0] = primes[1] = False

    for n, isprime in enumerate(primes):
        if isprime and n < upper_bound**0.5:
            for i in range(n**2, upper_bound + 1, n):
                if i % n == 0:
                    primes[i] = False

    return [value for value, isprime in enumerate(primes) if isprime]


def solution(n):
    primestring = "".join(str(num) for num in generateprimes((int(n * 2.5) + 100)))
    return primestring[n: n + 5]


if __name__ == "__main__":
    assert solution(3) == "71113"
    assert generateprimes_filter(760) == generateprimes_boolvector(760)
    print(timeit(generateprimes_filter, number=10))
    print(timeit(generateprimes_boolvector, number=10))
