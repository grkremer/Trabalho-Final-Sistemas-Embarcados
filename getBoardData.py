import berserk
# INSTRUCOES   
# CONTA Lichess:
# Login : tf_emb_chess
# Password : TBxkyekCJSAhg23
# Jogar contra o Stockfish sendo as pecas pretas
# Rodar o programa apos Stockfish fazer o seu primeiro movimento 



# currently:
#    whites first move needs to be made before running the script
#    game's id needs to be manually inputed 
#    white's player starts on the top halp of the board

# ++++++++++++++++ TO AVOID HAVING TO ENTER GAME_ID MANNUALLY ++++++++++++++++++++++++
# gets game history, 
# itr = client.board.stream_incoming_events()
# selects the last one
# for item in itr:
#      print(item)
# uses last game_id to stream game state


# creates initial board state and global variables
last_move = "aaaa"
whites_turn = True 
rows, cols = (8, 8)
board = arr = [['_' for i in range(cols)] for j in range(rows)]

def writes_into_file():
     global board
     try:
          with open("board.txt","w") as f:
               for row in board:
                    f.write("%s\n" % row)
     except FileNotFoundError:
          print("File not acessible")



def init_file():
     global board
     rows, cols = (8, 8)
     board = arr = [['_' for i in range(cols)] for j in range(rows)]


     board[7] = ['r','n','b','k','q','b','n','r']
     board[6] = ['p','p','p','p','p','p','p','p']
     board[1] = ['P','P','P','P','P','P','P','P']
     board[0] = ['R','N','B','K','Q','B','N','R']
     writes_into_file()


def decodes_notation(move:str):
     global board
     notation = ['a','b','c','d','e','f','g','h']
     for number,letter in enumerate(notation):
          move = move.replace(letter,str(number))
     old_col,old_row,new_col,new_row = [*move]
     print(old_col,old_row,new_col,new_row)
     board[int(new_row)-1][7-int(new_col)] = board[int(old_row)-1][7-int(old_col)]
     board[int(old_row)-1][7-int(old_col)] = '_'
     for row in board:
          print("%s\n" % row)
     return 



#chesck if last move known is a new one 
def updates_board(moves:str):
     global last_move
     global board
     # print("moves:", moves)
     # print("moves -4:", moves[-4:])
     if last_move == moves[-4:]:
          return
     last_move = moves[-4:] 
     print("last_move:",last_move)
     decodes_notation(last_move)
     writes_into_file()


token = 'lip_TtHWeHXQzjQHvuyFAfL9'

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

itr = client.board.stream_game_state("MntomZas")
#writes initial board
init_file()
for item in itr:
     print(item)
     try:
          moves = ''.join(item['state']['moves'])
     except KeyError:
          print(type(item['type']))
          moves = ''.join(item['moves'])
     print(moves)
     print(type(moves))
     updates_board(moves)




