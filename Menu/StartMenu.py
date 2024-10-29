import pygame
import button

pygame.init()

# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("-=:]Pygame Arcade[:=-")

# Game variables
menuState = "start"

# Define fonts
FONT = pygame.font.SysFont("arialblack", 40)

# Define colours
TEXT_COL = (255, 255, 255)

# Helper function to create buttons
def createButton(x, y, imgPath, scale=1):
    try:
        image = pygame.image.load(imgPath).convert_alpha()
        return button.Button(x, y, image, scale)
    except pygame.error as e:
        print(f"Error loading image '{imgPath}': {e}")
        placeholderImage = pygame.Surface((100, 50))
        placeholderImage.fill((255, 0, 0))  # Red colour for error
        return button.Button(x, y, placeholderImage, scale)

# Load images
arcadeLogo = pygame.image.load("images/pygameArcadeLogo.png").convert_alpha()

# Create buttons
startButton = createButton(299.5, 210, "images/gameButtons/startLong Background Removed.png", 1)
settingsButton = createButton(299.5, 310, "images/gameButtons/settingsLong Background Removed.png", 1)
quitButton = createButton(302, 410, "images/gameButtons/quitLong Background Removed.png", 1)
backButton = createButton(2, 510, "images/gameButtons/backLong Background Removed.png", 1)

def drawText(text, font, textCol, x, y):
    img = font.render(text, True, textCol)
    screen.blit(img, (x, y))

# Game loop
run = True
while run:
    screen.fill((156, 156, 156))

    # Check menu state and draw correct menu
    if menuState == "start":
        screen.blit(arcadeLogo, (144, 30))
        if startButton.draw(screen):
            menuState = "gameLibrary"
        elif settingsButton.draw(screen):
            menuState = "settings"
        elif quitButton.draw(screen):
            run = False
    elif menuState == "settings":
        drawText("Settings Page", FONT, TEXT_COL, 200, 250)
        if backButton.draw(screen):
            menuState = "start"
    elif menuState == "gameLibrary":
        drawText("Game Library", FONT, TEXT_COL, 200, 250)
        if backButton.draw(screen):
            menuState = "start"

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
