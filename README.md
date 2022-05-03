# PyDeb
Debugger for tkinter application

## Python version:
3.8.2

## Used Libraries:

+ tkinter
+ traceback
+ typing

## Using debugger in tkinter app

```py
from TkDeb import Debugger
from tkinter import Tk

root = Tk()
Debugger(root)
root.mainloop()
```
in class
```py
from TkDeb import Debugger
from tkinter import Tk

class App(Tk):
  def __init__(self):
    super().__init__()
    Debugger(root)
    
if __name__ == '__main__':
  app = App()
  app.mainloop()

```


## Keyboard shortcuts:

+ F2 - extended / normal mode
+ Esc - exit application

## Authors
Main programmer, designer: Mateusz Perczak


## Pictures of application
![Picture of application](https://raw.githubusercontent.com/losek1/PyDeb/master/images/app.jpg)
