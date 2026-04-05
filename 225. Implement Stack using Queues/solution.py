class Queue:
    """class Queue"""
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        """push"""
        self.data.append(x)

    def pop(self) -> int:
        """pop"""
        return self.data.pop(0)

    def top(self) -> int:
        """top"""
        return self.data[0]

    def empty(self) -> bool:
        """is_empty"""
        if not self.data:
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
