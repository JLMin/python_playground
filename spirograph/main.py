from datetime import datetime

from Canvas import Canvas
from Spirograph import Spirograph


if __name__ == '__main__':

    canvas = Canvas.with_random_color()

    max_size = min(canvas.width, canvas.height)
    spiro = Spirograph.with_random_size(max_size)

    canvas.reset_to(spiro.start_pos())
    canvas.draw_points(spiro.gen_pos())

    filename = 'spirograph_' + datetime.now().strftime("%Y%m%d_%H%M%S")
    canvas.save_as_png(filename)
