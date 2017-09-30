import math

# Brute force returns the sum of all multiples of x or y up to upper_limit.
def sumOfMultiplesOfXOrY(x, y, upper_limit):
    result = 0
    for i in range(0, upper_limit):
        if (i % x == 0 or i % y == 0):
            result = result + i
    return result

# Effectively returns the sum of all multiples of x or y up to upper_limit.
def sumOfMultiplesOfX(x, upper_limit):
    p = (upper_limit - 1) // x
    return x * (p * (p + 1)) // 2

# Return Fibonacci sequence up to upper limit.
def getFibonacciSequence(upper_limit):
    result = [1]
    next = 2
    while next <= upper_limit:
        result.append(next)
        next = result[-2] + result[-1]
    return result

# Return if a number is prime.
def isPrime(x):
    if x <= 1:
        return False
    elif x < 4: # 2 and 3 are prime
        return True
    elif x % 2 == 0:
        return False
    elif x < 9: # 4, 6, 8 already excluded, include 5, 7
        return True
    elif x % 3 == 0:
        return False
    else:
        # All primes greater than 3 can be written in the form 6k +/- 1
        # Any number x can have only one primefactor greater than sqrt(x)
        r = math.floor(math.sqrt(x))
        f = 5
        while f <= r:
            if x % f == 0:
                return False
            elif x % (f + 2) == 0:
                return False
            f = f + 6
    return True

# Return the next prime.
def nextPrime(x):
    result = x + 1
    while not isPrime(result):
        result = result + 1
    return result

# Return all prime factors of a number.
def getPrimeFactors(x):
    result = []
    remainder = x
    divisor = 2
    while remainder is not 1:
        if remainder % divisor == 0:
            remainder = remainder / divisor
            result.append(divisor)
        else:
            divisor = nextPrime(divisor)
    return result

# Return if number is palindrom.
def isPalindrom(x):
    return str(x) == str(x)[::-1]

# Return the largest palindrome of two x-digit numbers.
def getLargestPalindrome(x):
    all_products = []
    for i in range(10 ** (x - 1), 10 ** x):
        for j in range(i, 10 ** x):
            all_products.append(i * j)
    all_products.sort(key=int, reverse=True)
    for product in all_products:
        if isPalindrom(product):
            return product
    return -1

def isEvenlyDivisible(x, rng):
    for i in rng:
        if x % i is not 0:
            return False
    return True

# Return the smallest number that is evenly divisible by all numbers from 1 to x
def getSmallestEvenlyDivisible(x):
    result = x
    rng = range(x, 1, -1)
    while not isEvenlyDivisible(result, rng):
         result = result + x
    return result

# Return the sum of squares for vector 1 to n.
def calculateSumOfSquares(n):
    return n / 6 * (2 * n + 1) * (n + 1)

# Return the square of sum for vector 1 to n.
def calculateSquareOfSums(n):
    return ((n * (n+1) / 2) ** 2)

def int2List(n):
    return [int(i) for i in str(n)]

def productOfList(l):
    if not l:
        return 0
    result = 1
    for x in l:
        result = result * x
    return result

# Return the product of all size adjacent numbers in n.
def calculateMovingWindowProduct(n, size):
    l = int2List(n)
    result = []
    start = 0
    end = size
    while end <= len(l):
        result.append(productOfList(l[start:end]))
        start = start + 1
        end = end + 1
    return result

def solvePQ(p, q):
    a = -p / 2
    b = sqrt(p ** 2 - 4 * q) / 2
    return a + b, a - b
