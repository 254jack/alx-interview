#!/usr/bin/python3
"""
 Unlocked boxes
"""


def canUnlockAll(boxes):
    """
        Look when the box is unlocked
        Return true if is unlocked or false
    """

    unlocked_box = [0]
    for i in unlocked_box:
        for j in boxes[i]:
            if j < len(boxes):
                if j not in unlocked_box:
                    unlocked_box.append(j)

    if len(boxes) == len(unlocked_box):
        return True
    else:
        return False
