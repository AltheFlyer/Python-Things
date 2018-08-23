#AbnormalSelector.py
#Allen Liu
#August 17, 2018
#Using flood fill to select arbitrary areas

import pygame

#Flood fill function
def flood_fill(coord, original_color, new_color):
    queue = []
    x = coord[0]
    y = coord[1]
    queue.append([x, y])
    while len(queue) > 0:
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
        pxArray[x, y] = new_color
        if x > 0 and pxArray[x - 1, y] == original_color:
            queue.append([x - 1, y])
            pxArray[x - 1, y] = new_color
        if x < width - 1 and pxArray[x + 1, y] == original_color:
            queue.append([x + 1, y])
            pxArray[x + 1, y] = new_color
        if y > 0 and pxArray[x, y - 1] == original_color:
            queue.append([x, y - 1])
            pxArray[x, y - 1] = new_color
        if y < height - 1 and pxArray[x , y + 1] == original_color:
            queue.append([x , y + 1])
            pxArray[x , y + 1] = new_color
    
#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
        
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode([width, height])
pxArray = pygame.PixelArray(screen)

done = False

for i in range(20, 300):
    pxArray[i, 20] = GREEN
    pxArray[i, 200] = GREEN

for i in range(20, 200):
    pxArray[20, i] = GREEN
    pxArray[200, i] = GREEN

print(pxArray[50, 50])
flood_fill((50, 50), pxArray[50, 50], RED)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
