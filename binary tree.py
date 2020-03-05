class Node():
    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, node=None):
        self.root = node

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        else:
            queue = [self.root]
            while True:
                checked_node = queue.pop(0)
                if checked_node.left is None:
                    checked_node.left = node
                    break
                else:
                    queue.append(checked_node.left)
                    if checked_node.right is None:
                        checked_node.right = node
                        break
                    else:
                        queue.append(checked_node.right)

    def travel(self):
        if self.root is None:
            print("empty tree")
            return
        else:
            queue = [self.root]
            while queue:
                checked_node = queue.pop(0)
                print(checked_node.item)
                if checked_node.left is not None:
                    queue.append(checked_node.left)
                if checked_node.right is not None:
                    queue.append(checked_node.right)

    def preorder(self, rooter):
        if rooter is None:
            return
        else:
            print(rooter.item)
            self.preorder(rooter.left)
            self.preorder(rooter.right)

    def inorder(self, rooter):
        if rooter is None:
            return
        self.inorder(rooter.left)
        print(rooter.item)
        self.inorder(rooter.right)

    def postorder(self, rooter):
        if rooter is None:
            return
        self.postorder(rooter.left)
        self.postorder(rooter.right)
        print(rooter.item)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    '''
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
        0
       / \
      1   2
      / \
      3  4
    '''
    # tree.travel()
    # tree.preorder(tree.root)
    tree.inorder(tree.root)

