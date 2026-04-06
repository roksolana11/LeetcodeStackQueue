"""3 Task"""
from collections import deque

class Node:
    """class Node"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    """class Stack"""
    def __init__(self):
        self.top = None

    def push(self, val):
        """push"""
        node = Node(val, self.top)
        self.top = node

    def pop(self):
        """pop"""
        if not self.top:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        """peek"""
        if not self.top:
            return None
        return self.top.val

    def empty(self):
        """is_empty"""
        return self.top is None

    def count_val(self, val):
        """frequency of val"""
        count = 0
        curr = self.top
        while curr:
            if curr.val == val:
                count += 1
            curr = curr.next
        return count

class FreqStack:
    """FreqStack"""
    def __init__(self):
        self.group_stacks = deque()

    def _get_freq(self, val):
        """frequency in stack"""
        return sum(s.count_val(val) for s in self.group_stacks)

    def push(self, val: int) -> None:
        """push"""
        freq = self._get_freq(val) + 1
        while freq > len(self.group_stacks):
            self.group_stacks.append(Stack())
        self.group_stacks[freq - 1].push(val)

    def pop(self) -> int:
        """pop"""
        top_stack = self.group_stacks[-1]
        val = top_stack.pop()
        if top_stack.empty():
            self.group_stacks.pop()
        return val
