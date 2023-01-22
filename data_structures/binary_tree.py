class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(node: TreeNode):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def preorder(node: TreeNode):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


def postorder(node: TreeNode):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    print('Preorder:')
    preorder(tree)

    print('Inorder:')
    inorder(tree)

    print('Postorder:')
    postorder(tree)


if __name__ == '__main__':
    main()
