##
# Pygame base template for opening a window - MVC version
# Simpson College Computer Science
# http://programarcadegames.com/
#

## Import modules and functions
import pygame
import random
from Main_Menu_function import main_Menu
from ending_Function import ending
pygame.init()

# Create window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Water Jumper")
## MODEL - Data use in system


# ------------------ Defining Variables ---------------
# Define some colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (194, 159, 64)

# init scroll
scroll = 0
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Call main menu scene
main_Menu()



# Creating class for the player
class Player():
    pos = [400, 480]
    size = [45, 100]
    speed = [0, 0]
    inAir = False;
        
    def draw_Character(self):
        pygame.draw.circle(screen, BLACK, [self.pos[0] , self.pos[1] - scroll], 25)
        pygame.draw.line(screen, BLACK, [self.pos[0] , self.pos[1]- scroll], [self.pos[0] , self.pos[1] + 50- scroll], 10)
        pygame.draw.line(screen, BLACK, [self.pos[0] , self.pos[1] + 50- scroll], [self.pos[0] - 25, self.pos[1] + 100- scroll], 10)
        pygame.draw.line(screen, BLACK, [self.pos[0], self.pos[1] + 50- scroll], [self.pos[0] + 25, self.pos[1] + 100- scroll], 10)
        pygame.draw.line (screen, BLACK, [self.pos[0], self.pos[1] + 25- scroll], [self.pos[0] - 25, self.pos[1] + 50- scroll], 10)
        pygame.draw.line (screen, BLACK, [self.pos[0], self.pos[1] + 25- scroll], [self.pos[0] + 25, self.pos[1] + 50- scroll], 10)

    
    def move(self):
        self.pos[0] += self.speed[0]
        # set a constant effect of gravity
        self.speed[1] += 0.4
        self.pos[1] += self.speed[1]
        
        # for if character jumps moves off screen
        if (self.pos[0] > 845):
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = 845

    def jump(self):
        if not self.inAir:
            self.speed[1] = -20
            self.inAir = True
    
    # check collision using pos and size
    def checkCollisions(self, other):
        if other.pos[1]  < self.pos[1] + self.size[1] and \
            other.pos[1]  + other.size[1] > self.pos[1] and \
            other.pos[0] < self.pos[0] + self.size[0] and \
            other.pos[0] + other.size[0] > self.pos[0]:
            if self.speed[1] >= 0:
                #land on something
                self.speed[1] = 0
                self.pos[1] = other.pos[1] - self.size[1]
                self.inAir = False
            else:
                # hit object from under
                self.speed[1] = 0
                self.pos[1] = other.pos[1] + other.size[1]
                self.inAir = True

# Creat instance of class
character = Player()


# Creating class for platforms
class Platform():
    def __init__(self):
            self.pos = [0, 0]
            self.colour = BROWN
            self.size = [0, 0]
    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        size_W = self.size[0]
        size_H = self.size[1]
        pygame.draw.rect(screen, self.colour, [x, y- scroll, size_W, size_H])


# Creating loop for randomized platforms
my_List = [Platform()]
y_inc = 0
for i in range(50):
    floors = Platform()
    y_loc = 470
    y_inc -= 150
    floors.pos[1] = y_loc + y_inc
    floors.pos = [random.randrange(0, 650), y_loc + y_inc]
    floors.size = [150, 20]
    my_List.append(floors)

# Creating the beginning platform as an instance of the class Platform
beg_Plat = Platform()
beg_Plat.pos = [-100, 590- scroll]
beg_Plat.size = [1000, 40]

#--------------- Main Game Loop ------------------
while not done:
    # -------------------- CONTROL --------------------

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character.speed[0] = 10
            if event.key == pygame.K_LEFT:
                character.speed[0] = -10
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                character.speed[0] = 0
            if event.key == pygame.K_LEFT:
                character.speed[0] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                character.jump()
        
    # -------------------Game logic----------------------------
    
    # "Camera" scrolls alongside character 
    scroll = character.pos[1] - 470
    
    
    character.move() 
    # check for collision
    for floors in my_List:
        character.checkCollisions(floors)
    character.checkCollisions(beg_Plat)
    
    # if character reaches final platform game ending starts
    if character.pos[1] <= my_List[50].pos[1]:
        ending()
    ## ----------------------------VIEW------------------------------
    # Clear screen
    screen.fill(BLUE)
    # Draw
    
    character.draw_Character()
    beg_Plat.draw()
    
    # Draw each of the randomized platforms from list
    for floors in my_List:
        floors.draw()
    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()