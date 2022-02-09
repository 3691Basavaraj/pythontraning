class Top:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 100:
            value = self.num
            self.num += 1

            return value
        raise StopIteration


val = Top()
for x in val:
    print(x)


