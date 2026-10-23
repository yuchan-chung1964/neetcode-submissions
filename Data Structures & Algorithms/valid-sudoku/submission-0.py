class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val == '.':
                    continue
                key = (i - i % 3, j - j % 3)
                if val in columns[j] or val in rows[i] or val in boxes[key]:
                    return False
                boxes[key].add(val)
                columns[j].add(val)
                rows[i].add(val)
        return True