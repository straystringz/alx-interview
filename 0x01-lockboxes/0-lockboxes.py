#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1,
and each box may contain keys to the other boxes.
"""


def can_unlock_all(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists representing the boxes and their keys.
    :return: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked = [0]  # Keep track of the unlocked boxes
    for box in unlocked:
        for key in boxes[box]:
            # Check if the key corresponds to a box that hasn't been unlocked yet
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)  # Unlock the box by adding it to the unlocked list

    if len(unlocked) == len(boxes):
        return True  # All boxes have been unlocked
    return False  # Some boxes remain locked
