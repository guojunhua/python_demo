import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("UTE.CC 郭君华")
        self.geometry("300x200")


if __name__ == '__main__':
    app = App()
    app.mainloop()
