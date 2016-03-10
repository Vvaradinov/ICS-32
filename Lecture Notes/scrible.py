import tkinter

class ScribbleApp:
    def __init__(self):
        # 1. create widgets
        # 2. set up the layout
        # 3. wire up the event handler

        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master= self._root_window, width = 600,height = 500, background = "#57EX20")
        self._canvas.bind("<Button-1>",self._on_button_down)
        self._canvas.bind("<ButtonRelease-1>", self._on_mouse_move)
        self._canvas.bind("<Motion>",self._on_mouse_move)

        self._canvas.pack()

        self._last_x = 0
        self._last_y = 0
    def _on_button_down(self,event:tkinter.Event) -> None:
        self._on_button_down = True

    def _on_button_up(self,event:tkinter.Event) -> None:
        self._on_button_up = False

    def _on_mouse_move(self,event:tkinter.Event) -> None:
        self._canvas.create_line(self._last_x,self._last_y, event.x, event.y, fill = "black")

        self._last_x = event.x
        self._last_y = event.y

    def start(self):
        self._root_window.mainloop()










if __name__ == "__main__":
    app = ScribbleApp()
    app.start()