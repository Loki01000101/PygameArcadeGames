import pygame
import button
import buttonList as b
import ticTacToeGame1 as TicTacToe
from pygame.locals import *

# Initialize Pygame and create the display before loading images
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("-=:]Pygame Arcade[:=-")

# Colors and fonts
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.SysFont("arialblack", 40)

# Game states and variables
menuState = "start"
TOTAL_GAMES = 5
if TOTAL_GAMES % 4 == 0:
    pages = TOTAL_GAMES / 4
else:
    pages = (1 + (TOTAL_GAMES // 4))
gameLibraryPages = [f"gameLibrary{i+1}" for i in range(int(pages))]
currentPage = 0

# Helper function to create buttons
def createButton(x, y, imgPath, scale=1):
    try:
        image = pygame.image.load(imgPath).convert_alpha()
        return button.Button(x, y, image, scale)
    except pygame.error as e:
        print(f"Error loading image '{imgPath}': {e}")
        placeholderImage = pygame.Surface((100, 50))
        placeholderImage.fill((255, 0, 0))  # Red color for error
        return button.Button(x, y, placeholderImage, scale)

# Load and scale images
ARCADE_LOGO = pygame.image.load("images/pygameArcadeLogo.png").convert_alpha()
GAME_SETTINGS = pygame.image.load("images/gameSettings.jpg").convert_alpha()
GAME_SETTINGS = pygame.transform.scale(GAME_SETTINGS, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale to fit the screen

# Icon images (scaled to 288x144) before creating buttons
flappyBirdImage = pygame.transform.scale(pygame.image.load("images/gameIcons/flappyBird.png").convert_alpha(), (325, 169))
snakeImage = pygame.transform.scale(pygame.image.load("images/gameIcons/snake.jpg").convert_alpha(), (325, 169))
tetrisImage = pygame.transform.scale(pygame.image.load("images/gameIcons/tetris.jpeg").convert_alpha(), (325, 169))
ticTacToeImage = pygame.transform.scale(pygame.image.load("images/gameIcons/ticTacToe.png").convert_alpha(), (325, 169))
spaceInvadersImage = pygame.transform.scale(pygame.image.load("images/gameIcons/spaceInvaders.png").convert_alpha(), (325, 169))

# Buttons
startButton = b.startButton
settingsButton = b.settingsButton
quitButton = b.quitButton
backButton = b.backButton
leftArrowButton = b.leftArrowButton
rightArrowButton = b.rightArrowButton

# Create icon buttons with scaled images
flappyBirdIcon = button.Button(50, 100, flappyBirdImage, 1)
snakeIcon = button.Button(425, 100, snakeImage, 1)
tetrisIcon = button.Button(50, 319, tetrisImage, 1)
ticTacToeIcon = button.Button(425, 319, ticTacToeImage, 1)
spaceInvadersIcon = button.Button(50, 100, spaceInvadersImage, 1)

def drawText(text, x, y):
    img = FONT.render(text, True, TEXT_COLOR)
    screen.blit(img, (x, y))

def handlePageNavigation():
    """Handles page navigation for game library pages."""
    global currentPage, menuState
    if currentPage > 0 and leftArrowButton.draw(screen):  # Only show left arrow if not on the first page
        currentPage -= 1
    elif currentPage < len(gameLibraryPages) - 1 and rightArrowButton.draw(screen):  # Only show right arrow if not on the last page
        currentPage += 1
    menuState = gameLibraryPages[currentPage]

def confirmQuit():
    """Displays a confirmation message for quitting."""
    drawText("Are you sure you want to quit?", 100, 250)
    confirmButton = b.confirmButton
    cancelButton = b.cancelButton
    if confirmButton.draw(screen):
        return False  # Exit the game
    elif cancelButton.draw(screen):
        return True  # Return to the main menu
    return None  # No action taken

# Game loop
run = True
while run:
    screen.fill((156, 156, 156))

    if menuState == "start":
        screen.blit(ARCADE_LOGO, (144, 30))
        if startButton.draw(screen):
            menuState = gameLibraryPages[currentPage]  # Start with the first library page
        elif settingsButton.draw(screen):
            menuState = "settings"
        elif quitButton.draw(screen):
            menuState = "confirmQuit"

    elif menuState == "settings":
        screen.blit(GAME_SETTINGS, (0,0))
        if backButton.draw(screen):
            menuState = "start"

    elif menuState == "confirmQuit":
        quitDecision = confirmQuit()
        if quitDecision is False:
            run = False
        elif quitDecision is True:
            menuState = "start"

    elif menuState in gameLibraryPages:
        drawText(f"Game Library Page {currentPage + 1}", 200, 20)
        handlePageNavigation()
        if backButton.draw(screen):
            menuState = "start"

        if menuState == gameLibraryPages[0]:
            if flappyBirdIcon.draw(screen):
                print("Flappy bird icon clicked")
            elif snakeIcon.draw(screen):
                print("Snake icon clicked")
            elif tetrisIcon.draw(screen):
                print("Tetris icon clicked")
            elif ticTacToeIcon.draw(screen):
                TicTacToe.runGame(screen)
        elif menuState == gameLibraryPages[1]:
            if spaceInvadersIcon.draw(screen):
                print("Space invaders icon clicked")

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
