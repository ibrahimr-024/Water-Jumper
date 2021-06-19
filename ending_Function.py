## Import modules
import pygame
pygame.init()

# Create window
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# ------------------ Defining Variables ---------------
# Define some colors
BLACK = (0, 0, 0)

# Define image for background of scene
end_Screen = pygame.image.load("End screen.jpg")

# Define fonts for text
font = pygame.font.SysFont('Calibri', 25, True, False)
font_B = pygame.font.SysFont('Calibri', 70, True, False)

# Creating function for ending scene
def ending():
    end = True
    while end == True:
        screen.blit(end_Screen, [-50, -250])
                
        end_Text_A = font_B.render("You reached the end!", True, BLACK)
        screen.blit(end_Text_A, [100, 20])
        
        end_Text_B = font_B.render("Congratulations!", True, BLACK)
        screen.blit(end_Text_B, [160, 80])        
        
        end_Text_C = font.render("Press Esc to exit", True, BLACK)
        screen.blit(end_Text_C, [300, 200])
        # user control 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = False
                    pygame.quit()
        pygame.display.flip()
        clock.tick(60)