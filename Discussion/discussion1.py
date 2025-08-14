# Q1: Race
# Disciption: find the pair of (x, y) such that race(x, y) gives the wrong answer or run forever.
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

"""
Discussion:
The problem is that, the function counts by minutes, which doesn't detect the time between integer minutes.
For example, when x is irrational and y is rational, they never meet at time>0, so race() runs forever.
Even if x and y has a common multiplier， when 2x doesn't divide y, the first few encounters will be omissed."""

# Q2: Fizz-Buzz
# Discription: Implement Fizz-Buzz Sequence
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    assert isinstance(n, int) and n > 0, "n should be a positive integer"
    def is_threes(n):
        return False if n % 3 else True
    def is_fives(n):
        return False if n % 5 else True
    
    for i in range(1, n+1):
        if is_threes(i) and not is_fives(i):
            print("fizz")
        elif not is_threes(i) and is_fives(i):
            print("buzz")
        elif is_threes(i) and is_fives(i):
            print("fizzbuzz")
        else:
            print(i)