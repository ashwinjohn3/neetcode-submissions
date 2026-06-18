class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if board[i][j] == '.':
                    continue
                elif val in row[i] or val in cols[j] or val in squares[(i//3, j//3)]:
                    return False
                else:
                    row[i].add(val)
                    cols[j].add(val)
                    squares[(i//3, j//3)].add(val)
        return True

