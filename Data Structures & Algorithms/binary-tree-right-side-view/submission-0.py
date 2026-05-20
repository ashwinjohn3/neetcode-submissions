# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        self.right_side_view = []
        self.level_index = 0 
        if not root: 
            return []
        else:
            queue.append(root)
        self.bfs(queue)
        return self.right_side_view

    
    def bfs(self, queue):
        while queue:
            rightSide = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    rightSide = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if rightSide: 
                self.right_side_view.append(rightSide.val)
        