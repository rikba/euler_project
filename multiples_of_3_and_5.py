import time
import euler as e

upper_limit = 1000
start = time.time()
brute_force = e.sumOfMultiplesOfXOrY(3, 5, upper_limit)
end = time.time()
print 'The brute force sum of all multiples of 3 or 5 below', upper_limit, 'is:', brute_force, 'calculated in', end - start, 's.'

start = time.time()
effective = e.sumOfMultiplesOfX(3, upper_limit) + e.sumOfMultiplesOfX(5, upper_limit) - e.sumOfMultiplesOfX(15, upper_limit)
end = time.time()
print 'The effective sum of all multiples of 3 or 5 below', upper_limit, 'is:', effective, 'calculated in', end - start, 's.'
