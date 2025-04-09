from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


def sum(head: Node | None) -> int:
    """sum all values of nodes in linked list"""
    if head is None:  # is refers to objects/class
        return 0

    else:
        rest: int = sum(head.next)
        return head.value + rest
