import chess





if __name__.__eq__("__main__"): 
    board = chess.Board()

    legal_moves = list(board.legal_moves)

    for move in legal_moves: 
        print(move)

    pieces = [(square, board.piece_at(square)) for square in chess.SQUARES if board.piece_at(square)]

    # Print them in human-readable format
    for square, piece in pieces:
        print(f"{piece.symbol()} on {chess.square_name(square)}")


    
