import tkinter as tk

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.entries = [[tk.Entry(master, width=3) for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)
        
        solve_button = tk.Button(master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, columnspan=9)

    def solve_sudoku(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                if value.isdigit() and 1 <= int(value) <= 9:
                    grid[i][j] = int(value)
                else:
                    grid[i][j] = 0
        
        if self.solve(grid):
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(grid[i][j]))
        else:
            print("No solution found")

    def solve(self, grid):
        find = self.find_empty(grid)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve(grid):
                    return True
                grid[row][col] = 0

        return False

    def find_empty(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()