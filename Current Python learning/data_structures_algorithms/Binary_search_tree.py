# Date - 2023-07-23 (YYYY-MM-DD)

# ====================================================================
# Binary Search Tree
from collections import deque, defaultdict
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:

    # # Binary Search Tree Insertion
    def insert(self, node, val):
        if node is None: return Node(val)

        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node

    # # # Binary Tree Traversals
    # # In-order traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    # # Pre-order Traversal
    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # # Post-order Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")

    def levelOrder(self, node):
        if not node: return
        res = []
        queue = deque([node])
        while queue:
            lenQueue = len(queue)
            level = []
            for _ in range(lenQueue):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res

    def nonLeafNodes(self, node):
        if (not node) or (not node.left) or (not node.right): return
        if (node.left is not None) or (node.right is not None): print(node.val, end=" ")
        self.nonLeafNodes(node.left)
        self.nonLeafNodes(node.right)

    def height(self, node):
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def min_val(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def max_val(self, node):
        curr = node
        while curr and curr.right: curr = curr.right
        return curr

tree = BST()
root = Node(50)
# tree.insert(root, 50)
tree.insert(root, 30)
tree.insert(root, 20)
tree.insert(root, 40)
tree.insert(root, 70)
tree.insert(root, 60)
tree.insert(root, 80)
tree.inorder(root)
print()
print(tree.levelOrder(root))
print(tree.height(root))
tree.nonLeafNodes(root)
print()
print(tree.min_val(root).val)
print(tree.max_val(root).val)




