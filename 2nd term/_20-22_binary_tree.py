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

    def remove(self, removing_key, previous=None, start='start'):
        if start == 'start':
            start = self.root
        if start is None:
            return
        if removing_key > start.key:
            self.remove(removing_key, (start, 1), start.right)
        elif removing_key < start.key:
            self.remove(removing_key, (start, -1), start.left)
        else:
            if start.left is None and start.right is None:
                if previous is None:
                    start = None
                else:
                    if previous[1] == 1:
                        previous[0].right = None
                    else:
                        previous[0].left = None
            elif start.left is None:
                if previous[1] == 1:
                    previous[0].right = start.right
                else:
                    previous[0].left = start.right
            elif start.right is None:
                if previous[1] == 1:
                    previous[0].right = start.left
                else:
                    previous[0].left = start.left
            else:
                if start.right.left is None:
                    start.right.left = start.left
                    if previous[1] == 1:
                        previous[0].right = start.right
                    else:
                        previous[0].left = start.right
                else:
                    current = start.right
                    while current:
                        answ = current
                        current = current.left
                    start.key = answ.key
                    start.value = answ.value
                    self.remove(answ.key, previous=(start, 1), start=start.right)









# T = Tree()
# T.add((0 , 15))
# T.add((12 , 25))
# T.add((7 , 45))
# T.add((-20 , None))
# T.add((17, 'tree'))
# T.print()
# print('sep')
# T.remove(0)
# T.print()
# print('sep')
# T.remove(12)
# T.print()
# print('sep')
# print(T.find(17))
# print(T.find(-20))
# print(T.find(12))
# print(T.find(222))
# print(T.find(7))
my = Tree()
for i in [(4, 0), (435, 0), (2, 0), (35, 0), (23, 0), (454, 0), (435345, 0), (1, 0)]:
    my.add(i)
my.remove(2)
my.print()