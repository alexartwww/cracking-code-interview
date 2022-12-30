class Node(object):

    def __init__(self, data):
        self.next = None
        self.data = data


class MyQueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        current = Node(data)
        if self.last is not None:
            self.last.next = current
        self.last = current
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            return None
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return data

    def peek(self):
        if self.first is None:
            return None
        return self.first.data

    def is_empty(self):
        return self.first is None


if __name__ == '__main__':
    simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    queue = MyQueue()
    for i in simple_list:
        queue.add(i)

    while True:
        node = queue.remove()
        if node is not None:
            print(node)
        else:
            break
