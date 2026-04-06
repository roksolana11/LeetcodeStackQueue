"""2 Task"""

class Node:
    """class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class Queue:
    """class Queue"""
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        """push"""
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> int:
        """pop"""
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def top(self) -> int:
        """top"""
        if not self.head:
            return None
        return self.head.data

    def empty(self) -> bool:
        """is_empty"""
        if not self.head:
            return True
        return False

class MyStack:
    """class MyStack"""
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        """push"""
        self.queue2.push(x)
        while not self.queue1.empty():
            el = self.queue1.pop()
            self.queue2.push(el)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """pop"""
        return self.queue1.pop()

    def top(self) -> int:
        """top"""
        return self.queue1.top()

    def empty(self) -> bool:
        """is_empty"""
        return self.queue1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
