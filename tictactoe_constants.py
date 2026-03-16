# tictactoe_constants.py
# Constants for Tic Tac Toe game
GAMMA = 0.9
SCORE_CONSTANTS = {
    1: 1,  # Agent's score
    -1: -1,  # Rival's score
    0: 0.5  # Tie score
}

BLOCKING_SCORE = 0.95

TOURNAMENT_NUMBER_OF_GAMES = 50
TOURNAMENT_INFO_FILE = "tournament_info.json"
TOURNAMENT_BOARDS_SCORES_FILE = "tournament_boards_scores.json"


GAME_PLANS = ['random', 'simple_heuristic', 'minimax', 'complex_heuristic', 'smart_agent_dict', 'smart_agent_cnn']
CNN_MODEL_PATH = 'xo_cnn_model_20250707_130013.h5'