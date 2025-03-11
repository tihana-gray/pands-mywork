# generate primes
# Author: Tihana Gray

primes = []

for candidate in range (2, 101):
    # print(candidate)
    is_prime = True
    for divisor in range(2, candidate):
        if (candidate % divisor == 0):
            is_prime = False
            break
        
    if is_prime:
        primes.append(candidate)

print(primes)
