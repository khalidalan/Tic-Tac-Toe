import tkinter as tk  
import random  

class TicTacToe:  
    def __init__(self, master):  
        # Initialize the main window and game variables  
        self.master = master  
        self.master.title("Tic-Tac-Toe")  # Set the window title  
        self.board = [" " for _ in range(9)]  # Create a 3x3 board  
        self.player_score = 0  # Player score  
        self.computer_score = 0  # Computer score  
        self.create_widgets()  # Create the game interface  
        self.update_score()  # Display initial scores  

    def create_widgets(self):  
        # Create buttons for the game board and score label  
        self.buttons = []  
        for i in range(9):  
            button = tk.Button(self.master, text=" ", font=('Arial', 20), width=5, height=2,  
                               command=lambda i=i: self.player_move(i))  # Bind button to player_move  
            button.grid(row=i // 3, column=i % 3)  # Arrange buttons in a grid  
            self.buttons.append(button)  # Add button to the list  

        # Create and position the score label  
        self.score_label = tk.Label(self.master, text=f"You: {self.player_score} Computer: {self.computer_score}")  
        self.score_label.grid(row=3, column=0, columnspan=3)  # Position the score label  
        
        # Create and position the restart button  
        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart)  
        self.restart_button.grid(row=4, column=0, columnspan=3)  # Position the restart button  

    def player_move(self, index):  
        # Handle player's move  
        if self.board[index] == " ":  # Check if the cell is empty  
            self.board[index] = 'X'  # Mark the cell with 'X'  
            self.buttons[index].config(text='X')  # Update button text  
            if self.check_winner('X'):  # Check if the player has won  
                self.player_score += 1  # Increment player score  
                self.show_winner("X wins!", 'white')  # Show winning message  
                return  
            elif " " not in self.board:  # Check for tie  
                self.show_winner("Tie, No Winner!", 'red')  # Show tie message  
                self.highlight_draw()  # Highlight the draw condition  
                return  
            self.computer_move()  # Let the computer make a move  

    def computer_move(self):  
        # Handle computer's move  
        index = self.best_move()  # Get the best move  
        if index is not None:  
            self.board[index] = 'O'  # Mark the cell with 'O'  
            self.buttons[index].config(text='O')  # Update button text  
            if self.check_winner('O'):  # Check if the computer has won  
                self.computer_score += 1  # Increment computer score  
                self.show_winner("O wins!", 'white')  # Show winning message  
            elif " " not in self.board:  # Check for tie  
                self.show_winner("Tie, No Winner!", 'red')  # Show tie message  
                self.highlight_draw()  # Highlight the draw condition  

    def best_move(self):  
        # Simple AI to choose the best move  
        for i in range(9):  
            # Check if computer can win  
            if self.board[i] == " ":  
                self.board[i] = 'O'  
                if self.check_winner('O'):  
                    self.board[i] = " "  
                    return i  
                self.board[i] = " "  

        for i in range(9):  
            # Check if player can win, block it  
            if self.board[i] == " ":  
                self.board[i] = 'X'  
                if self.check_winner('X'):  
                    self.board[i] = " "  
                    return i  
                self.board[i] = " "  

        # If no immediate win/block, pick a random empty spot  
        empty_indices = [i for i, x in enumerate(self.board) if x == " "]  
        if empty_indices:  
            return random.choice(empty_indices)  
        return None  

    def check_winner(self, player):  
    # Reset colors of all buttons  
        for button in self.buttons:  
            button.config(bg='SystemButtonFace')  # Reset to default color  

        # Define winning conditions  
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows  
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns  
                        (0, 4, 8), (2, 4, 6)]  # Diagonals  

        # Color setup  
        color_mapping = {'X': 'lightgreen', 'O': 'lightblue'}  # Different colors for X and O  

        for condition in win_conditions:  
            if all(self.board[i] == player for i in condition):  # Check winning condition  
                for i in condition:  
                    self.buttons[i].config(bg=color_mapping[player])  # Change color of winning cells  
                return True  # Return True if player wins  
                
        return False  # Return False if no winner
    def highlight_draw(self):  
        # Highlight all buttons in red if drawer occurs  
        for button in self.buttons:  
            button.config(bg='red')  # Change button background to red  

    def show_winner(self, message, color):  
        # Display the winner or tie message  
        self.score_label.config(text=message, bg=color)  # Update score label with message and color  
        for button in self.buttons:  
            button.config(state='disabled')  # Disable buttons after game ends  

    def restart(self):  
        # Reset the game  
        self.board = [" " for _ in range(9)]  # Clear the board  
        for button in self.buttons:  
            button.config(text=' ', state='normal', bg='SystemButtonFace')  # Reset button text and state  
        self.score_label.config(text=f"You: {self.player_score} Computer: {self.computer_score}", bg='SystemButtonFace')  # Reset score label  

    def update_score(self):  
        # Update the score label  
        self.score_label.config(text=f"You: {self.player_score} Computer: {self.computer_score}")  

if __name__ == "__main__":  
    root = tk.Tk()  # Create the main window  
    game = TicTacToe(root)  # Start the game  
    root.mainloop()  # Run the application