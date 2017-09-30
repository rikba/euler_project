import time
import euler as e

upper_limit = 4 * 10**6
start = time.time()
fibonacci_sequence = e.getFibonacciSequence(upper_limit)
sum_even = sum([x for x in fibonacci_sequence if x % 2 == 0])
end = time.time()

print 'The brute force sum of all even numbers in a Fibonacci sequence up to', upper_limit, 'is:', sum_even, 'calculated in', end - start, 's.'
