class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after(self, target, value):
        if self.head is None:
            print("List is empty. Cannot insert.")
            return

        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(value)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:  # middle case
                    temp.next.prev = new_node
                else:  # inserting after tail
                    self.tail = new_node

                temp.next = new_node

                print(f"Inserted {value} after {target}")
                self.traverse()
                return

            temp = temp.next

        print(f"Target {target} not found")
        self.traverse()

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return

        if pos <= 0:
            print("Invalid position")
            return

        temp = self.head
        count = 1

        # Case 1: Delete head
        if pos == 1:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            print(f"Deleted node at position {pos} (head)")
            self.traverse()
            return

        # Traverse to position
        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            self.traverse()
            return

        # Case 2: Delete middle or tail
        if temp.next:
            temp.next.prev = temp.prev
        else:
            self.tail = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

        print(f"Deleted node at position {pos}")
        self.traverse()

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("List: Empty\n")
            return

        temp = self.head
        result = []

        while temp:
            result.append(str(temp.data))
            temp = temp.next

        print("List:", " <-> ".join(result), "\n")


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Initial list
    for val in [10, 20, 30, 40]:
        dll.append(val)

    print("Initial List:")
    dll.traverse()

    operations = [
        ("insert_after", 20, 25),
        ("insert_after", 40, 50),
        ("delete_pos", 1),
        ("delete_pos", 3),
        ("delete_pos", 10)
    ]

    for op in operations:
        if op[0] == "insert_after":
            dll.insert_after(op[1], op[2])

        elif op[0] == "delete_pos":
            dll.delete_at_position(op[1])