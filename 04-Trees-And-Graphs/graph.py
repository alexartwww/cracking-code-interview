class Node(object):

    def __init__(self, data):
        self.links = set()
        self.data = data

class Visited(object):
    def __init__(self):
        self.objects = set()

    def add(self, object):
        self.objects.add(object)

    def check(self, object):
        return object in self.objects

class MyQueueNode(object):

    def __init__(self, data):
        self.next = None
        self.data = data

class MyQueue(object):
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data):
        current = MyQueueNode(data)
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


def search_depth(node, level):
    if visited.check(node):
        return
    visited.add(node)
    print(" " * level, "Узел", node.data)
    for child in node.links:
        search_depth(child, level+1)


def search_wide(node):
    queue = MyQueue()
    queue.add(node)
    while not queue.is_empty():
        r = queue.remove()
        print("Узел", r.data)
        visited.add(r)
        for n in r.links:
            if not visited.check(n):
                visited.add(n)
                queue.add(n)


if __name__ == '__main__':
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    root.links.add(node1)
    root.links.add(node4)
    root.links.add(node5)

    node1.links.add(node3)
    node1.links.add(node4)

    node2.links.add(node1)

    node3.links.add(node4)
    node3.links.add(node2)

    visited = Visited()
    search_depth(root, 0)
    visited = Visited()
    search_wide(root)
