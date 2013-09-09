# -*- coding: utf-8 -*-
import Image
import ImageDraw
import math
from datetime import datetime

# each vertices is represented by a tupple (x, y)
# define some params
SIZE = 800
ITERATIONS = 6

BACKGROUND_COLOR = '#020104'
CARPET_COLOR = '#A4B1F2'


# Main function who calculate the sierpinski triangle
# x, y are the coordinates of the carpet
# size are the size of the carpet
# n is the number of remaining iterations
def generate_carpet(x, y, size, n):
    if n > 1:
        subsquare_size = math.ceil(size / 3.0)

        for i in xrange(0, 3):
            for j in xrange(0, 3):
                if i != 1 or j != 1:
                    x0 = x+subsquare_size*i
                    y0 = y+subsquare_size*j
                    generate_carpet(x0, y0, subsquare_size, n-1)
    else:
        canvas.rectangle([x, y, x+size, y+size], fill=CARPET_COLOR)


if __name__ == "__main__":
    # init the canvas
    img = Image.new("RGB", (SIZE, SIZE), BACKGROUND_COLOR)
    canvas = ImageDraw.Draw(img)

    generate_carpet(10, 10, SIZE - 20, ITERATIONS)

    # save the fractal
    now = datetime.now()
    filename = now.strftime("%Y-%m-%d-%H:%M:%S") + '_sierpinski_carpet.png'
    img.save(filename, "PNG")
