# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.main_list = []
        
        treeq = deque()

        if root: 
            treeq.append(root)
        else:
            return []

        self.bfs(treeq)
        return self.main_list
                

    def bfs(self, queue):
        level = 0
        while len(queue) > 0:
            level_list = []
            level += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)  
            if level_list:
                self.main_list.append(level_list)
        