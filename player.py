import pygame 

pygame.init()
 
# displaying a window of height
# 500 and width 400
screen = pygame.display.set_mode((640, 480))
 
# Setting name for window
screen.fill((0,200,200))

plane = pygame.image.load("plane.png")
 
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

    screen.blit(plane, (0,0))

    pygame.display.flip()

