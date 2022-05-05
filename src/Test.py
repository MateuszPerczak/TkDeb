from tkinter import ttk, Tk, StringVar
from TkDeb.TkDeb import Debugger


class TestApp(Tk):
    def __init__(self: Tk) -> Tk:
        super().__init__()
        self.title("Test App")
        self.geometry("300x300")
        # variables
        self.configure(bg='#aaa')
        self.var = StringVar(value="Click the button")
        # ui
        self.__init_ui()

        self.bind('<F12>', lambda e: Debugger(self))

    def __init_ui(self: Tk) -> None:
        frame = ttk.Frame(self)

        center_frame = ttk.Frame(frame)
        ttk.Label(center_frame, textvariable=self.var, style='my.TLabel').pack(
            anchor='c', padx=10, pady=10)
        ttk.Button(center_frame, text='Click me', command=self.click).pack(
            anchor='c', padx=10, pady=10)

        center_frame.place(relx=.5, rely=.5, anchor='c')

        frame.pack(fill='both', expand=True)

    def click(self: Tk) -> None:
        self.var.set('clicked')

        self.after(1000, lambda: self.var.set('Click the button'))


class TestWidget(ttk.Frame):
    def __init__(self, parent) -> ttk.Frame:
        super().__init__(parent, name="kupsko")


if __name__ == "__main__":
    TestApp().mainloop()
