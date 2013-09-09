# -*- coding: utf-8 -*-
import Image
import ImageDraw
from datetime import datetime

# size of the image
WIDTH = 2000
HEIGHT = 1600
# max iteration/points
MAX_ITER = 500
# plan drawn. reduce values to zoom on mandelbrot set
x_plot = (-3, 1)
y_plot = (-1.5, 1.5)

# init canvas
img = Image.new("RGB", (WIDTH, HEIGHT), "#010204")
draw = ImageDraw.Draw(img)

ratioW = (x_plot[1] - x_plot[0]) / float(WIDTH)
ratioH = (y_plot[1] - y_plot[0]) / float(HEIGHT)

# iteration through each pixels
for j in xrange(0, HEIGHT):
    for i in xrange(0, WIDTH):
        x0, y0 = ratioW * i + x_plot[0], ratioH * j + y_plot[0]

        x = y = 0

        iteration = 0

        while x**2 + y**2 < 4 and iteration < MAX_ITER:
            xtemp = x**2 - y**2 + x0
            y = 2*x*y + y0

            x = xtemp

            iteration += 1

        # choose a color and draw point
        if iteration == MAX_ITER:
            color = 0
        else:
            color = iteration % MAX_ITER

        draw.point((i, j), fill=(color, 0, 0))

    # display percentage of pixels already calculated
    if j % (HEIGHT / 100) == 0:
        print '%d%%' % (j / (HEIGHT / 100))

# save the fractal
now = datetime.now()
filename = now.strftime("%Y-%m-%d-%H:%M:%S") + '_mandelbrot.png'
img.save(filename, "PNG")
