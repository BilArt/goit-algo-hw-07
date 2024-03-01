class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min(root):
    if root is None:
        return float('inf')
    min_val = root.value
    left_min = find_min(root.left)
    right_min = find_min(root.right)
    return min(min_val, left_min, right_min)

# Створення дерева:
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

# Пошук найменшого значення
print("Найменше значення у дереві:", find_min(root))
