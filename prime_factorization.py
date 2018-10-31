def SieveOfEratosthenes(limit): 
    # Create a boolean array "prime[0..limit]" and initialize all entries as True.  Value i will be set to False if it is a multiple of any smaller number. 
    prime = [True for j in range(limit + 1)] 
    for i in range(2, limit + 1):
        if (prime[i] == True): 
            yield i
            # All multiples of p are not prime
            for j in range(i * i, limit + 1, i): 
                prime[j] = False


def prime_factorize(number, result):
    for prime in primes:
        if (prime > number):
            return result
        if (number % prime == 0):
            result.append(prime)
            return prime_factorize(int(number / prime), result)


numbers = sorted([3, 3 * 3, 2 * 3 * 4 * 5, 32 * 9 * 25, 39874191])
primes = list(SieveOfEratosthenes(max(numbers)))
print("There are", len(primes), "primes between", 2, "and", max(numbers), flush=True)
for number in numbers:
    print ("The prime factorization of", number, "is", prime_factorize(number, []), flush=True)
