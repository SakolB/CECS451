"""
Tic Tac Toe Player
"""
import math
import copy



X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of empty cells, if there are none, the game is tie
    # return None
    if sum(row.count(EMPTY) for row in board)== 0:
        return None
    # Count the number of x and if there are more x than o, return o, otherwise return x
    if sum(row.count("X") for row in board) > sum(row.count("O") for row in board):
        return "O"
    return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create a set to store all possible actions
    # iterate through the board and add the empty cells to the set
    # since any empty cell is a possible move
    # return the set
    set_of_actions = set()
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell == EMPTY:
                possible_move = (row_index, cell_index)
                set_of_actions.add(possible_move)
    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if the action is not in the set of possible actions, raise an exception
    # otherwise, create a deep copy of the board and update the cell with the player's symbol
    # and return the new board
    if(action not in actions(board)):
        raise Exception("Invalid action")
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check if there is a winner in the rows, columns or diagonals
    # if there is a winner, return the winner
    # otherwise return none
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for cell in range(3):
        if(board[0][cell] == board[1][cell] == board[2][cell] != EMPTY):
            return board[0][cell]
    if(board[0][0] == board[1][1] == board[2][2] != EMPTY):
        return board[0][0]
    if(board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[0][2]
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if there is a winner or the board is full, return True
    # otherwise return False
    if winner(board) != EMPTY:
        return True
    if sum(row.count(EMPTY) for row in board) == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if the winner is X, return 1
    # if the winner is O, return -1
    # otherwise return 0
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # max_value function return the maximum value given a board
    # the function checks for all possible actions 
    # and returns value of action that leads to a maximum value possible
    def max_value(board):
        v = -math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
    
    # min_value function return the minimum value given a board
    # the function checks for all possible actions
    # and returns value of action that leads to a minimum value possible
    def min_value(board):
        v = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v
    
    # if the player is X, return the action that leads to the maximum value
    # the max function takes the output of actions(board) which is a set of possible actions
    # then uses the lambda function to decide the comparison value for each action
    # the lambda function is used to find the action that leads to the minimum value
    # since the objective of player X is to maximize the minimum value
    # the best_action in this case will be the action that maximize the minimum value

    # if the player is O, return the action that leads to the minimum value
    # the min function takes the output of actions(board) which is a set of possible actions
    # then uses the lambda function to decide the comparison value for each action
    # the lambda function is used to find the action that leads to the maximum value
    # since the objective of player O is to minimize the maximum value
    # the best_action in this case will be the action that minimize the maximum value
    if player(board) == "X":
        best_action = max(actions(board), key = lambda action: min_value(result(board, action)))
    else:
        best_action = min(actions(board), key = lambda action: max_value(result(board, action)))
    
    return best_action