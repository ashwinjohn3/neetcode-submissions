# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # When we are at a node: 
        # 1. Whats the maximum of the right 
        # 2. Check the maximum of the left 
        # 3. Calculate the max(maxValue, root + maxLeft + maxRight)
        max_val = root.val

        def maxDownwardPathDfs(root):
            nonlocal max_val
            if not root: 
                return 0
            # postorder traversal
            left_max = max(maxDownwardPathDfs(root.left), 0)
            right_max = max(maxDownwardPathDfs(root.right), 0) 

            max_val = max(max_val, root.val + left_max + right_max)
            return root.val + max(left_max, right_max)

        maxDownwardPathDfs(root)

        return max_val