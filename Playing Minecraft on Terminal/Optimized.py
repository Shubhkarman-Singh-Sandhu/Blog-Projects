import PIL.ImageGrab
import os 

a = ["@", "#", "S", "%","?", "*", "+", ";", ":", ",", "."]
n = 160
while True:
    i = PIL.ImageGrab.grab(bbox=(-1024, 0,0, 768), all_screens=True)
    w, h = i.size
    r = h/w/2
    u = int(n/r)
    p = i.resize((u, n)).convert("L").getdata()
    c = "".join([a[o//25] for o in p])
    l = len(c)
    print("\n".join([c[j:(j+u)] for j in range(0, l, u)]))

     
    os.system('cls')