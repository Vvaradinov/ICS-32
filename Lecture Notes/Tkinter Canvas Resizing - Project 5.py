# rings.py
#
# ICS 32 Winter 2016
# Code Example
#
# Executing this module displays what we called the "Rings" application,
# which displays a set of ovals (e.g., the Olympic rings) on a "tkinter"
# canvas.
#
# Unlike our previous use of a canvas, however, this one gets larger
# or smaller automatically as the size of the window changes, and the
# image drawn on the canvas is resized accordingly.  Unfortunately,
# "tkinter" doesn't automate this process, so we have to do some work
# to make it happen, but it's not an overwhelming amount of work.
#
# As we'll see in a future code example, building the right tools ahead
# of time will simplify matters even further.  But first thing's first;
# let's understand the problem of resizing a canvas and conceptualize a
# solution to it, then we'll worry about writing it cleanly.

import tkinter


class RingsApplication:
    def __init__(self, rings: [(float, float, float, float)]):
        # First, store the list of ring coordinates in an attribute,
        # so they'll be available to us when we need to draw them.
        self._rings = rings

        # We'll set up the window the same way we set up the previous
        # one.  To make it show up more clearly, though, we'll make
        # the background of our canvas pink, so we can more easily see
        # which part of the window contains our canvas and which part
        # is empty.
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 400,
            background = 'pink')

        # We'll discuss layout more thoroughly in a future lecture and
        # code example.  For now, the idea of what's happening here is
        # this:
        #
        # * The canvas is in grid cell (0, 0), which is the only grid
        #   cell in our window.
        # * As the size of grid cell (0, 0) changes, the size of our
        #   canvas changes accordingly, because it's "stuck" to all
        #   four edges of the cell (north, south, west, and east).
        # * There are 30 pixels of padding (empty space) inside of the
        #   grid cell (0, 0) horizontally and vertically, with the canvas
        #   surrounding by the padding.
        # * As the size of the window changes, all of the added or removed
        #   space is added to (or taken from) the size of grid cell (0, 0).
        #   (That's what the calls to rowconfigure and columnconfigure do;
        #   they set the "weights" on the row and column, which specifies
        #   what proportion of newly-available space should be allocated
        #   to rows and columns in the grid when the size of the window
        #   changes.)

        self._canvas.grid(
            row = 0, column = 0, padx = 30, pady = 30,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resized)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()


    # Because of the call we made to bind() in the __init__ method,
    # this method is called whenever the size of the canvas changes.
    # We respond by calling our own _draw_rings() method to redraw the
    # image, given the new size of the canvas.
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._draw_rings()


    def _draw_rings(self) -> None:
        # Remove all of the shapes currently in the canvas.  (For a fun
        # effect, comment this line out and re-run the program.  Why does
        # it behave differently?)
        self._canvas.delete(tkinter.ALL)

        # Draw the rings.  We always want the size of the rings to be
        # in the same proportions as the size of the canvas, so we're
        # passing "fractional coordinates" instead of "pixel coordinates".
        # When we actually draw ovals on the canvas, we'll convert the
        # fractional coordinates (ranging from 0.0 to 1.0 in the x and y
        # directions) to pixel coordinates (with the range changing as
        # the size of the canvas changes).
        for frac_x1, frac_y1, frac_x2, frac_y2 in self._rings:
            self._draw_ring(frac_x1, frac_y1, frac_x2, frac_y2)


    def _draw_ring(self, frac_x1: float, frac_y1: float, frac_x2: float, frac_y2: float) -> None:
        # Given the fractional coordinates representing the top-left and
        # bottom-right points of the bounding box around the oval we want
        # to draw, draw the corresponding oval.  We have to convert the
        # coordinates from fractional to pixel in order to draw the oval,
        # since Canvas' create_oval() method expects pixel coordinates.
        # We can do that by multiplying the fractional coordinate by the
        # width or height, respectively.

        # Though, first, we'll need to find out how big the canvas is, in
        # terms of pixels.
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        # Now we can do the multiplication and draw the oval.
        self._canvas.create_oval(
            canvas_width * frac_x1, canvas_height * frac_y1,
            canvas_width * frac_x2, canvas_height * frac_y2,
            outline = 'black')



if __name__ == '__main__':
    rings = [
        (.05, .05, .32, .32), (.37, .05, .64, .32), (.69, .05, .96, .32),
        (.19, .19, .46, .46), (.51, .19, .78, .46)
    ]

    app = RingsApplication(rings)
    app.start()