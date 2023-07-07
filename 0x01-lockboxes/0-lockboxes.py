#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1,
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists representing the boxes and their keys.
    :return: True if all boxes can be opened, False otherwise.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]  
    for box in unlocked:
        for key in boxes[box]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key) 

    if len(unlocked) == len(boxes):
        return True 
    return False  
