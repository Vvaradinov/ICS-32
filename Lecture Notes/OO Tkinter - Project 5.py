# scribble.py
#
# ICS 32 Winter 2016
# Code Example
#
# This is an application that I'm calling Scribble, which is a demonstration
# that embraces the use of classes and object-oriented programming, a
# technique that makes the design of our GUIs clearer and simpler.
#
# The general design of this example revolves around a class called
# ScribbleApplication.  A ScribbleApplication object represents a single
# instance of our Scribble application: a "root window" that contains a
# canvas on which a user can draw by clicking the primary mouse button
# and dragging the mouse across the canvas.
#
# There isn't a lot of code here, but there are some important design
# lessons that will show up again in later examples.
#
# * Using a class to represent an application (or, as we'll see later,
#   to represent portions of our application) is a very handy way to
#   make all of the necessary data in our application available to
#   event handlers, by making sure that event handlers are methods that
#   are called on our application object.
#
# * When there are values we need to remember between events, we need
#   to store those values somewhere.  In the case of our Scribble
#   application, we handle events that specify mouse motion and want to
#   draw another little line every time motion occurs.  Each line connects
#   the previous position to the current one.  This requires us to remember,
#   when a mouse motion event occurs, what the previous position was.
#   Part of what makes classes so useful in implement GUIs is that they
#   provide a good place to store this kind of data: into the attributes
#   of "self"!
#
# * The event handlers, instead of being functions, are methods in our
#   class.  This requires binding the events to "bound methods" instead
#   of functions.


import tkinter



# Try changing these colors.  Each is specified as a '#' character
# followed by three two-hexadecimal-digit amounts, which respectively
# specify an amount of red, green, and blue that should be mixed to
# generate the color.  Try these and see if you can understand why they
# turn out the way they do:
#
#     '#FF0000'
#     '#00FF00'
#     '#0000FF'
#     '#000080'
#     '#FFFFFF'
#     '#000000'
#     '#FFFF00'

_BACKGROUND_COLOR = '#FFFFFF'
_LINE_COLOR = '#008000'



class ScribbleApplication:
    def __init__(self):
        '''
        Initializes a new Scribble application by creating a window and
        placing a Canvas widget inside of it.  However, the application
        does not execute until its start() method is called.
        '''

        self._root_window = tkinter.Tk()

        self._scribble_canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 400,
            background = _BACKGROUND_COLOR)

        # Bind the event that occurs when the first mouse button is
        # clicked within the canvas.  The event handler is a "bound
        # method", meaning that tkinter will call the _on_button_down
        # method on the self object for us, and also pass it an event
        # object as an additional argument.
        self._scribble_canvas.bind('<Button-1>', self._on_button_down)

        # Also bind the event that occurs when the first mouse button
        # is released.  This allows us to know we should stop drawing
        # when the mouse subsequently moves.
        self._scribble_canvas.bind('<ButtonRelease-1>', self._on_button_up)

        # Bind the event that occurs when mouse motion occurs within
        # the canvas.
        self._scribble_canvas.bind('<Motion>', self._on_mouse_moved)

        # Since the canvas is the only thing in our window, we'll just
        # call pack() to resize the window's area to exactly fit our
        # canvas (which we asked to be 500x400).
        self._scribble_canvas.pack()

        # Set the initial state of our application.  At any given time,
        # we'll keep track of whether the mouse button is down, as
        # well as the most recent place the mouse has been (which we'll
        # use when we're drawing lines).
        self._button_is_down = False
        self._last_x = 0
        self._last_y = 0


    def start(self) -> None:
        '''
        Starts the Scribble application.  Note that this method will not
        return until the Scribble application's window is closed.
        '''

        # Starting the application is to simply call mainloop() on our
        # root window.  That will turn control over to tkinter; our
        # event handlers will be called when the interesting events
        # happen, but things are otherwise out of our hands until the
        # window is closed.
        self._root_window.mainloop()


    def _on_button_down(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is down within the canvas.
        '''

        # Remember that the click happened, so we'll know that the
        # button is down.  This will tell us whether to draw when
        # there is mouse motion.
        self._button_is_down = True

        # Remember where this click happened, so subsequent movement
        # can draw a line starting where the initial click was made.
        self._last_x = event.x
        self._last_y = event.y


    def _on_button_up(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when the primary mouse button
        is up within the canvas.
        '''

        # Track that the button is now up.
        self._button_is_down = False


    def _on_mouse_moved(self, event: tkinter.Event) -> None:
        '''
        Event handler that is called when there is mouse motion within
        the canvas.
        '''

        # Every time motion is detected and the button is down, we
        # draw a line from the last known place where the mouse was
        # to where the mouse is now.
        #
        # The event object includes two attributes, x and y, that
        # specify the x- and y-coordinate where the mouse is now.
        #
        # The create_line() method takes four arguments (specifying the
        # x- and y-coordinate where the line should start and the x- and
        # y-coordinate where it should end), plus additional keyword
        # arguments (in our case, the "fill" argument, which specifies the
        # color of the line that is to be drawn).

        if self._button_is_down:
            self._scribble_canvas.create_line(
                self._last_x, self._last_y, event.x, event.y,
                fill = _LINE_COLOR)

            # Now we want to remember our new position, so any subsequent
            # motion will draw a line from this point to the new position.
            # (For fun, remove these two lines and see what happens when
            # you run the program.)
            self._last_x = event.x
            self._last_y = event.y



if __name__ == '__main__':
    # Create a ScribbleApplication and start it
    app = ScribbleApplication()
    app.start()