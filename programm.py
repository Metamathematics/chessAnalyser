#indent tabs
# -*- coding: utf-8 -*-
'''
import ulrlib2

url="https://lichess.org/training/62510"
page=ulrlib2.urlopen(url)
content=page.read()

filename="/Users/sergeygerodes/Code/chess_helper/test/testfile"
file=open(filename,"w")
file.write(content)
file.close()
'''

def print_board(board):
    for rank in board:
        print rank

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen2 = "8/​1p6/​1P1p4/​1B1Pk2p/​8/​7K/​8/​4r3"

def fen_to_matrix(fen):
    for i in range(1,9):
        fen = fen.replace(str(i),'-' * i)
    print fen
    fen = fen.split("/")
    #print fen
    board=[['-']*8]*8
    #print_board(board)
    for r_index,rank_element in enumerate(fen):
        #print rank_element
        for f_index,square_element in enumerate(rank_element):
            #print square_element
            board[r_index][f_index]=square_element
    return board





print_board(fen_to_matrix(fen))
print_board(fen_to_matrix(fen2))

