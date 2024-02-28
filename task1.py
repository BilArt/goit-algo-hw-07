class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return float('-inf')
    max_val = root.value
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(max_val, left_max, right_max)

# Створення дерева:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Пошук найбільшого значення
print("Найбільше значення у дереві:", find_max(root))
