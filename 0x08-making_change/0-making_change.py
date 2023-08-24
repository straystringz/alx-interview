#!/usr/bin/python3
"""Solve change problem."""


def makeChange(coins, total):
    """Givn_ a pile of coins of different values,
    determin the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1
