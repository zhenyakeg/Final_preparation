class Node():

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Tree():

    def __init__(self, root=None):
        self.root = root

    def add(self, vertex, start='start'):
        if start == 'start':
            start = self.root
        if start is None:
            self.root = Node(vertex[0], vertex[1])
            return
        if vertex[0] > start.key:
            if start.right is None:
                start.right = Node(vertex[0], vertex[1])
                return
            self.add(vertex, start.right)
        elif vertex[0] < start.key:
            if start.left is None:
                start.left = Node(vertex[0], vertex[1])
                return
            self.add(vertex, start.left)
        else:
            return

    def print(self, start='start'):
        if start == 'start':
            start = self.root
        if start is None:
            return
        self.print(start.left)
        print(str(start.key), str(start.value))
        self.print(start.right)

    def find(self, key, start='start'):
        if start == 'start':
            start = self.root
        if start is None:
            return
        if key > start.key:
            return self.find(key, start.right)
        elif key < start.key:
            return self.find(key, start.left)
        else:
            return start.key, start.value


T = Tree()
T.add((0 , 15))
T.add((12 , 25))
T.add((7 , 45))
T.add((-20 , None))
T.add((17, 'tree'))
T.print()
print(T.find(17))
print(T.find(-20))
print(T.find(12))
print(T.find(222))
print(T.find(7))