# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        start_index = 1
        small_map = {}
        def dfs(node):
            nonlocal start_index
            if not node:
                return
            dfs(node.left)
            small_map[start_index] = node.val
            start_index += 1
            dfs(node.right)
        
        dfs(root)

        return small_map[k]
