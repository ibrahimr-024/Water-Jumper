
import pygame

pygame.init()


size = (800, 600)
screen = pygame.display.set_mode(size)

# ------------------ Defining Variables ---------------
# Define some colors
BLACK = (0, 0, 0)

# Set background image for scene
background_image = pygame.image.load("Main Menu Backdrop.png")

# Define fonts for text
font = pygame.font.SysFont('Calibri', 25, True, False)
font_B = pygame.font.SysFont('Calibri', 70, True, False)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Creating function for main menu scene
def main_Menu():
    intro = True
    while intro == True:
        screen.blit(background_image, [-400,-300])
        
        text = font.render('Press enter to start', True, BLACK)
        screen.blit(text, [275, 300])
        
        text_B = font_B.render("Water Jumper", True, BLACK)
        screen.blit(text_B, [175, 200])
        # Creating user control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

        pygame.display.flip()
        clock.tick(60)
