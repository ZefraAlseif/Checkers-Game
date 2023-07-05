class Logic():
    
    def __init__(self):
        self.board = [["bP","--","bP","--","bP","--","bP","--"],
                      ["--","bP","--","bP","--","bP","--","bP"],
                      ["bP","--","bP","--","bP","--","bP","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["rP","--","rP","--","rP","--","rP","--"],
                      ["--","rP","--","rP","--","rP","--","rP"],
                      ["rP","--","rP","--","rP","--","rP","--"]]
        self.red_to_move = True
        self.move_log = []
    
    def makeMove(self,move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.red_to_move = not self.red_to_move

class Move():
    rows_to_ranks = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    ranks_to_rows = {v: k for k,v in rows_to_ranks.items()}
    
    files_to_cols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files = {v: k for k,v in files_to_cols.items()}
    
    def __init__(self,start_sq,end_sq,board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
    
    def getNotation(self):
        return self.piece_moved[1] + self.getRankedFile(self.end_row,self.end_col)
    
    def getRankedFile(self,row,col):
        return self.cols_to_files[col] + self.ranks_to_rows[row]