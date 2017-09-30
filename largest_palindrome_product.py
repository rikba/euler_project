import time
import euler as e

factor_digits = 3
start = time.time()
palindrome = e.getLargestPalindrome(factor_digits)
end = time.time()

print 'The brute force largest palindrome product for', factor_digits, 'digit factors is:', palindrome, 'calculated in', end - start, 's.'
