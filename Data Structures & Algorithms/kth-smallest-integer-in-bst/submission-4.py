# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_value = 0
        current_k = 0
        def dfs(root): 
            nonlocal current_k
            nonlocal k_value
            if not root:
                return
            
            dfs(root.left)
            current_k += 1
            if k == current_k: 
                k_value = root.val
            dfs(root.right)
            return 
        
        dfs(root)
        return k_value