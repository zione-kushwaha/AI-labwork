import tkinter as tk
from tkinter import messagebox
from queue import Queue

class Puzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Solver")
        self.board = [[0, 1, 2], [3, 4, 5], [7, 8, 6]]  # Initial board state
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]   # Goal state
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        # Adding the search algorithm selection
        self.algorithm = tk.StringVar(value="BFS")  # Default algorithm is BFS
        self.algorithm_menu = tk.OptionMenu(root, self.algorithm, "BFS", "DFS", "A*")
        self.algorithm_menu.grid(row=3, column=0, columnspan=3)

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.grid(row=4, column=0, columnspan=3)

        self.moves_label = tk.Label(root, text="Moves: ", font=('Arial', 12))
        self.moves_label.grid(row=5, column=0, columnspan=3)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=str(self.board[i][j]), font=('Arial', 24), width=4, height=2)
                self.buttons[i][j].grid(row=i, column=j)
        self.update_board()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                text = str(self.board[i][j]) if self.board[i][j] != 0 else ""
                self.buttons[i][j].config(text=text)
                

    def solve(self):
        # Get the selected algorithm
        algorithm = self.algorithm.get()
        solution, moves = None, []

        # Run the selected search algorithm
        if algorithm == "BFS":
            solution, moves = self.bfs(self.board)
        elif algorithm == "DFS":
            solution, moves = self.dfs(self.board)
        elif algorithm == "A*":
            solution, moves = self.a_star(self.board)

        # Display solution or error
        if solution:
            self.animate_solution(solution, moves)
            self.moves_label.config(text="Moves: " + " -> ".join(moves))  # Display moves in the label
            messagebox.showinfo("Solved", "Puzzle Solved!")
        else:
            messagebox.showerror("Error", "No solution found!")

    def animate_solution(self, solution, moves):
        # Animate the moves one by one
        for step, move in zip(solution, moves):
            self.board = step
            self.update_board()
            self.root.update()
            self.root.after(500)  # Delay for visualization of moves
            print(move)  # Printing the move in the console
        # Ensure the last move is displayed
        self.update_board()
        self.root.update()

    def bfs(self, start):
        # Perform BFS to solve the puzzle
        def is_goal(state):
            return state == self.goal

        def get_neighbors(state):
            neighbors = []
            moves = []
            x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            direction_names = ["Up", "Down", "Left", "Right"]
            for (dx, dy), direction in zip(directions, direction_names):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 3:
                    new_state = [row[:] for row in state]
                    new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                    neighbors.append(new_state)
                    moves.append(f"Move {new_state[x][y]} {direction}")
            return neighbors, moves

        queue = Queue()
        queue.put((start, [], []))
        visited = set()
        visited.add(tuple(tuple(row) for row in start))

        while not queue.empty():
            current, path, moves = queue.get()
            if is_goal(current):
                return path + [current], moves
            neighbors, new_moves = get_neighbors(current)
            for neighbor, move in zip(neighbors, new_moves):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)
                    queue.put((neighbor, path + [current], moves + [move]))
        return None, None

    def dfs(self, start):
        # Perform DFS to solve the puzzle
        def is_goal(state):
            return state == self.goal

        def get_neighbors(state):
            neighbors = []
            moves = []
            x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            direction_names = ["Up", "Down", "Left", "Right"]
            for (dx, dy), direction in zip(directions, direction_names):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 3:
                    new_state = [row[:] for row in state]
                    new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                    neighbors.append(new_state)
                    moves.append(f"Move {new_state[x][y]} {direction}")
            return neighbors, moves

        stack = [(start, [], [])]
        visited = set()
        visited.add(tuple(tuple(row) for row in start))

        while stack:
            current, path, moves = stack.pop()
            if is_goal(current):
                return path + [current], moves
            neighbors, new_moves = get_neighbors(current)
            for neighbor, move in zip(neighbors, new_moves):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)
                    stack.append((neighbor, path + [current], moves + [move]))
        return None, None

    def a_star(self, start):
        # A* algorithm can be implemented here if needed, or another search heuristic
        pass

if __name__ == "__main__":
    root = tk.Tk()
    puzzle = Puzzle(root)
    root.mainloop()