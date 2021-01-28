import pyglet as pt
import random as r
import matplotlib.pyplot as plt, numpy as np

window = pt.window.Window(500, 500, "Evolving Colors", True)
#window.set_fullscreen(True)
batch = pt.graphics.Batch()

background = pt.shapes.Rectangle(0, 0, window.width, window.height, batch=batch)

colorsTuple = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
colors = list(colorsTuple)
background.color = colorsTuple

red = []
green = []
blue = []
colorVals = [red, green, blue]
index = 1
timeFactor = 60
def update(dt): 
    for i in range(len(colors)):
        if colors[i] >= (255-index):
            colors[i] -= r.randint(0, index)
        elif colors[i] <= index:
            colors[i] += r.randint(0, index)
        else:
            colors[i] += r.randint((-1 * index), index)

        colorVals[i].append(colors[i]) 
    colorsTuple = tuple(colors)
    background.color = colorsTuple

@window.event
def on_close():
    window.close()
    x = np.linspace(0, len(colorVals[0]), num=len(colorVals[0]))
    plt.axis([0, 6000, 0, 255])
    plt.plot(x, colorVals[0], c="red")
    plt.plot(x, colorVals[1], c="green")
    plt.plot(x, colorVals[2], c="blue")
    title = "Value of each RGB color with the index as " + str(index)
    plt.title(title)
    plt.show()

pt.clock.schedule_interval(update, 1/timeFactor)
@window.event
def on_resize(width, height):
    background.width = window.width
    background.height = window.height 
@window.event
def on_draw():
    window.clear()
    batch.draw()

pt.app.run()
