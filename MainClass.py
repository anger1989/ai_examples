import tkinter
import configparser
import Zwitter
conf = configparser.RawConfigParser()
conf.read("config.cfg")

root = tkinter.Tk()
zwitter = Zwitter.Zwitter()

root.title('Zwitter field')

WIDTH = conf.get("window","width")
HEIGHT = conf.get("window", "height")
#BODY_SIZE = conf.get("zwitterbody", "size")
x = 20
y = 50
canvas = tkinter.Canvas(root,width=WIDTH, height=HEIGHT, bg="#003300")

BODY_SIZE = zwitter.body
canvas.grid()
canvas.focus_set()

canvas.create_rectangle(x,y,x+BODY_SIZE,y+BODY_SIZE,fill="white")

print(WIDTH,HEIGHT)

root.mainloop()