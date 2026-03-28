class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Array is empty"
        val = self.arr[self.size - 1]
        self.size -= 1

        if self.size > 0 and self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return val

    def resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def display(self):
        return self.arr[:self.size]


# Example
d = DynamicArray()
d.append(10)
d.append(20)
d.append(30)
print(d.display())
print(d.pop())
print(d.display())