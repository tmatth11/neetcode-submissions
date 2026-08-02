class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dupe_row = defaultdict(set)
        dupe_col = defaultdict(set)
        dupe_box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                if val in dupe_row[r] or val in dupe_col[c] or val in dupe_box[(r // 3, c // 3)]:
                    return False
                
                dupe_row[r].add(val)
                dupe_col[c].add(val)
                dupe_box[(r // 3, c // 3)].add(val)
        
        return True