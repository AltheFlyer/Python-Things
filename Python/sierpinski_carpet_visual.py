#SierpinskiCarpetVisual.py
#Allen Liu
#August 23, 2018
#A visual representation of a Sierpinski Carpet

import pygame
import math

#Lines
squares = []

#Limit fractal level
level = 0

#Fractal function
def fractal(squares):
    new_squares = []
    for square in squares:
        #Important values
        #Lower corner
        min_x = min(square[0][0], square[1][0], square[2][0], square[3][0])
        min_y = min(square[0][1], square[1][1], square[2][1], square[3][1])
        #Upper corner
        max_x = max(square[0][0], square[1][0], square[2][0], square[3][0])
        max_y = max(square[0][1], square[1][1], square[2][1], square[3][1])

        #Thirds
        third_x = (max_x - min_x) / 3
        third_y = (max_y - min_y) / 3

        left_x = min_x + third_x
        right_x = max_x - third_x
        bot_y = min_y + third_y
        top_y = max_y - third_y

        #Squares:
        #Top section
        new_squares.append(([min_x, top_y], [left_x, top_y], [left_x, max_y], [min_x, max_y]))
        new_squares.append(([left_x, top_y], [right_x, top_y], [right_x, max_y], [left_x, max_y]))
        new_squares.append(([right_x, top_y], [max_x, top_y], [max_x, max_y], [right_x, max_y]))
        #Mid section
        new_squares.append(([min_x, bot_y], [left_x, bot_y], [left_x, top_y], [min_x, top_y]))
        #Left out hole
        #new_squares.append(([left_x, top_y], [right_x, top_y], [right_x, max_y], [right_x, max_y]))
        new_squares.append(([right_x, bot_y], [max_x, bot_y], [max_x, top_y], [right_x, top_y]))
        #Bottom section
        new_squares.append(([min_x, min_y], [left_x, min_y], [left_x, bot_y], [min_x, bot_y]))
        new_squares.append(([left_x, min_y], [right_x, min_y], [right_x, bot_y], [left_x, bot_y]))
        new_squares.append(([right_x, min_y], [max_x, min_y], [max_x, bot_y], [right_x, bot_y]))
        
    return new_squares
    

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

#Pygame things
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

done = False;

#Default square
squares.append(([0, 0], [0, 500], [500, 500], [500, 0]))


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and level < 5:
            squares = fractal(squares)
            level += 1
            

    screen.fill(WHITE)

    for square in squares:
        pygame.draw.polygon(screen, BLACK, square, 0)
        
    pygame.display.flip()
    
pygame.quit()
