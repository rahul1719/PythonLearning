class Linear:

    def search(self):
        arr = [1, 2, 3, 49, 99, 4, 6, 17, 10]
        key = 11
        for i in range(len(arr)):
            if arr[i] == key:
                return i
        return -1


linear = Linear()
result = linear.search()
if result != -1:
    print("Key present at index %d " % result)
else:
    print("Key not found")
