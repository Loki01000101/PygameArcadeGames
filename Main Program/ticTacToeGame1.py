import pygame
import buttonList as b
from pygame.locals import *

def runGame(screen):  # Accept screen as an argument
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 400  # Adjusted height for scores

    # Define variables
    lineWidth = 6
    markers = [[0] * 3 for _ in range(3)]  # Initialize 3x3 grid
    clicked = False
    player = 1
    winner = 0
    gameOver = False

    # Score variables
    player1_score = 0
    player2_score = 0
    filled_cells = 0  # Track filled cells

    # Define colors and fonts
    GREEN, RED, BLUE = (0, 255, 0), (255, 0, 0), (0, 0, 255)
    TEXT_COLOR, GRAY = (255, 255, 255), (169, 169, 169)
    FONT = pygame.font.SysFont("arialblack", 40)

    # Create play again rectangle
    againRect = Rect(370, 175, 280, 70)

    def drawGrid():
        bg, grid = (255, 255, 200), (50, 50, 50)
        screen.fill(bg)
        # Draw the grid lines with offset
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (5, x * 100 + 5), (300 + 5, x * 100 + 5), lineWidth)
            pygame.draw.line(screen, grid, (x * 100 + 5, 5), (x * 100 + 5, 300 + 5), lineWidth)
        # Draw a square border around the grid
        pygame.draw.rect(screen, grid, (5, 5, 301, 301), lineWidth)

    def drawMarkers():
        for x in range(3):
            for y in range(3):
                if markers[x][y] == 1:
                    pygame.draw.line(screen, RED, (x * 100 + 25, y * 100 + 20), 
                                     (x * 100 + 85, y * 100 + 90), lineWidth + 2)
                    pygame.draw.line(screen, RED, (x * 100 + 25, y * 100 + 90), 
                                     (x * 100 + 85, y * 100 + 20), lineWidth + 2)
                elif markers[x][y] == -1:
                    pygame.draw.circle(screen, BLUE, (x * 100 + 55, y * 100 + 55), 40, lineWidth)

    def drawScores():
        scoreText = f"Player 1: {player1_score}    Player 2: {player2_score}"
        scoreImg = FONT.render(scoreText, True, TEXT_COLOR)
        pygame.draw.rect(screen, GRAY, (20, 345, 522, 70))
        screen.blit(scoreImg, (25, 350))

    def checkWinner():
        nonlocal winner, gameOver, player1_score, player2_score, filled_cells
        for x in range(3):
            if abs(sum(markers[x])) == 3:  # Row check
                winner = 1 if sum(markers[x]) > 0 else 2
                player1_score += (winner == 1)
                player2_score += (winner == 2)
                gameOver = True
            elif abs(markers[0][x] + markers[1][x] + markers[2][x]) == 3:  # Column check
                winner = 1 if markers[0][x] + markers[1][x] + markers[2][x] > 0 else 2
                player1_score += (winner == 1)
                player2_score += (winner == 2)
                gameOver = True

        # Diagonal checks
        if abs(markers[0][0] + markers[1][1] + markers[2][2]) == 3 or abs(markers[2][0] + markers[1][1] + markers[0][2]) == 3:
            winner = 1 if markers[1][1] == 1 else 2
            player1_score += (winner == 1)
            player2_score += (winner == 2)
            gameOver = True

        # Check for a draw
        if filled_cells == 9 and winner == 0:
            gameOver = True
            winner = -1

    def drawWinner():
        if winner == -1:
            winText = "It's a draw!"
        else:
            winText = f"Player {winner} wins!"
        winImg = FONT.render(winText, True, TEXT_COLOR)
        pygame.draw.rect(screen, GRAY, (345, 45, 325, 70))
        screen.blit(winImg, (350, 50))  
        againText = "Play Again?"
        againImg = FONT.render(againText, True, TEXT_COLOR)
        pygame.draw.rect(screen, GRAY, againRect)
        screen.blit(againImg, (againRect.x + 15, againRect.y + 5))

    def gameRestart():
        nonlocal filled_cells, player, winner, gameOver
        markers[:] = [[0] * 3 for _ in range(3)]
        filled_cells = 0
        player, winner, gameOver = 1, 0, False
        screen.fill((255, 255, 200))  # Clear screen with background color

    run = True
    while run:
        drawGrid()
        drawMarkers()
        drawScores()

        if b.backButton.draw(screen):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if not gameOver:
                if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                    clicked = True
                elif event.type == pygame.MOUSEBUTTONUP and clicked:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    if 5 <= pos[0] < 305 and 5 <= pos[1] < 305:
                        xCell, yCell = (pos[0] - 5) // 100, (pos[1] - 5) // 100
                        if markers[xCell][yCell] == 0:
                            markers[xCell][yCell] = player
                            filled_cells += 1
                            player *= -1
                            checkWinner()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and againRect.collidepoint(event.pos):
                    gameRestart()

        if gameOver:
            drawWinner()
        
        pygame.display.update()
