"""1 Task"""
class Stack:
    """class Stack"""
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        """push"""
        self.data.append(x)

    def pop(self) -> int:
        """pop"""
        return self.data.pop()

    def peek(self) -> int:
        """peek"""
        return self.data[-1]

    def empty(self) -> bool:
        """is_empty"""
        if not self.data:
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
