import pygame 

pygame.init()
 
# displaying a window of height
# 500 and width 400
screen = pygame.display.set_mode((640, 700))
 
# Setting name for window
screen.fill((0,200,200))

plane = pygame.image.load("plane.png")
plane = pygame.transform.flip(plane, False, True)
plane = pygame.transform.scale(plane, (100, 100))



class enemyPlane:

    def __init__(self, x_coordinate, y_coordinate, health, speed):
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.flip(plane, False, True)
        self.image = pygame.transform.scale(plane, (100, 100))

enemy = enemyPlane(100, 100, 1000, 5)



 
# creating a bool value which checks 
# if game is running
running = True

 
# Game loop
# keep game running till running is true
while running:
   
    # Check for event if user has pushed 
    # any event in queue
    for event in pygame.event.get():


        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    screen.blit(enemy.image, (0,0))

    pygame.display.flip()

