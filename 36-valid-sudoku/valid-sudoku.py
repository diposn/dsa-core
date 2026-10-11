class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # track numbers seen in each rows, cols and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        # go through each colum and row
        for row in range(9):
            for col in range(9):
                
                # get the number at current row and column
                number = board[row][col]
                
                # if cell empty skip
                if number == ".":
                    continue

                #find which 3x3 box number belongs to
                box_i = (row // 3) * 3 + (col // 3)

                #check if number is in row, col or box
                if (number in rows[row] or
                    number in cols[col] or
                    number in box[box_i]):
                    return False

                rows[row].add(number)
                cols[col].add(number)
                box[box_i].add(number)
        return True
