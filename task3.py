class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)

# Створення дерева:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Знаходження суми всіх значень:
print("Сумма всіх значень у дереві", tree_sum(root))