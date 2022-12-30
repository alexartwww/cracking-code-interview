class Node(object):

    def __init__(self, data):
        self.parent = None
        self.children = set()
        self.data = data

    def append(self, node):
        node.parent = self
        self.children.add(node)
        return self

def view_tree(node, level, last):
    if not last:
        print((" ┣━" * level), node.data)
    else:
        print((" ┣━" * (level-1)) + " ┗━", node.data)
    for i, n in enumerate(node.children):
        view_tree(n, level + 1, i == len(node.children) - 1)

if __name__ == '__main__':
    root = Node(8)
    node1 = Node(1)
    node2 = Node(2)
    node4 = Node(4)
    node4.append(node1)
    node4.append(node2)
    root.append(node4)
    node6 = Node(6)
    root.append(node6)
    node20 = Node(20)
    node10 = Node(10)
    node10.append(node20)
    root.append(node10)
    view_tree(root, 0, False)
