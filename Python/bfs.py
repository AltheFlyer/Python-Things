#BFS.py
#Allen Liu
#August 17, 2018
#A visual BFS demonstration

import pygame
import pygame.freetype
import math
from datetime import datetime, timedelta

def in_rectangle(point, rect):
    return (point[0] > rect[0] and
            point[0] < rect[0] + rect[2] and
            point[1] > rect[1] and
            point[1] < rect[1] + rect[3])

def bfs():
    #Draws outlines
    def draw_bfs(action):
        cls()
        #Draw pending connections
        for edge in nodes[s]:
            if not edge in visited:
                connection(s, edge, RED)
        for x in visited:
            highlight(x, GREEN)
        #Nodes still in queue have the green overidden
        for x in queue:
            highlight(x, RED)
        #Text:
        if action == "look":
            font.render_to(screen, (20, 440), "Looking at node {}".format(s))
            #Current node highlight override
            highlight(s, BLUE)
        elif action == "add":
            font.render_to(screen, (20, 440), "Added node {}".format(i))
            #Current node highlight override
            highlight(s, BLUE)
        else:
            font.render_to(screen, (20, 440), "Finished")
        draw(False)
    
    queue = []
    queue.append(0)
    
    visited = []
    visited.append(0)

    #Classic bfs, with graphics
    while len(queue) > 0:
        s = queue.pop(0)
        print("Looking at node {}".format(s))
        start_time = datetime.now()
        while (datetime.now() - start_time < timedelta(milliseconds=2000)):
            draw_bfs("look")
            
        for i in nodes[s]:
            if visited.count(i) == 0:
                print("Added {}".format(i))
                start_time = datetime.now()
                queue.append(i)
                visited.append(i)
                while (datetime.now() - start_time < timedelta(milliseconds=2000)):
                    draw_bfs("add")
                
                
    end_time = datetime.now()
    while (datetime.now() - start_time < timedelta(milliseconds=3000)):
        draw_bfs("done")
        
def cls():
    screen.fill(WHITE)
    
def highlight(i, color):
    pygame.draw.circle(screen, color, circles[i], RADIUS + 5)

def connection(a, b, color):
    pygame.draw.line(screen, color, circles[a], circles[b], 3)
    
def draw(do_bfs):
    global selected
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        #On click:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #If node is clicked, 'grab' it
            for circle in circles:
                distance = math.sqrt((pygame.mouse.get_pos()[0] - circle[0]) ** 2 +
                        (pygame.mouse.get_pos()[1] - circle[1]) ** 2)
                if distance <= RADIUS:
                    selected = circles.index(circle)
            #If bfs button is clicked, start bfs
            if do_bfs and in_rectangle(pygame.mouse.get_pos(), (0, 460, 500, 40)):
                bfs()
        #This prevents continuous selection
        elif event.type == pygame.MOUSEBUTTONUP:
            selected = -1

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
    if pygame.mouse.get_pressed() == (1, 0, 0) and pygame.mouse.get_pos()[1] < 460 - RADIUS:
        if selected >= 0:
            circles[selected] = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]

    #BFS button
    if do_bfs and in_rectangle(pygame.mouse.get_pos(), (0, 460, 500, 40)):
        pygame.draw.rect(screen, RED, [0, 460, 500, 40])
    else:
        pygame.draw.rect(screen, (200, 20, 20), [0, 460, 500, 40])
    big_text.render_to(screen, (200, 465), "Start BFS")
    
    pygame.display.flip()
    
nodes = []
circles = []
selected = -1
auto = False

RADIUS = 15;

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Get number of nodes
num_nodes = int(input("Enter the number of nodes.\n"))

#Create nodes
for i in range(num_nodes):
    nodes.append([])

#Create edges
command = ""
while not command == "stop":
    command = input("Type two numbers to connect their nodes, " +
                    "or type 'stop' to end this.\n" +
                    "You may also type 'demo' for a pregenerated graph.\n")
    if command == 'demo':
        #Manual
        num_nodes = 10
        for i in range(num_nodes):
            nodes.append([])
        nodes[0].append(1)
        nodes[1].append(2)
        nodes[1].append(3)
        nodes[2].append(4)
        nodes[2].append(5)
        nodes[3].append(5)
        nodes[3].append(6)
        nodes[4].append(7)
        nodes[7].append(8)
        nodes[9].append(8)
        nodes[6].append(8)
        auto = True
        break
    elif not command == "stop":
        try:
            tokens = command.split()
            #2 way connections
            nodes[int(tokens[0])].append(int(tokens[1]))
            nodes[int(tokens[1])].append(int(tokens[0]))
        except:
            print("invalid input")
print("Prepare for the graph. You may drag the nodes around with the mouse.")

#Generate circle locations
if auto:
    circles.append([40, 230])
    circles.append([125, 230])
    circles.append([210, 153])
    circles.append([210, 306])
    circles.append([295, 115])
    circles.append([295, 230])
    circles.append([295, 345])
    circles.append([380, 163])
    circles.append([380, 296])
    circles.append([465, 296])
else:
    screen_max = int(500 / RADIUS)
    for y in range(int(num_nodes / screen_max) + 1):
        for x in range(screen_max - 1):
            circles.append([RADIUS + x * 2 * RADIUS, RADIUS + y * 2 * RADIUS])

pygame.init()
pygame.freetype.init()

screen = pygame.display.set_mode((500, 500))
font = pygame.freetype.SysFont("calibri", 16)
big_text = pygame.freetype.SysFont("calibri", 32)

pygame.display.set_caption("Graph")


done = False

while not done:
    cls()
    draw(True)

pygame.quit()
pygame.freetype.quit()
