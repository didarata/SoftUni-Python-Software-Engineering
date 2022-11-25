class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.operation = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.operation == self.count - 1:
            raise StopIteration

        self.operation += 1

        return self.operation * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)