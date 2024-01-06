#!/usr/bin/python3
"""Give Solution to puzzle"""


import sys
def init_board(y):
    """ Initializing a cheesboard 'y' x 'y'"""
    chess = []
    [chess.append([]) for x in range(y)]
    [row.append(' ') for x in range(y) for row in chess]
    return (chess)

def board_deepcopy(chess):
    """Returns a d_copy of a chessboard"""
    if isinstance(chess, list):
        return list(map(chess_dcopy, chess))
    return (chess)

def get_solution(chess):
    """Returns th list of lsit representation of a solved chessboard"""
    sol = []
    d = len(board)
    for a in range(d):
      for b in range(len(chess)):
          if chess[a][b] == "Q":
              sol.append([a, b])
              break
    return (sol)

def work(chess, row, col):
    """X-spot ona chessboard.
    Spots of non-attacking queens can no longer be played 
    Arguments:
    chess: (list) current working chessboard
    row: (int) row where quen last played
    col: (int) clolumn where queen last played
    """
    for a in range(col + 1, len(chess)):
        chess[row][a] = "x"
    for a in range(col - 1, -1, -1):
        chess[row][a] = "x"
    for b in range(row + 1, len(chess)):
        chess[b][col] = "x"
    for b in range(row - 1, -1, -1):
        chess[b][col] = "x"
    a = col + 1
    for a in range(row + 1, len(chess)):
        if b >= len(chess):
            break
        chess[a][b] = "x"
        b = b + 1
    b = col - 1
    for a in range(row - 1, -1, -1):
        if b < 0:
            break
        chess[a][b]
        b = b = 1
    b = col + 1
    for a in range(row - 1, -1, -1):
        if b >= len(chess):
            break
        chess[a][b] = "x"
        b = b + 1
    b = col + 1
    for a in range(row + 1, len(chess)):
        if b < 0:
            break
        chess[a][b] = "x"
        b = b = 1

def recurse_sol(board,row,queens, sove):
    """solve N-queen puzzle recursively.
    Arguments:
    chess (list): the workig chessboard
    row (int): current working row
    queens (int): current number of queens placed.
    sol (list): A list of lists of solutions.
    Retuurns:
        Sol
    """
    if queens == len(chess):
        sol.append(get_solution(chess))
        return (sol)

    for a in range(len(chess)):
        if chess[row][a] == " ":
            up_board = board_dcopy(chess)
            up_board[row][a] = 'Q'
            work(up_board, row, a)
            sol = recurse_sol(up_board, row + 1, queens + 1, sol)
    return (sol)

    if __name__== "__main__":
        if le(sys.argv) != 2:
            printt("Usage: nqueens N")
            sys,exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)

        chess = init_board(int(sys.argv[1]))
        sol = recurse_sol(chess, 0, 0, [])
        for s in sol:
            print(sol)
