import os
import turtle
from random import random

from PIL import Image


class Canvas:

    def __init__(self, color=None):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        if color:
            self.pen.color(*color)

    @staticmethod
    def with_random_color():
        random_color = [random() for _ in range(3)]
        return Canvas(random_color)

    @property
    def width(self):
        return turtle.window_width()

    @property
    def height(self):
        return turtle.window_height()

    def reset_to(self, point):
        self.pen.clear()
        self.pen.up()
        self.pen.setpos(*point)
        self.pen.down()

    def draw_points(self, points):
        for point in points:
            self.pen.setpos(*point)

    def save_as_png(self, filename):
        """ You'll need to install Ghostscript (https://www.ghostscript.com/)
            to be able to save canvas as an image file."""
        try:
            epsfile = filename + '.eps'
            pngfile = filename + '.png'
            turtle.getcanvas().postscript(file=epsfile)
            Image.open(epsfile).save(pngfile)
            os.remove(epsfile)
        except Exception as e:
            print(f'Failed to save image.\n{e}')
