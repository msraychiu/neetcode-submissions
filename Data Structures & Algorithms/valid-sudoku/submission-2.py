class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i]
            s = set()
            for j in range(len(board)):
                if row[j] != ".":
                    if row[j] in s:
                        return False
                    else:
                        s.add(row[j])

        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            
            s = set()
            for k in range(len(col)):
                if col[k] != ".":
                    if col[k] in s:
                        return False
                    else:
                        s.add(col[k])

        prevI = 0
        prevJ = 0
        for i in range(3, len(board), 3):
            for j in range(3, len(board), 3):
                grid = []
                for a in range(prevI, i):
                    for b in range(prevJ, j):
                        grid.append(board[a][b])
                s = set()
                for k in range(len(grid)):
                    if grid[k] != ".":
                        if grid[k] in s:
                            return False
                        else:
                            s.add(grid[k])
                prevJ = j
            prevI = i
            


        return True        
        
            