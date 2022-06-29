def largest_prime_factor(n):
    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n // i))
def is_prime(m):
    return all(m % i for i in range(2, m-1))
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
