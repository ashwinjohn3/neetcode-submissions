class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in dirs:
                    new_r = nr + r
                    new_c = nc + c
                    if 0 <= new_r < lr and 0 <= new_c < lc and grid[new_r][new_c] == 1: 
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        fresh -= 1
            time += 1
        
        print(fresh)
        print(time)
        return -1 if fresh != 0 else time