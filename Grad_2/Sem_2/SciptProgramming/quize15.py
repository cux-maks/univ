# 1
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# 2
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

if __name__ == '__main__':
    # 1
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

    # 2
    for n in frange(0, 4, 0.5):
        print(n)

    list(frange(0, 1, 0.125))
