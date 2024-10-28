import pygame
import button

pygame.init()

# Create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Game variables
gamePaused = False
menuState = "main"

# Define fonts
font = pygame.font.SysFont("arialblack", 40)

# Define colours
TEXT_COL = (255, 255, 255)

# Load button images
resumeImg = pygame.image.load("images/button_resume.png").convert_alpha()
optionsImg = pygame.image.load("images/button_options.png").convert_alpha()
quitImg = pygame.image.load("images/button_quit.png").convert_alpha()
videoImg = pygame.image.load("images/button_video.png").convert_alpha()
audioImg = pygame.image.load("images/button_audio.png").convert_alpha()
keysImg = pygame.image.load("images/button_keys.png").convert_alpha()
backImg = pygame.image.load("images/button_back.png").convert_alpha()

# Create button instances
resumeButton = button.Button(304, 125, resumeImg, 1)
optionsButton = button.Button(297, 250, optionsImg, 1)
quitButton = button.Button(336, 375, quitImg, 1)
videoButton = button.Button(226, 75, videoImg, 1)
audioButton = button.Button(225, 200, audioImg, 1)
keysButton = button.Button(246, 325, keysImg, 1)
backButton = button.Button(332, 450, backImg, 1)

def drawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Game loop
run = True
while run:

    screen.fill((52, 78, 91))

    # Check if game is paused
    if gamePaused == True:
        # check menu state
        if menuState == "main":
            # Draw pause screen buttons
            if resumeButton.draw(screen):
                gamePaused = False
            if optionsButton.draw(screen):
                menuState = "options"
            if quitButton.draw(screen):
                run = False
        # Check if the options menu is open
        if menuState == "options":
            # Draw the different options buttons
            if videoButton.draw(screen):
                print("Video Settings")
            if audioButton.draw(screen):
                print("Audio Settings")
            if keysButton.draw(screen):
                print("Change Key Bindings")
            if backButton.draw(screen):
                menuState = "main"
    else:
        drawText("Press P to pause", font, TEXT_COL, 200, 250)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                gamePaused = True
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

pygame.quit()
