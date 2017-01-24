from PIL import Image

im = Image.open("cat.jpg").convert("rgb")
im_black = im.copy()
pixels = im.load()
pixels_black = im_black.load()

for i in range(im.width):
    for j in range(im.height):
        r,g,b = pixels[i,j]

        a = (r+g+b)//3
        pixels[i, j] =(a,a,a)

        if a<170:
            pixels_black[i,j]=(0,0,0)
        else:
            pixels_black[i, j] = (255, 200, 200)
im.show()
im.save("result.jpg")
im_black.show()