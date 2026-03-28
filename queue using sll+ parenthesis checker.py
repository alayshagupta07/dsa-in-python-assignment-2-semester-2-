class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Queue is empty"
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print(q.dequeue())
q.display()