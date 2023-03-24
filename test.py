# Disc 03
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


# print(multiply(5, 4))
# print(is_prime(2))
# print(is_prime(16))
# print(is_prime(521))
# print(count_stair_ways(4))
# print(merge(31, 42))
# a = hailstone(10)
# print(a)
# b = hailstone(1)
# print(b)
# print(count_k(10, 3))
# print(count_k(300, 1))
# print(count_k(3, 3))
# print(count_k(4, 4))

# Disc 04
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    ret = []
    for elem in seq:
        ret.append(fn(elem))
    return ret


# print(my_map(lambda x: x*x, [1, 2, 3]))

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    ret = []
    for elem in seq:
        if pred(elem):
            ret.append(elem)
        else:
            continue
    return ret


# print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    result = seq[0]
    for elem in seq[1:]:
        result = combiner(result, elem)
    return result


# print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4]))
# print(my_reduce(lambda x, y: x * y, [1, 2, 3, 4]))
# print(my_reduce(lambda x, y: x * y, [4]))
# print(my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]))

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    count = 0
    for elem in L:
        if elem.lower() == elem[::-1].lower():
            count += 1
    return count


# print(count_palindromes(("Acme", "Madam", "Pivot", "Pip")))
# print(count_palindromes('hhhhh'))

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    ret = []
    i = 0
    for elem in s:
        if i % 2 == 0:
            ret.append(elem*i)
        i += 1
    return ret


# print(even_weighted([1, 2, 3, 4, 5, 6]))

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    product1 = 0
    product2 = 0
    ret = 0
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        max_seq_1 = max_product(s[2:])
        max_seq_2 = max_product(s[3:])
        if max_seq_1 > 1:
            product1 = max_seq_1*s[0]
        else:
            product1 = s[0]
        if max_seq_2 > 1:
            product2 = max_seq_2*s[1]
        else:
            product2 = s[1]
        ret = max(product1, product2)
    return ret


# print(max_product([10, 3, 1, 9, 2]))
# print(max_product([5, 10, 5, 10, 5]))
# print(max_product([]))


