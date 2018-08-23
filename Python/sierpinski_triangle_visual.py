#SierpinskiTriangleVisual.py
#Allen Liu
#August 23, 2018
#A visual representation of a Sierpinski triangle

import pygame
import math

#Lines
triangles = []

#Limit fractal level
level = 0

#Fractal function
def fractal(triangles):
    new_triangles = []
    for triangle in triangles:
        #Important points
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]
        mid_ab = (a[0] + 0.5 * (b[0] - a[0]),  a[1] + 0.5 * (b[1] - a[1]))
        mid_bc = (b[0] + 0.5 * (c[0] - b[0]),  b[1] + 0.5 * (c[1] - b[1]))
        mid_ac = (a[0] + 0.5 * (c[0] - a[0]),  a[1] + 0.5 * (c[1] - a[1]))

        new_triangles.append((a, mid_ab, mid_ac))
        new_triangles.append((b, mid_bc, mid_ab))
        new_triangles.append((c, mid_ac, mid_bc))

    return new_triangles
    

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

#Pygame things
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

done = False;

#Default triangle
triangles.append(([100, 400], [400, 400], [250, 400 - 300 * 0.866]))


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and level < 6:
            triangles = fractal(triangles)
            level += 1
            

    screen.fill(WHITE)

    for triangle in triangles:
        pygame.draw.polygon(screen, BLACK, triangle, 0)
        
    pygame.display.flip()
    
pygame.quit()
