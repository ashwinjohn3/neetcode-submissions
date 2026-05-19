# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_index = 0
        k_value = 0
        def dfs(node):
            nonlocal current_index
            nonlocal k_value
            if not node:
                return
            dfs(node.left)
            print(current_index)
            print(node.val)
            current_index += 1
            if current_index == k:
                k_value = node.val
                
                print(k_value)
                return
            else:
                dfs(node.right)
            
        
        dfs(root)

        return k_value
