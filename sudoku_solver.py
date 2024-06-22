class Board:
    def __init__(self, board):
        self.board = board
        # Precompute row, column, and square sets for quick lookups
        self.rows = [set(row) for row in board]
        self.cols = [set(col) for col in zip(*board)]
        self.squares = [
            set(
                board[r + i][c + j]
                for i in range(3) for j in range(3)
            )
            for r in (0, 3, 6) for c in (0, 3, 6)
        ]

    def __str__(self):
        board_str = ''
        for row in self.board:
            # Replace 0 with '*' for display purposes
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str) + '\n'
        return board_str

    def find_empty_cell(self):
        # Locate the first empty cell (marked by 0)
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        # Check if the number is not present in the specified row
        return num not in self.rows[row]

    def valid_in_col(self, col, num):
        # Check if the number is not present in the specified column
        return num not in self.cols[col]

    def valid_in_square(self, row, col, num):
        # Check if the number is not present in the 3x3 sub-grid
        square_index = (row // 3) * 3 + col // 3
        return num not in self.squares[square_index]

    def is_valid(self, empty, num):
        # Check if the number can be placed at the empty cell
        row, col = empty
        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_square(row, col, num)
        )

    def place_number(self, row, col, num):
        # Place the number on the board and update the sets
        self.board[row][col] = num
        self.rows[row].add(num)
        self.cols[col].add(num)
        square_index = (row // 3) * 3 + col // 3
        self.squares[square_index].add(num)

    def remove_number(self, row, col, num):
        # Remove the number from the board and update the sets
        self.board[row][col] = 0
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        square_index = (row // 3) * 3 + col // 3
        self.squares[square_index].remove(num)

    def solver(self):
        # Solve the Sudoku puzzle using backtracking
        if (next_empty := self.find_empty_cell()) is None:
            return True
        row, col = next_empty
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                self.place_number(row, col, guess)
                if self.solver():
                    return True
                # Reset the cell if the guess doesn't lead to a solution
                self.remove_number(row, col, guess)
        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

if __name__ == '__main__':
    # Solve the provided Sudoku puzzle
    solve_sudoku(puzzle)
