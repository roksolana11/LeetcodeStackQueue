"""1 Task"""

class Node:
    """class Node"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class Stack:
    """class Stack"""
    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        """push"""
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        """pop"""
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self) -> int:
        """peek"""
        if not self.head:
            return None
        return self.head.data

    def empty(self) -> bool:
        """is_empty"""
        if not self.head:
            return True
        return False

class MyQueue:
    """class MyQueue"""
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x: int) -> None:
        """push"""
        self.stack_in.push(x)

    def pop(self) -> int:
        """pop"""
        if self.stack_out.empty():
            while not self.stack_in.empty():
                elem = self.stack_in.pop()
                self.stack_out.push(elem)
        if not self.stack_out.empty():
            return self.stack_out.pop()

    def peek(self) -> int:
        """peek"""
        if self.stack_out.empty():
            while not self.stack_in.empty():
                elem = self.stack_in.pop()
                self.stack_out.push(elem)
        if not self.stack_out.empty():
            return self.stack_out.peek()

    def empty(self) -> bool:
        """is_empty"""
        if self.stack_out.empty() and self.stack_in.empty():
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
