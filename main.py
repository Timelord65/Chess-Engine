import chess
import chess_board
import collections
from copy import deepcopy
from typing import Final

INF: Final = 1000000


def material_balance(board):
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
        3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
        3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
        5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
        9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens))
    )

def MinMax(board, depth=4, comp_plays=0, turn=0) -> int:
    # Turn == 1 for white and Turn == 0 for black


    # Insert Code for checking end game conditions and assigining appropriate evaluations
    if board.is_checkmate():
        return INF * (-1 if turn==1 else 1), board
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw():
        return 0.5, board

    if depth == 0 or depth < 0:
        return -1 * material_balance(board), board

    candidates = {}
    for move in board.legal_moves:
        # print("stuff")
        # print(board.outcome())
        # print(candidates.keys())
        # print(move)
        depth -= 1
        A = deepcopy(board)
        # print(move)
        A.push_san(str(move))
        turn = (1 if turn==0 else 0)
        print(MinMax(A, depth, 0, turn))
        evaluation, something = MinMax(A, depth, 0, turn)
        print(evaluation)
        try:
            candidates[evaluation].append(A)
        except KeyError:
            candidates[evaluation] = []
            candidates[evaluation].append(A)

    print(candidates.keys())

    current_max = -100000000
    print(candidates.keys())
    for k in candidates.keys():
        if k > current_max:
            current_max = k

    print(board)
    board = candidates[k][0]
    print(board)
    return (-1 * material_balance(board)), board
