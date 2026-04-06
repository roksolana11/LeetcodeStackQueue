"""3 Task"""

class Node:
    """class Node"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class LinkedList:
    """class LinkedList"""
    def __init__(self):
        self.head = None

    def push(self, val):
        """push"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """pop"""
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def empty(self):
        """is_empty"""
        if self.head is None:
            return True
        return False

class FreqStack:
    """class FreqStack"""
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.maxfreq = 0

    def push(self, val: int) -> None:
        """push"""
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        self.maxfreq = max(self.maxfreq, f)

        if f not in self.groups:
            self.groups[f] = LinkedList()
        self.groups[f].push(val)

    def pop(self) -> int:
        """pop"""
        val = self.groups[self.maxfreq].pop()
        self.freq[val] -= 1

        if self.groups[self.maxfreq].empty():
            self.maxfreq -= 1
        return val
