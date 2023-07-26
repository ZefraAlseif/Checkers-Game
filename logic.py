class Logic():
    
    def __init__(self):
        self.board = [["--","bP","--","bP","--","bP","--","bP"],
                      ["bP","--","bP","--","bP","--","bP","--"],
                      ["--","bP","--","bP","--","bP","--","bP"],
                      ["--","--","--","--","--","--","--","--"],
                      ["--","--","--","--","--","--","--","--"],
                      ["rP","--","rP","--","rP","--","rP","--"],
                      ["--","rP","--","rP","--","rP","--","rP"],
                      ["rP","--","rP","--","rP","--","rP","--"]]
        self.red_to_move = True
        self.move_log = []
    # Making a move function
    def makeMove(self,move):
         # capture move
        if move.capture_move:
            deltaR = (move.end_row - move.start_row)//2
            deltaC = (move.end_col - move.start_col)//2
            self.board[move.start_row+deltaR][move.start_col+deltaC] = "--"
        
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.red_to_move = not self.red_to_move
        
       
        
    # Undo a move function:
    def undoMove(self):
        move = self.move_log.pop()
        self.board[move.start_row][move.start_col] = move.piece_moved
        self.board[move.end_row][move.end_col] = move.piece_captured
        self.red_to_move = not self.red_to_move
        
        # undo capture move
        if move.capture_move:
            deltaR = abs(move.end_row - move.start_row)/2
            deltaC = abs(move.end_col - move.start_col)/2
            self.board[move.end_row][move.end_col] = "--"
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.start_row+deltaR][move.start_col+deltaC] = move.piece_captured
            
    # Obtain all legal moves
    def validMoves(self):
        return self.possibleMoves()
    
    # Obtain all possible moves
    def possibleMoves(self):
        possible_moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == "r" and self.red_to_move) or (turn == "b" and not self.red_to_move):
                    piece = self.board[r][c][1]
                    if piece == "P":
                        self.getPawnMoves(r,c,possible_moves)
                    elif piece == "Q":
                        self.getQueenMoves(r,c,possible_moves)
        return possible_moves
    
    # Get all pawn moves
    def getPawnMoves(self,r,c,possible_moves):
        if self.red_to_move: # if red pawn moves
            if (r-1 >= 0) and (c+1 <= 7):
                if self.board[r-1][c+1] == "--": 
                    possible_moves.append(Move((r,c),(r-1,c+1),self.board))
                # Best to do the captures in a loop
                if self.board[r-1][c+1][0] == "b" and ((r-2 >= 0) and (c+2 <= 7)):
                    if self.board[r-2][c+2] == "--":
                        possible_moves.append(Move((r,c),(r-2,c+2),self.board,capture_move=True))
            if (r-1 >= 0) and (c-1 >= 0):
                if self.board[r-1][c-1] == "--":
                    possible_moves.append(Move((r,c),(r-1,c-1),self.board))
                if self.board[r-1][c-1][0] == "b" and ((r-2 >= 0) and (c-2 >= 0)):
                    if self.board[r-2][c-2] == "--":
                        possible_moves.append(Move((r,c),(r-2,c-2),self.board,capture_move=True))
        elif not self.red_to_move:  
            if (r+1 <= 7) and (c+1 <= 7):
                if self.board[r+1][c+1] == "--":
                    possible_moves.append(Move((r,c),(r+1,c+1),self.board))
                # Best to do the captures in a loop
                if self.board[r+1][c+1][0] == "r" and ((r+2 <= 7) and (c+2 <= 7)):
                    if self.board[r+2][c+2] == "--":
                        possible_moves.append(Move((r,c),(r+2,c+2),self.board,capture_move=True))
            if (r+1 <= 7) and (c-1 >= 0):
                if self.board[r+1][c-1] == "--":
                    possible_moves.append(Move((r,c),(r+1,c-1),self.board))
                if self.board[r+1][c-1][0] == "r" and ((r+2 <= 7) and (c-2 >= 0)):
                    if self.board[r+2][c-2] == "--":
                        possible_moves.append(Move((r,c),(r+2,c-2),self.board,capture_move=True))
            
                
    # Get all queen moves
    def getQueenMoves(self,r,c,possible_moves):
        pass
        

class Move():
    rows_to_ranks = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    ranks_to_rows = {v: k for k,v in rows_to_ranks.items()}
    
    files_to_cols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files = {v: k for k,v in files_to_cols.items()}
    
    def __init__(self,start_sq,end_sq,board,capture_move = False,):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]

        # capturing moves
        self.capture_move = capture_move
        if capture_move:
            self.piece_captured = "rP" if self.piece_moved == "bP" else "bP"
        
        self.moveID =  self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        #print(self.moveID)
    
    # Overriding the equals method
    def __eq__(self, other):
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False     
    
    
    def getNotation(self):
        return self.piece_moved[1] + self.getRankedFile(self.end_row,self.end_col)
    
    def getRankedFile(self,row,col):
        return self.cols_to_files[col] + self.ranks_to_rows[row]