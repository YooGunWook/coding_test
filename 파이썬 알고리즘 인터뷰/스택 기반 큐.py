class Myqueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        if self.input and self.output:
            return False
        elif not self.input and not self.output:
            return True


if __name__ == "__main__":
    print(6 % 5)

