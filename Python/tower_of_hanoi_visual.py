#TowerOfHanoi - Visual.py
#Allen Liu
#August 15, 2018
#########################DESCRIPTION#########################
#A recursive tower of hanoi solver
#Now with geraffics
#############################################################

import pygame
import pygame.freetype
from time import sleep

#Represent each stack:
stacks = []
left = []
middle = []
right = []
stacks.append(left)
stacks.append(middle)
stacks.append(right)

#Where the graphics come in:
pygame.init()
pygame.freetype.init

size = [500, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The wonderful tower.")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

font = pygame.freetype.SysFont("calibri", 16)

#Disks represented by ints
def fill_stack(n):
    for i in range(n, 0, -1):
        left.append(i)

def print_stacks():
    print("{}{}{}".format(left, middle, right))

#Simple move
def move(start, end):
    i = stacks[start].pop()
    stacks[end].append(i)
    print_stacks()
    draw(i, start, end)

#Simple two disk movement
def hanoi_2(start, middle, end):
    move(start, middle)
    move(start, end)
    move(middle, end)

#Hard coding until a pattern is found.
#I have no clue how but ok
def hanoi(start, middle, end, n):
    #1 stack:
    if n == 1:
        move(start, end)
    #2 stack
    if n == 2:
        hanoi_2(start, middle, end)
    #n stack
    elif n > 2:
        #Move all disks except for the largest to the middle
        hanoi(start, end, middle, n - 1)
        #Move largest
        move(start, end)
        #Repeat with the stack in the middle
        hanoi(middle, start, end, n - 1)

def draw(moved, start, end):
    time_ticks = 90
    for time in range(time_ticks):
        pygame.event.get()
        #cls
        screen.fill(WHITE)

        #Description:
        font.render_to(screen, (10, 10), "Moving block {} from stack {} to stack {}.".format(moved, start + 1, end + 1))
        
        #Draw the blocks
        for stack in range(3):
            count = 0
            for i in stacks[stack]:
                if not i == moved:
                    pygame.draw.rect(screen, colors[i - 1], [stack * 175 + (50 - widths[i - 1] / 2), 280 - 20 * count, widths[i - 1], 20], 0)
                    font.render_to(screen, (50 + stack * 175, 280 - 20 * count + 4), str(i))
                    count += 1

        #I don't understand any of this
        #Raise up
        if time < time_ticks / 3:
            start_height = 280 - 20 * (len(stacks[start]))
            new_height = start_height - time * ((start_height - 50) / (time_ticks / 3)) 
            pygame.draw.rect(screen, colors[moved - 1],
                             [start * 175 + (50 - widths[moved - 1] / 2),
                              new_height,
                              widths[moved - 1],
                              20],
                             0)
            font.render_to(screen, (50 + start * 175, new_height + 4), str(moved))
        #Move across
        elif time < 2 * time_ticks / 3:
            height = 50
            x_start = start * 175 + (50 - widths[moved - 1] / 2)
            x_end = end * 175 + (50 - widths[i - 1] / 2)
            x = x_start + (time - (time_ticks / 3)) * ((x_end - x_start) / (time_ticks / 3))
            pygame.draw.rect(screen, colors[moved - 1],
                             [x,
                              height,
                              widths[moved - 1],
                              20],
                             0)
            font.render_to(screen, (x + (widths[moved - 1] / 2), height + 4), str(moved))
        #Drop down
        elif time < time_ticks:
            end_height = 280 - 20 * (len(stacks[end]) - 1)
            new_height = 50 + (time - (2 * time_ticks / 3)) * ((end_height - 50) / (time_ticks / 3))
            pygame.draw.rect(screen, colors[moved - 1],
                             [end * 175 + (50 - widths[moved - 1] / 2),
                              new_height,
                              widths[moved - 1],
                              20],
                             0)
            font.render_to(screen, (end * 175 + 50, new_height + 4), str(moved))
        pygame.display.flip()
        pygame.time.delay(20)

    
a = 10
widths = []
colors = []
#Generate rectangles:
#Generate colors:
for i in range(a):
    widths.append(50 + i * (50 / (a - 1)))
    c = ()
    if i % 3 == 0:
        c = (255 - (50 * int(i / 3)), 0, 0)
    if i % 3 == 1:
        c = (0, 255 - (50 * int(i / 3)), 0)
    if i % 3 == 2:
        c = (0, 0, 255 - (50 * int(i / 3)))
    colors.append(c)

fill_stack(a)
print_stacks()
hanoi(0, 1, 2, a)

done = False
print("Mark 1")

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    #cls
    screen.fill(WHITE)
    font.render_to(screen, (10, 10), "Done")

    #Draw the blocks
    for stack in range(3):
        count = 0
        for i in stacks[stack]:
            pygame.draw.rect(screen, colors[i - 1], [stack * 175 + (50 - widths[i - 1] / 2), 280 - 20 * count, widths[i - 1], 20], 0)
            font.render_to(screen, (50 + stack * 175, 280 - 20 * count + 4), str(i))
            count += 1
    pygame.display.flip()
    
pygame.quit()
pygame.freetype.quit()

