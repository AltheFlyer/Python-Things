#Bezier.py
#Allen Liu
#August 18, 2018
#A representation of how a bezier curve may be drawn

import pygame
import math

#Ordered list of ordered (x, y) pairs
anchors = []
curve = []
selected = -1

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
POINT_MAX = 101 #0 to 100%

#Only expects 2 points
def get_inter_point(points, percent):
    percent *= 0.01
    start_x = points[0][0]
    start_y = points[0][1]
    end_x = points[1][0]
    end_y = points[1][1]
    a = start_x + percent * (end_x - start_x)
    b = start_y + percent * (end_y - start_y)
    return (a, b)
    
def bezier_default(points, percent):
    start_x = points[0][0]
    start_y = points[0][1]
    mid_x = points[1][0]
    mid_y = points[1][1]
    end_x = points[2][0]
    end_y = points[2][1]
    #Draw the intermediary line
    first = get_inter_point([(start_x, start_y), (mid_x, mid_y)], percent)
    last = get_inter_point([(mid_x, mid_y), (end_x, end_y)], percent)
    pygame.draw.line(screen, BLACK, first, last, 1)
    x = int(get_inter_point([first, last], percent)[0])
    y = int(get_inter_point([first, last], percent)[1])
    #Where the next point in the curve is
    pygame.draw.circle(screen, BLUE, (x, y), 5)
    #Add the point in the curve
    if len(curve) < POINT_MAX:
        curve.append((x, y))

def bezier(points, percent):
    color = 255 - (255 / (len(points) - 2))
    #Draw lines
    pygame.draw.lines(screen, (color, color, color), False, points, int(len(points) / 2))
    #Draw generated anchors
    #Controllable anchors are made to appear differently
    if len(points) < len(anchors):
        for anchor in points:
            pygame.draw.circle(screen, BLACK, (int(anchor[0]), int(anchor[1])), len(points))
    if len(points) == 3:
        bezier_default(points, percent)
    else:
        new_points = []
        for i in range(len(points)):
            if not i == len(points) - 1:
                new_points.append(get_inter_point([
                    (points[i][0], points[i][1]),
                    (points[i + 1][0], points[i + 1][1])], percent))
        
        bezier(new_points, percent)

pygame.init()

height = 500
width = 500
screen = pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()
count = 0

#Initialize points:
##anchors.append((10, 450))
##anchors.append((10, 200))
##anchors.append((100, 10))
##anchors.append((300, 10))
##anchors.append((400, 200))
##anchors.append((400, 450))
anchors.append((10, 10))
anchors.append((240, 10))
anchors.append((240, 490))
anchors.append((490, 490))

while not done:

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                curve = []
                count = 0
                selected = -2
                for circle in anchors:
                    d = math.sqrt((pygame.mouse.get_pos()[0] - circle[0]) ** 2 +
                            (pygame.mouse.get_pos()[1] - circle[1]) ** 2)
                    if d < 10:
                        selected = anchors.index(circle)
                #Add anchor
                if selected == -2:
                    anchors.append(pygame.mouse.get_pos())
                    selected = len(anchors) - 1
            #Delete anchor with right-click
            elif pygame.mouse.get_pressed() == (0, 0, 1) and len(anchors) > 3:
                curve = []
                count = 0
                selected = -2
                for circle in anchors:
                    d = math.sqrt((pygame.mouse.get_pos()[0] - circle[0]) ** 2 +
                            (pygame.mouse.get_pos()[1] - circle[1]) ** 2)
                    if d < 10:
                        selected = anchors.index(circle)
                if not selected == -2:
                    del(anchors[selected])
        elif event.type == pygame.MOUSEBUTTONUP:
            curve = []
            count = 0
            selected = -1

    #Dragging anchors
    if pygame.mouse.get_pressed() == (1, 0, 0) and selected > -1:
        anchors[selected] = pygame.mouse.get_pos()
    
    screen.fill(WHITE)
    
    #Tick through bezier curve
    bezier(anchors, count)
    if count < POINT_MAX - 1:
        count += 1
    else:
        count = 0

    for anchor in anchors:
        pygame.draw.circle(screen, GREEN, anchor, 10)

        #Draws the curve
    for i in range(len(curve)):
        pygame.draw.circle(screen, RED, curve[i], 2)
    if len(curve) > 1:
        pygame.draw.lines(screen, RED, False, curve, 4)
            

    pygame.display.flip()
    
pygame.quit()
    
