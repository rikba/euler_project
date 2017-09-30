import time
import euler as e

upper_limit = 20
start = time.time()
smallest_multiple = e.getSmallestEvenlyDivisible(upper_limit)
end = time.time()

print 'The brute force smallest evenly dividible multiple number by all numbers from 1 to', upper_limit, 'is:', smallest_multiple, 'calculated in', end - start, 's.'
