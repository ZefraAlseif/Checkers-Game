import pygame
from logic import Logic, Move
pygame.init()
WIDTH = HEIGHT = 512 
DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

IMAGES = {}

# Initialize a global dictionary of images
def loadImages():
    pieces = ["rP","rK","bK","bP"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("Sprites/"+ piece+ ".png"),(SQ_SIZE,SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    game_state = Logic() 
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    loadImages()
    running = True
    sq_selected = ()
    player_clicks = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row,col):
                    sq_selected = ()
                    player_clicks = []
                else:
                    sq_selected = (row,col)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2:
                    move = Move(player_clicks[0],player_clicks[1],game_state.board)
                    print(move.getNotation())
                    game_state.makeMove(move)
                    sq_selected = ()
                    player_clicks = []
        drawGameState(screen,game_state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

def drawGameState(screen,game_state):
    drawBoard(screen)
    drawPieces(screen,game_state.board)

def drawBoard(screen):
    colors = [pygame.Color("gold"),pygame.Color("blue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(screen,color,pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
    