#GraphDemo.py
#Allen Liu
#August 17, 2018
#A visual graph demonstration

import pygame
import pygame.freetype
import math

nodes = []
circles = []
selected = 0

RADIUS = 15;

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Get number of nodes
num_nodes = int(input("Enter the number of nodes.\n"))

#Create nodes
for i in range(num_nodes):
    nodes.append([])

print(nodes)

#Create edges
command = ""
while not command == "stop":
    command = input("Type two numbers to connect their nodes, " +
                    "or type 'stop' to end this\n")
    if not command == "stop":
        try:
            tokens = command.split()
            #2 way connections
            nodes[int(tokens[0])].append(int(tokens[1]))
            nodes[int(tokens[1])].append(int(tokens[0]))
        except:
            print("invalid input")

print(nodes)

#Generate circle locations
screen_max = int(500 / RADIUS)
for y in range(int(num_nodes / screen_max) + 1):
    for x in range(screen_max - 1):
        circles.append([RADIUS + x * 2 * RADIUS, RADIUS + y * 2 * RADIUS])

pygame.init()
pygame.freetype.init()

screen = pygame.display.set_mode((500, 500))
font = pygame.freetype.SysFont("calibri", 16)

pygame.display.set_caption("Graph")


done = False

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for circle in circles:
                distance = math.sqrt((pygame.mouse.get_pos()[0] - circle[0]) ** 2 +
                        (pygame.mouse.get_pos()[1] - circle[1]) ** 2)
                if distance <= RADIUS:
                    selected = circles.index(circle)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected = -1
            

    #cls
    screen.fill(WHITE)

    #Edges
    for i in range(num_nodes):
        circle = circles[i]   
        for edge in nodes[i]:
            pygame.draw.line(screen, RED, circle, circles[edge], 1)

    #Circles
    for i in range(num_nodes):
        circle = circles[i]
        #Circle
        pygame.draw.circle(screen, BLACK, circle, RADIUS)
        #Text
        font.render_to(screen, (circle[0] - RADIUS / 3, circle[1] - RADIUS / 2), str(i), fgcolor=WHITE)

        
    #If use clicks/holds:
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if selected >= 0:
            circles[selected] = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
        
    pygame.display.flip()

pygame.quit()
pygame.freetype.quit()
