class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def is_empty(self):
        return self.top is None


def is_valid_parentheses(s):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


# Example
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))      # False