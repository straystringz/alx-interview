#!/usr/bin/python3

"""
   Problem:
   In a text file, there is a single character 'H'. Your text editor
   can perform only two operations: Copy All and Paste. Given a number n,
   write a function that calculates the fewest number of operations needed
   to result in exactly n 'H' characters in the file.

   Approach:
   We can find the fewest number of operations by finding the prime factors
   of n and summing them up. Each prime factor represents the number of times
   we need to perform the Copy All and Paste operations.

   Example:
   For n = 12, the prime factors are 2 * 2 * 3.
   So, the fewest number of operations needed is 2 + 2 + 3 = 7.
"""


def minOperations(n):
    num_ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            num_ops += min_ops
            n /= min_ops
        min_ops += 1
    return num_ops
