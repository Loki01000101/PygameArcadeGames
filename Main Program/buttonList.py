import pygame
import button

pygame.init()
pygame.display.set_mode()

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


startButton = createButton(299.5, 210, "images/gameButtons/startLong Background Removed.png", 1)
settingsButton = createButton(299.5, 310, "images/gameButtons/settingsLong Background Removed.png", 1)
quitButton = createButton(302, 410, "images/gameButtons/quitLong Background Removed.png", 1)
backButton = createButton(2, 510, "images/gameButtons/backLong Background Removed.png", 1)
leftArrowButton = createButton(275, 510, "images/gameButtons/rewind Background Removed.png", 1)
rightArrowButton = createButton(431, 510, "images/gameButtons/fastFoward Background Removed.png", 1)
confirmButton = createButton(152, 350, "images/gameButtons/okLong Background Removed.png", 1)
cancelButton = createButton(450, 350, "images/gameButtons/cancelLong Background Removed.png", 1)
    
