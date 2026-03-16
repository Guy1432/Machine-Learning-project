import random
import math
import json
import tictactoe_constants

from tictactoe_constants import SCORE_CONSTANTS, GAMMA


class Game:
    """
    This class implements the Tic-Tac-Toe (XO) game using a Monte Carlo approach.
    - Each board state receives a score based on the final game result.
    - Scores are taken from SCORE_CONSTANTS (winner_id → score).
    - The agent plays as 'X' and always moves first.
    - The rival plays as 'O' and chooses moves randomly.
    - Scores for earlier board states are reduced using the discount factor gamma.
    """
    
    def __init__(self, plan):
        # Initialize the board and available cells
        # 0: Empty, 1: X (agent), -1: O (rival)
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.available_cells = []
        for i in range(3):
            for j in range(3):
                self.available_cells.append((i, j))
        self.agent_turn = True
        self.boards_states = []
        self.boards_states_scores = []
        self.score_constants = SCORE_CONSTANTS
        self.gamma = GAMMA
        self.plan = plan

    def play(self):

        # Perform a move
        player = -1
        position = 1
        if self.agent_turn:
            player = 1
            position = 0
        if self.plan[position] == 'simple_heuristic':
            self.perform_simple_heuristic_move(player)
        elif self.plan[position] == 'complex_heuristic':
            self.perform_complex_huristic_move(player)
        elif self.plan[position] == 'minimax':
            self.perform_minimax_move(player)
        elif self.plan[position] == 'smart_agent_dict':
            self.perform_smart_agent_move_dict(player)
        elif self.plan[position] == 'smart_agent_cnn':
            self.perform_smart_agent_move_cnn(player)
        else: #random plan 
            self.perform_random_move(player)

        self.boards_states.append(self.array_to_string())

        # Switch turns
        self.agent_turn = not self.agent_turn
    
    

    def perform_random_move(self, player):
        # Make one random move for the given player.
        # player = 1 means X (agent), player = -1 means O (rival)

        # Steps:
        # 1) Pick a random (row, col) from self.available_cells
        # 2) Remove it from self.available_cells so it can't be used again
        # 3) Put the player's value on the board in that position
        pass       

    


    def check_win(self):
        #add_your implementation:
        # Return:
        #   1  → agent wins
        #  -1  → rival wins
        #   0  → no winner yet
        # Check all rows, columns, and both diagonals.
        pass

    def is_board_full(self):
        #add your implementation
        #Check whether the board is full (no empty cells).
        pass

    def is_game_over(self):
        
        # Return True if the game is finished:
        # - someone won (check_win() != 0), OR
        # - there are no moves left (len(self.available_cells) == 0)
        pass

    
    def print_board(self):

        # Print the current board in a friendly way.

        # Steps:
        # 1) Print "Board:"
        # 2) For each row:
        # - convert each cell (1/-1/0) into a character ('X'/'O'/'_')
        # - print the converted row
        pass
                
    
    def cell_to_char(self, cell):
        # Implement cell_to_char(cell):
        # - If cell equals 1, return 'X'
        # - If cell equals -1, return 'O'
        # - Otherwise (cell equals 0), return '_'
        pass
       
    def array_to_string(self):
        # Implement array_to_string():
        # - If no board is given, use self.board
        # - Create an empty string called result
        # - Go through each row in the board
        # - Convert each cell in the row to a character using cell_to_char()
        # - Join the characters of the row into a string
        # - Add the row string to result
        # - Return the final string (without extra spaces)
        pass
       
    
    def update_scores(self):
        #Assign a score to each saved board state after the game ends.
       
        
        # Go over the saved board states from last move to first move,
        # and save each board state together with its score.
        #
        # Steps: (add your implementation for steps 2-4)
        # 1) Compute the final game score (win / loss / tie) using SCORE_CONSTANTS.
        #    This is the score for the LAST board state
        #    (already implemented in the line below — no need to change it):

        game_score = self.score_constants.get(self.check_win(), 0)

        # 2) Walk backward through the saved board states (from last to first).
        
        # 3) Each step backward multiplies the score by gamma, so earlier moves
        #    get less credit (discounting).
        
        # 4) Save (board_state, score) into boards_states_scores.
        
        
   




        
    def print_boards_states_scores(self):
        # add your implementation:

        # - Print a title
        # - Go through all saved (board, score) pairs in boards_states_scores
        # - For each pair:
        #     * Print the board state
        #     * Print its score
        pass

    def get_final_result(self):
        
        # Implement get_final_result():
        # - Use check_win() to find who won the game
        # - If the result is 1, return a message saying the agent (X) wins
        # - If the result is -1, return a message saying the rival (O) wins
        # - Otherwise, return a message saying the game ended in a tie
        pass
       


if __name__ == '__main__':

    plan = ('random', 'random')  # Default to random moves for both players
    game = Game(plan)
    
    while not game.is_game_over():
        game.play()
    
    # Show the board at the end of the game
    # Show who won (or if the game ended in a draw)
    # Give scores to all previous moves
    # Show each move with its score
    # Show how many moves were saved


