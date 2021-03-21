import PIL.ImageGrab
import os 

ascii_chars = ["@", "#", "S", "%","?", "*", "+", ";", ":", ",", "."]
height = 160

def ascii(image, new_height):
    width, height = image.size
    ratio = height/width/2
    new_width = int(new_height/ratio)
    resized_image = image.resize((new_width, new_height))
    gray_image = resized_image.convert("L")
    pixel_data = gray_image.getdata()
    string = "".join([ascii_chars[pixel//25] for pixel in pixel_data])
    length = len(string)
    ascii_string = "\n".join([string[i:(i+new_width)] for i in range(0, length, new_width)])
    
    return ascii_string
    

while True:
    image = PIL.ImageGrab.grab(bbox=(-1024, 0,0, 768), all_screens=True)
    ascii = ascii(ascii, height)
    print(ascii)     
    os.system('cls')