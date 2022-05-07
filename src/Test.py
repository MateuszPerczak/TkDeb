from tkinter import ttk, Tk, StringVar
from TkDeb.TkDeb import Debugger


class TestApp(Tk):
    def __init__(self: Tk) -> Tk:
        super().__init__()
        self.title("Test App")
        self.geometry("500x500")
        # variables
        self.configure(bg='#27ae60')
        self.var = StringVar(value='Debug me!')
        self.text = StringVar(value='Just a sad message')
        self.radio = StringVar(value='Default message')
        self.radio.trace('w', lambda a, b, c: self.update_label())
        # ui
        self.__init_ui()

        self.bind('<F12>', lambda _: Debugger(self))

    def __init_ui(self: Tk) -> None:
        self.style = ttk.Style(self)
        # frame style
        self.style.configure('TFrame', background='#27ae60')
        # label style
        self.style.configure('TLabel', background='#27ae60',
                             font=('Segoe 20 bold'), foreground='#fff')
        self.style.configure(
            'other.TLabel', background='#c0392b', font=('Segoe 12 bold'))
        # button style
        self.style.layout('TButton', [('Button.padding', {
            'sticky': 'nswe', 'children': [('Button.label', {'sticky': 'nswe'})]})])
        self.style.configure('TButton', background='#3498db', font=(
            'Segoe 18 bold'), foreground='#fff', anchor='c', padding=4)
        self.style.map('TButton', background=[('pressed', '!disabled', '#000'), (
            'active', '#2980b9')])

        # radiobutton style
        self.style.layout('TRadiobutton', [('Radiobutton.padding', {
            'sticky': 'nswe', 'children': [('Radiobutton.label', {'sticky': 'nswe'})]})])

        self.style.configure('TRadiobutton', background='#e74c3c', relief='flat', font=(
            'Segoe 12 bold'), foreground='#fff', anchor='c', padding=5)

        self.style.map('TRadiobutton', background=[('pressed', '!disabled', '#000'), (
            'active', '#c0392b'), ('selected', '#c0392b')])
        # ui
        self.frame = ttk.Frame(self)
        center_frame = ttk.Frame(self.frame)
        ttk.Label(center_frame, textvariable=self.var).pack(
            anchor='c', padx=10, pady=10)
        ttk.Button(center_frame, text='Click me', command=self.click).pack(
            anchor='c', padx=10, pady=10)
        center_frame.place(relx=.5, rely=.5, anchor='c')

        bot_frame = ttk.Frame(self.frame)
        radio_frame = ttk.Frame(bot_frame)
        ttk.Radiobutton(radio_frame, text='Page 1', value='This is a about section\nHello world',
                        variable=self.radio).pack(side='left')
        ttk.Radiobutton(radio_frame, text='Page 2',
                        value='Page 2 is the best page\nChange my mind', variable=self.radio).pack(side='left')
        ttk.Radiobutton(radio_frame, text='Page 3',
                        value='Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna run around and desert you\nNever gonna run around and desert you\nNever gonna run around and desert you', variable=self.radio).pack(side='left')

        radio_frame.pack(side='top', fill='x', padx=10, pady=(10, 0))
        ttk.Label(bot_frame, textvariable=self.text,
                  style='other.TLabel').pack(side='top', fill='both', expand=True, padx=10)

        bot_frame.pack(side='bottom', fill='both',
                       padx=10, pady=(10, 0))

        self.frame.pack(fill='both', expand=True, pady=(0, 20))
        self.radio.set('Test2')

    def click(self: Tk) -> None:
        self.var.set('HI!')

        self.after(1000, lambda: self.var.set('Click the button'))

    def update_label(self: Tk) -> None:
        self.text.set(self.radio.get())


class TestWidget(ttk.Frame):
    def __init__(self, parent) -> ttk.Frame:
        super().__init__(parent, name="kupsko")


if __name__ == "__main__":
    TestApp().mainloop()
