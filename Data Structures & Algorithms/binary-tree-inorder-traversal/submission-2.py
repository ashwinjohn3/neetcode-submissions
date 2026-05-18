# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_arr = []
        
        def inorder_atomic(root: Optional[TreeNode]): 
            if not root:
                return
            inorder_atomic(root.left)
            result_arr.append(root.val)
            inorder_atomic(root.right)
        
        inorder_atomic(root)

        return result_arr

    

        
        


        
        