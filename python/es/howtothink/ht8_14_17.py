"""remove red from an image"""
#** pip install cImage **
import image

img = image.Image(r"python\es\howtothink\doge.png")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
#img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        #set red channel to 0
        NEWRED = 0
        newgreen = p.getGreen()
        newblue = p.getBlue()

        newpixel = image.Pixel(NEWRED, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()
