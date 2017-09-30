import time
import euler as e

x = 600851475143
start = time.time()
prime_factors = e.getPrimeFactors(x)
end = time.time()

print 'The brute force prime factor search of', x, 'results in:', prime_factors, 'calculated in', end - start, 's.'
