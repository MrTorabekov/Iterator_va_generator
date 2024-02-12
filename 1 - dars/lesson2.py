class PowTwo:
    def __init__(self, limit=0):
        self.limit = limit

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.limit:
            pow_number = 2 ** self.n
            self.n += 1
            return pow_number
        else:
            raise StopIteration


numbers = PowTwo(5)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))