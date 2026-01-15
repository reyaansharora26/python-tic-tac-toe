import tkinter as tk
from tkinter import messagebox

# Main Application
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Tic-Tac-Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.scores = {"X": 0, "O": 0}

        self.create_widgets()
        self.update_scoreboard()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Tic-Tac-Toe", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        title.pack(pady=10)

        # Scoreboard
        self.score_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#f0f0f0")
        self.score_label.pack(pady=5)

        # Grid Frame
        grid_frame = tk.Frame(self.root, bg="#f0f0f0")
        grid_frame.pack(pady=20)

        # Create buttons
        for i in range(9):
            btn = tk.Button(grid_frame, text="", font=("Helvetica", 32), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Reset Button
        reset_btn = tk.Button(self.root, text="Reset Game", font=("Helvetica", 14), bg="#ff4d4d", fg="white",
                              command=self.reset_game)
        reset_btn.pack(pady=10)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, disabledforeground="black")
            self.buttons[index].config(state="disabled")

            if self.check_winner():
                self.scores[self.current_player] += 1
                self.update_scoreboard()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.highlight_winner_line()
                self.disable_all_buttons()
                return
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a Tie!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Winning combinations
        win_combos = [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # columns
            [0,4,8], [2,4,6]           # diagonals
        ]
        for combo in win_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                self.winning_combo = combo
                return True
        return False

    def highlight_winner_line(self):
        for i in self.winning_combo:
            self.buttons[i].config(bg="#90ee90")  # Highlight winning buttons

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="SystemButtonFace")

    def update_scoreboard(self):
        self.score_label.config(text=f"Score - X: {self.scores['X']} | O: {self.scores['O']}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
