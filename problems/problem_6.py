
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def get_primes(max_num):
    primes = []
    for i in range(1, max_num + 1):
        if is_prime(i):
            primes.append(i)

    return primes

num = int(input("Search for prime numbers up to: "))

for prime in get_primes(num):
    print(prime)
