class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs 
        qp = deque([p])
        qq = deque([q])
        
        while qp and qq:
            for _ in range(len(qp)):
                currentq = qq.popleft()
                currentp = qp.popleft()
                if currentq is None and currentp is None: 
                    continue
                if currentq is None or currentp is None or currentq.val != currentp.val:
                    return False
                qq.append(currentq.left)
                qq.append(currentq.right)
                qp.append(currentp.left)
                qp.append(currentp.right)

        return True