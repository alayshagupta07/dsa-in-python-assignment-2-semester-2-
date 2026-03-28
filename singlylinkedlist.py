class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # For efficient insert at end

    def insert_at_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        print(f"Inserted {value} at beginning")
        self.traverse()

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        print(f"Inserted {value} at end")
        self.traverse()

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return

        # Case 1: Delete head
        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:   # List became empty
                self.tail = None
            print(f"Deleted {value} (was head)")
            self.traverse()
            return

        # Case 2: Delete middle or tail
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next

                # If deleting tail
                if curr == self.tail:
                    self.tail = prev

                print(f"Deleted {value}")
                self.traverse()
                return

            prev = curr
            curr = curr.next

        # Value not found
        print(f"Value {value} not found")
        self.traverse()

    def traverse(self):
        if self.head is None:
            print("List: Empty\n")
            return

        temp = self.head
        result = []

        while temp:
            result.append(str(temp.data))
            temp = temp.next

        print("List:", " -> ".join(result), "\n")


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    sll = SinglyLinkedList()

    operations = [
        "insert_begin 10",
        "insert_end 20",
        "insert_end 30",
        "insert_begin 5",
        "delete 20",
        "delete 5",
        "delete 30",
        "delete 100"
    ]

    for op in operations:
        parts = op.split()

        if parts[0] == "insert_begin":
            sll.insert_at_beginning(int(parts[1]))

        elif parts[0] == "insert_end":
            sll.insert_at_end(int(parts[1]))

        elif parts[0] == "delete":
            sll.delete_by_value(int(parts[1]))