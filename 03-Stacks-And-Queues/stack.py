class Node(object):

    def __init__(self, data):
        self.next = None
        self.data = data


class Stack(object):
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        current = Node(data)
        current.next = self.top
        self.top = current

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


if __name__ == '__main__':
    simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stack = Stack()
    for i in simple_list:
        node = Node(i)
        stack.push(node)

    while True:
        node = stack.pop()
        if node is not None:
            print(node.data)
        else:
            break
