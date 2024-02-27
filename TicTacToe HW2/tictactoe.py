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
    # max_value function return the maximum value as well as the best action given a board
    # the function checks for all possible actions 
    # and returns value of action that leads to a maximum value possible
    def max_value(board):
        v = -math.inf
        best_action = None
        if terminal(board):
            return best_action, utility(board)
        for action in actions(board):
            _, minValue = min_value(result(board, action))
            if(minValue > v):
                v = minValue
                best_action = action
        return best_action, v

    # min_value function return the minimum value as well as the best action given a board
    # the function checks for all possible actions
    # and returns value of action that leads to a minimum value possible
    def min_value(board):
        v = math.inf
        best_action = None
        if terminal(board):
            return best_action, utility(board)
        for action in actions(board):
            _, maxValue = max_value(result(board, action))
            if(maxValue < v):
                v = maxValue
                best_action = action
        return best_action, v

    if player(board) == "X":
        best_action, _ = max_value(board)
    else:
        best_action, _ = min_value(board)
    print(best_action)
    return best_action