#Fractal.py
#Allen Liu
#August 23, 2018
#Collection of fractals
#Code taken from previous fractal visualizations

import math

#Not actually a fractal, but a base for other fractal classes
class Fractal():

    #Generates a fractal up to the nth step
    def generate(self, level, base):
        if level == 0:
            return base
        else:
            values = self.generate(level - 1, base)
            values = self.step(values)
            return values

    #Performs the fractal's step on a given set of input
    def step(self, values):
        new_set = values
        new_set.append(len(set_of_values))
        return new_set

#Uses lines, defined as [([x, y], [a, b]), ...]
class KochQuadratic(Fractal):
    
    def step(self, lines):
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

#Uses lines, defined as [([x, y], [a, b]) , ...]
class KochCurve(Fractal):

    def step(self, lines):
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

            #Finding location of the extruded point
            #Centre point
            centre = (line[0][0] + (line[1][0] - line[0][0]) / 2,
                     line[0][1] + (line[1][1] - line[0][1]) / 2)
            #Length of a third
            third_length = math.sqrt((sub_a[0] - start[0]) ** 2 +
                                     (sub_a[1] - start[1]) ** 2)
            #distance of extruded point to main line, based on 30-60-90 triangle ratio
            top_height = third_length * (math.sqrt(3) / 2)
            #Create the extruded parts
            angle = math.atan2(end[1] - start[1], end[0] - start[0]) - (math.pi / 2)
            top_point = ((centre[0] + top_height * math.cos(angle)),
                         (centre[1] + top_height * math.sin(angle)))

            #Add lines to list
            new_lines.append((start, sub_a))
            new_lines.append((sub_a, top_point))
            new_lines.append((top_point, sub_b))
            new_lines.append((sub_b, end))
            
        return new_lines

#Uses triangles, defined as [([a, b], [c, d], [e, f]), ...]
class SierpinskiTriangle(Fractal):

    def step(self, triangles):
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

#Uses squares (or rectangles) of form [([a, b], [c, d], [e, f], [g, h]), ...]
#In no particular order
class SierpinskiCarpet(Fractal):

    def step(self, squares):
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
