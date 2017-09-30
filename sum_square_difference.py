import time
import euler as e

upper_limit = 100
start = time.time()
sum_squares = e.calculateSumOfSquares(upper_limit)
square_sum = e.calculateSquareOfSums(upper_limit)
result = square_sum - sum_squares
end = time.time()

print 'The difference between the sum of squares of the first', upper_limit, 'natural numbers and the square of the sum is:', result, 'calculated in', end - start, 's.'
