def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m*n
    else:
        return m+multiply(m, n-1)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(n):
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True
    return helper(n)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    count = 0

    def cnt(n, count=0):
        print(int(n))
        count += 1
        if not n == 1:
            if n % 2 == 0:
                return cnt(n/2, count)

            else:
                return cnt(3*n+1, count)
        return count
    return cnt(n, count)


def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    digits = []
    while n1 > 0:
        digits.append(n1 % 10)
        n1 //= 10
    while n2 > 0:
        digits.append(n2 % 10)
        n2 //= 10
    digits = sorted(digits, reverse=True)
    tmp = 0
    for elem in digits:
        tmp = tmp*10+elem
    return tmp


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)


def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    memo = {}
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        if n in memo:
            return memo[n]
        count = 0
        for i in range(1, k+1):
            count += count_k(n-i, k)
        memo[n] = count
        return count


#  print(multiply(5, 4))
print(is_prime(2))
print(is_prime(16))
print(is_prime(521))
#  print(count_stair_ways(4))
# print(merge(31, 42))
# a = hailstone(10)
# print(a)
# b = hailstone(1)
# print(b)
# print(count_k(10, 3))
# print(count_k(300, 1))
# print(count_k(3, 3))
# print(count_k(4, 4))
