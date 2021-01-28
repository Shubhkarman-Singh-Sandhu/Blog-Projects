import pyglet as pt
import random as r
import matplotlib.pyplot as plt
import numpy as np

window = pt.window.Window(500, 500, "Evolving Colors", True)
window.set_fullscreen(True)
batch = pt.graphics.Batch()

time = datetime.datetime.now().strftime("%X")
background = pt.shapes.Rectangle(0, 0, window.width, window.height, batch=batch)
colorsTuple = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
colors = list(colorsTuple)
background.color = colorsTuple

red = []
green = []
blue = []
improved = [[], [], []]
colorVals = [red, green, blue]
index = 10
timeFactor = 60
loopIndex = 5000
def update(dt):
    global improved, colors, index
    if len(improved[0]) == 0:
        for j in range(loopIndex):
            for i in range(len(colors)):
                if colors[i] >= (255-index):
                    colors[i] -= r.randint(0, index)
                elif colors[i] <= index:
                    colors[i] += r.randint(0, index)
                else:
                    colors[i] += r.randint((-1 * index), index)
                colorVals[i].append(colors[i]) 
        x = np.linspace(0, len(colorVals[0]), num=len(colorVals[0]))
        improvedRed = np.poly1d(np.polyfit(x, colorVals[0], 3))
        improvedGreen = np.poly1d(np.polyfit(x, colorVals[1], 3))
        improvedBlue = np.poly1d(np.poly1d(np.polyfit(x, colorVals[2], 3)))

        redRaw = plt.plot(x, improvedRed(x), c="red")
        greenRaw = plt.plot(x, improvedGreen(x), c="red")
        blueRaw = plt.plot(x, improvedBlue(x), c="red")

        red = redRaw[0].get_ydata()
        green = greenRaw[0].get_ydata()
        blue = blueRaw[0].get_ydata()
        
        red = red.tolist()
        green = green.tolist()
        blue = blue.tolist()
        improved = [red, green, blue]

    colors = [improved[0][0], improved[1][0], improved[2][0]]
    colorsTuple = tuple(colors)
    background.color = colorsTuple

    improved[0].pop(0)
    improved[1].pop(0)
    improved[2].pop(0)

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
