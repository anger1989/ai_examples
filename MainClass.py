import tkinter
import configparser
import Zwitter

conf = configparser.RawConfigParser()
conf.read("config.cfg")
life = False  # global
root = tkinter.Tk()
zwitter = Zwitter.Zwitter()

WIDTH = conf.get("window", "width")
HEIGHT = conf.get("window", "height")
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
x = 20
y = 50
root.title('Zwitter field')
canvas.grid()
canvas.focus_set()




def lifecycle(life):
        zwitter.breath(life)
        BODY_SIZE = zwitter.body
        BODY_COLOR = zwitter.color
        canvas.create_rectangle(x, y, x + BODY_SIZE, y + BODY_SIZE, fill=BODY_COLOR)


def _start():
    print('ok')
    lifecycle(life)
    root.mainloop()



if __name__ == '__main__':
    _start()


