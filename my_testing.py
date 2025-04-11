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


n0: Node = Node(80, None)
n1: Node = Node(50, n0)
n2: Node = Node(70, n1)
n3: Node = Node(90, n1)
n4: Node = Node(100, n3)
n5: Node = Node(110, n4)


def last(head: Node) -> int:
    if head.next is None:
        return head.value

    else:
        return last(head.next)


print("my value is " + str(last(n5)) + "!")
