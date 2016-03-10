import tkinter

class RingsApp:
    def __init__(self,rings: [(float,float,float,float)]):
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 700, height = 600,
            background = "red")
        self._canvas.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind("<Configure>",self._on_canvas_resize)


        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


        self._canvas.create_oval(100,120,400,530,outline = "black",fill = "white")



    def start(self):
        self._root_window.mainloop()


    def _on_canvas_resize(self,event: tkinter.Event):
        """
        """
        print("Canvas got resized")

    def draw_rings(self,event:tkinter.Event):
        pass




if __name__ == "__main__":
    app = RingsApp([(0.1,0.1,0.2,0.2),(0.5,0.3,0.7,0.4),(0.85,0.15,0.87,0.2)])
    app.start()

