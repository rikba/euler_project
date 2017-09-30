import time
import euler as e

no = 10001
prime = 2
start = time.time()
for i in range(1, no):
    prime = e.nextPrime(prime)
end = time.time()

print 'The brute force', no, 'prime is:', prime, 'calculated in', end - start, 's.'
