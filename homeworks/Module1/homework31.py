class EvenNumbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __iter__(self):
        return self
    def __next__(self):
        if self.x + 1 >= self.y:
            raise StopIteration()
        self.x += 2
        return self.x
en = EvenNumbers(10, 27)
for i in en:
    print(i)