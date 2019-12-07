class yrange:
    def __init__(self, n):
        self.i = n
        self.n = len(n)

    def __iter__(self):
        return self.i

    def prev(self):
        if self.n > 0:
            self.n -= 1

            return self.i[self.n]
        else:
            raise StopIteration()


y = yrange([1, 2, 3])
print(list(y.__iter__()))
print(y.prev())
print(y.prev())
print(y.prev())
print(y.prev())
