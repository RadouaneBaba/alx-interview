#!/usr/bin/python3
""" Lockboxes interview question """
boxes_states = {}


def unlockBox(boxes, num, prev_key):
    """ unlock a box """
    for key in boxes[prev_key]:
        if key >= num or boxes_states.get(key):
            continue
        boxes_states[key] = True
        unlockBox(boxes, num, key)


def canUnlockAll(boxes):
    """ check if we can unlock all boxes """
    boxes_states[0] = True
    unlockBox(boxes, len(boxes), 0)
    for i in range(len(boxes)):
        if not boxes_states.get(i):
            return False
    return True
