"""apply sepia fitler to an image"""
#** pip install cImage **
import image

def sepia(r,g,b):
    """sepia filter"""
    newr = int(r * 0.393 + g * 0.769 + b * 0.189)
    newg = int(r * 0.349 + g * 0.686 + b * 0.168)
    newb = int(r * 0.272 + g * 0.534 + b * 0.131)
    #check value <256
    for i in [newr, newg, newb]:
        i= min(i, 255)
        #print(i, sep="-", end=" ")
    #print("\n")
    #print(newr, newg, newb, sep="-", end=" ")

    return newr, newg, newb

img = image.Image(r"python\es\howtothink\doge.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
#img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        newred, newgreen, newblue = sepia(red, green, blue)
        #!! fix value > 255
        try:
            newpixel = image.Pixel(newred, newgreen, newblue)
        except ValueError:
            newpixel = image.Pixel(255, 255, 255)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
