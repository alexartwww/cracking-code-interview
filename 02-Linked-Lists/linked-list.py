class Node(object):

    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        self.get_tail().next = Node(data)

    def get_tail(self):
        current = self

        while current.next is not None:
            current = current.next

        return current


def delete_node(head, data):
    current = head

    # искомый - первый
    if current.data == data:
        return current.next

    while current.next is not None:
        # найдено, удалил, вышел
        if current.next.data == data:
            current.next = current.next.next
            return head
        current = current.next
    # не найдено
    return head


def node_to_list(head):
    result = []
    current = head
    result.append(current.data)
    while current.next is not None:
        current = current.next
        result.append(current.data)
    return result


def list_to_node(datas):
    head = None
    for i in datas:
        if head is None:
            head = Node(i)
        else:
            head.append_to_tail(i)
    return head


def get_n_node(head, n):
    current = head
    i = 0
    while current.next is not None:
        if i == n:
            return current
        current = current.next
        i += 1
    return None


if __name__ == '__main__':
    simple_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    head = None
    for i in simple_list:
        if head is None:
            head = Node(i)
        else:
            head.append_to_tail(i)

    a = node_to_list(head)[-5]
    print(a.data)
