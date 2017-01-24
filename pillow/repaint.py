from PIL import Image

im = Image.open("cat.jpg").convert("RGB")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r,g,b = pixels[i,j]

        a = (r+g+b)//3

        if a>180:
            pixels[i,j]=(255,g-40,255)
im.show()
im.save("result.jpg")