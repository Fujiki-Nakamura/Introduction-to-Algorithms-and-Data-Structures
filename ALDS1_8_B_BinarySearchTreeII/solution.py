class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.list = []

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < y.key:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:  # node.key >= y.key
            y.right = node

    def find(self, key):
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < y.key:
                x = x.left
            elif key > y.key:
                x = x.right
            else:  # key == y.key
                return True

        return False

    def inorder(self, node):
        if node is None:
            return  # noqa
        self.inorder(node.left)
        self.list.append(node.key)
        self.inorder(node.right)
        return self.list

    def preorder(self, node):
        if node is None:
            return  # noqa
        self.list.append(node.key)
        self.preorder(node.left)
        self.preorder(node.right)
        return self.list


if __name__ == '__main__':
    tree = Tree()

    m = int(input())
    results = []
    for _ in range(m):
        order, *k = input().split()
        if order.startswith('insert'):
            node = Node(int(k.pop(0)))
            tree.insert(node)
        elif order.startswith('find'):
            k = int(k.pop(0))
            is_found = tree.find(k)
            if is_found:
                results.append('yes')
            else:
                results.append('no')
        elif order.startswith('print'):
            tree.list = []
            inordered = tree.inorder(tree.root)
            results.append(inordered)
            tree.list = []
            preordered = tree.preorder(tree.root)
            results.append(preordered)
    for result in results:
        if isinstance(result, str):
            print(result)
        elif isinstance(result, list):
            print(' ' + ' '.join(map(str, result)))
