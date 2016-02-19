import tkinter

window = tkinter.Tk()
# a TK object represents the "root window" of your application

window.mainloop()

# tkinter offers us a model called "even-base programming"
# you put tkinter fully in charge when you call mainloop()
# tkinter handles input events of various kinds automatically
# you register an interest in some of those events, and specify
# which of your functions/methods should be called when those events take place

# 1. Widgets -- widgets when you create them they have options
# 2. Layout
# 3. Event Handlers
def on_button_pressed():
    print("Hello")

def on_mouse_entered_button(event: tkinter.Event):
    event.widget["text"] = "In button"

def on_mouse_exited_button(event: tkinter.Event):
    event.widget["text"] = "Out of button"


if __name__ == "__main__":
    root_window = tkinter.Tk()

    button = tkinter.Button(
        master= root_window, text= "HELLO", font = ("Helvetica",24),command = on_button_pressed)

    button.bind("<Enter>", on_mouse_entered_button)
    button.bind("<Leave>", on_mouse_exited_button)
    button.pack()

    root_window.mainloop()