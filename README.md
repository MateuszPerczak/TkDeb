# PyDeb

TkDeb is a simple debugger for the Tkinter application with allows you to see all widgets properties without needing to print them in your python code!

## Python version:

3.8.2

## Used Libraries:

- tkinter
- typing
- os

## Using debugger in tkinter app

```py
from TkDeb.TkDeb import Debugger
from tkinter import Tk

root = Tk()
Debugger(root)
root.mainloop()
```

## Or using class

```py
from TkDeb.TkDeb import Debugger
from tkinter import Tk

class App(Tk):
    def __init__(self):
        super().__init__()
        Debugger(self)
```

## Keyboard shortcuts:

- Esc - exit application

## Authors

Main programmer, designer: Mateusz Perczak

## Pictures of application

![Picture of application](https://raw.githubusercontent.com/losek1/PyDeb/master/images/app.jpg)

## Icons

Icons: [icons8](https://icons8.com/)
