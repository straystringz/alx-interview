#!/usr/bin/python3

"""Winner Prime"""

def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def can_win(n):
        # If n is even, Maria wins; otherwise, Ben wins
        return n % 2 == 0

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if is_prime(n):
            if can_win(n):
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None

# Test the function with the given example
x = 3
nums = [4, 5, 1]
result = isWinner(x, nums)
print(result)  # Output should be "Ben" as Ben wins 2 rounds and Maria wins 1 round.

