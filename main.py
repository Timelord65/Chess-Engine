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

def quiescence_search(board, alpha, beta, turn):
    """Quiescence search to handle captures at end of search depth"""
    stand_pat = material_balance(board) * (1 if turn == 1 else -1)
    
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat
    
    # Only consider captures in quiescence search
    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiescence_search(board, -beta, -alpha, 1 - turn)
            board.pop()
            
            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    
    return alpha

def MinMax(board, depth=4, alpha=-INF, beta=INF, turn=0):
    # Turn == 1 for white and Turn == 0 for black
    
    # Check end game conditions
    if board.is_checkmate():
        return INF * (-1 if turn==1 else 1), None
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw():
        return 0, None

    if depth == 0:
        # Use quiescence search for captures
        evaluation = quiescence_search(board, alpha, beta, turn)
        return evaluation, None

    best_move = None
    best_evaluation = -INF if turn == 1 else INF
    
    for move in board.legal_moves:
        board.push(move)
        evaluation, _ = MinMax(board, depth - 1, alpha, beta, 1 - turn)
        board.pop()
        
        if turn == 1:  # White's turn - maximize
            if evaluation > best_evaluation:
                best_evaluation = evaluation
                best_move = move
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Alpha-beta pruning
        else:  # Black's turn - minimize
            if evaluation < best_evaluation:
                best_evaluation = evaluation
                best_move = move
            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha-beta pruning

    return best_evaluation, best_move
