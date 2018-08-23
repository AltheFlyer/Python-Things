#KochQuadraticVisual.py
#Allen Liu
#August 23, 2018
#A visual representation of a quadratic Koch fractal

import pygame
import math

#Lines
lines = []

#Limit fractal level
level = 0

#Fractal function
def fractal(lines):
    new_lines = []
    for line in lines:
        #Important points
        #Start and end
        start = (line[0][0], line[0][1])
        end = (line[1][0], line[1][1])
        #Thirds
        sub_a = (line[0][0] + (line[1][0] - line[0][0]) / 3,
                 line[0][1] + (line[1][1] - line[0][1]) / 3)
        sub_b = (line[0][0] + (2 * (line[1][0] - line[0][0])) / 3,
                 line[0][1] + (2 * (line[1][1] - line[0][1])) / 3)

        #Find extruded points
        third_length = math.sqrt((sub_a[0] - start[0]) ** 2 +
                                 (sub_a[1] - start[1]) ** 2)
        angle = (math.atan2(end[1] - start[1], end[0] - start[0]) -
                 (math.pi / 2))
        top_a = (sub_a[0] + third_length * math.cos(angle),
                 sub_a[1] + third_length * math.sin(angle))
        top_b = (sub_b[0] + third_length * math.cos(angle),
                 sub_b[1] + third_length * math.sin(angle))
        new_lines.append((start, sub_a))
        new_lines.append((sub_a, top_a))
        new_lines.append((top_a, top_b))
        new_lines.append((top_b, sub_b))
        new_lines.append((sub_b, end))
        
    return new_lines
    

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

#Pygame things
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

done = False;

#Default line
lines.append(([0, 490], [500, 490]))


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and level < 5:
            lines = fractal(lines)
            level += 1
            

    screen.fill(WHITE)

    for line in lines:
        pygame.draw.line(screen, BLACK, line[0], line[1], 1)
        
    pygame.display.flip()
    
pygame.quit()
