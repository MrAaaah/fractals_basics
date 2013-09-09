# -*- coding: utf-8 -*-
import Image
import ImageDraw
from datetime import datetime

# each vertices is represented by a tupple (x, y)
# define some params
WIDTH = HEIGHT = 800
ITERATIONS = 7

# vertices of the sierpinski triangle
A = (400, 68)
B = (10, 760)
C = (790, 760)

BACKGROUND_COLOR = '#020104'
TRIANGLE_COLOR = '#A4B1F2'


# return the cordinates of the middle of the segment [ab]
def middle_of_segment(a, b):
    return ((a[0]+b[0])/2, (a[1]+b[1])/2)


# draw a triangle abc
def draw_triangle(a, b, c, color):
    canvas.polygon([a, b, c], fill=color)


# Main function who calculate the sierpinski triangle
# a, b and c are the vertices of the triangle
# n is the number of remaining iterations
def generate_triangle(a, b, c, n):
    if n > 1:
        # calculate the middle of each segments
        p1 = middle_of_segment(a, b)
        p2 = middle_of_segment(a, c)
        p3 = middle_of_segment(b, c)

        # repeat the process for each subtriangle
        generate_triangle(a, p1, p2, n-1)
        generate_triangle(b, p1, p3, n-1)
        generate_triangle(c, p2, p3, n-1)
    else:
        draw_triangle(a, b, c, TRIANGLE_COLOR)


if __name__ == "__main__":
    # init the canvas
    img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND_COLOR)
    canvas = ImageDraw.Draw(img)

    generate_triangle(A, B, C, ITERATIONS)

    # save the fractal
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H:%M:%S") + '_sierpinski_triangle.png'
    img.save(filename, "PNG")
