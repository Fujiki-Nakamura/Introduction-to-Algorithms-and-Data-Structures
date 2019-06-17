class Node:
    def __init__(self, key=-1, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class Tree:
    def __init__(self, ):
        self.root = None
        self.node_list = []

    def insert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < y.key:
                x = x.left
            else:  # node.key >= y.key
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    def inorder(self, node):
        if node is None: return  # noqa
        self.inorder(node.left)
        self.node_list.append(node.key)
        self.inorder(node.right)
        return self.node_list

    def preorder(self, node):
        if node is None: return # noqa
        self.node_list.append(node.key)
        self.preorder(node.left)
        self.preorder(node.right)
        return self.node_list


if __name__ == '__main__':
    tree = Tree()
    m = int(input())
    for _ in range(m):
        order, *k = input().split()
        if order.startswith('insert'):
            k = int(k.pop())
            node = Node(key=k)
            tree.insert(node)
        elif order.startswith('print'):
            tree.node_list = []
            node_list = tree.inorder(tree.root)
            print(' ' + ' '.join(map(str, node_list)))
            tree.node_list = []
            node_list = tree.preorder(tree.root)
            print(' ' + ' '.join(map(str, node_list)))
