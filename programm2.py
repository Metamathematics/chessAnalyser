#indent tabs
# -*- coding: utf-8 -*-
import chess
import requests
import time

def undefendent_pieces(color):
    undef_pieces = chess.SquareSet()
    for piece_type in range(1,7):
        for piece in board.pieces(piece_type, color):
            if not board.is_attacked_by(color, piece):
                undef_pieces.add(piece)
    return undef_pieces

def get_fen_out_of_adress(adress):
    
    page = requests.get(adress)
    content = page.text
    i_initial_fen = content.find("initialFen")
    index_of_fen_beg = content.find("\"fen\":", i_initial_fen) + 7
    index_of_fen_end = content.find(",",index_of_fen_beg) - 1
    extracted_fen = content[index_of_fen_beg : index_of_fen_end]
    #print("FEN: " , extracted_fen)
    return extracted_fen

def find_lichess_url():
    import os
    cmd = """osascript -e 'tell application \"Safari\" to get the URL of every tab of every window'"""
    os.system(cmd)

def show_udef_pieces():
    print("Board: ")
    print (board)
    print ()
    undef_w = undefendent_pieces(chess.WHITE)
    undef_b = undefendent_pieces(chess.BLACK)
    undef_all = undef_b.union(undef_w)
    print("White")
    print(undef_w)
    print("Black")
    print(undef_b)
    print("All")
    print(undef_all)


#find_lichess_url()
url="https://lichess.org/Bp3hWC7MB9Y1"
old_fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

for i in range (1000):
    url_fen = get_fen_out_of_adress(url)
    if url_fen == old_fen:
        time.sleep(3)
        continue
    board = chess.Board(url_fen)
    show_udef_pieces()
    old_fen = url_fen





