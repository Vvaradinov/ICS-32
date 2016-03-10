# spots_gui.py
#
# ICS 32 Winter 2016
# Code Example
#
# This module implements a tkinter-based GUI application called Spots.
# The application begins with a blank canvas.  Clicking on the canvas
# causes a yellow "spot" to be drawn on the canvas.  Clicking within an
# existing spot instead causes that spot to be removed.  The spots get
# larger or smaller as the window is resized; they always cover a
# constant percentage of the canvas' area.

import point
import spots_model
import tkinter


class SpotsApplication:
    def __init__(self, state: spots_model.SpotsState):
        self._state = state

        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#006000')

        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self) -> None:
        self._root_window.mainloop()


    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        # Whenever the Canvas' size changes, redraw all of the spots,
        # since their sizes have changed, too.
        self._redraw_all_spots()


    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        # When the canvas is clicked, tkinter generates an event.  Since
        # we've bound to this method to that event, this method will be
        # called whenever the canvas is clicked.  The event object passed
        # to this method will have two useful attributes:
        #
        # * event.x, which specifies the x-coordinate where the click
        #   occurred
        # * event.y, which specifies the y-coordinate where the click
        #   occurred
        #
        # tkinter is not aware of the concept of fractional coordinates.
        # It always returns pixel coordinates.  But that's okay,
        # because we can simply create a Point object and let it
        # do the appropriate conversion for us.
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_point = point.from_pixel(
            event.x, event.y, width, height)

        # Ask the SpotsState object to handle the click, by either
        # adding or removing a spot.
        self._state.handle_click(click_point)

        # Now that a spot has either been added or removed, redraw
        # the dots.
        self._redraw_all_spots()


    def _redraw_all_spots(self) -> None:
        # Delete and redraw all of the spots.  Since spots are represented
        # by Spot objects that contain a Point object representing the
        # center of the spot, we'll need to do some work here to figure out
        # the top-left and bottom-right corners of the bounding box around
        # the oval we need to draw.  But since this is purely a matter of
        # "what it looks like" (i.e., a "view" problem, not a "model"
        # problem), that code belongs here in the user interface.

        self._canvas.delete(tkinter.ALL)

        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        for spot in self._state.all_spots():
            center_x, center_y = spot.center().pixel(canvas_width, canvas_height)

            radius_x = spot.radius_frac() * canvas_width
            radius_y = spot.radius_frac() * canvas_height

            self._canvas.create_oval(
                center_x - radius_x, center_y - radius_y,
                center_x + radius_x, center_y + radius_y,
                fill = '#ffff00', outline = '#000000')



if __name__ == '__main__':
    # Create a SpotsState object that will store the current state of the
    # Spots application as it runs, then pass it to a newly-created
    # SpotsApplication, and finally start the application.  Note how
    # we can nest expressions like this when we don't need to reuse their
    # results more than once.
    SpotsApplication(spots_model.SpotsState()).start()