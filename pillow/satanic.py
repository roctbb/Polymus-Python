from PIL import Image

im = Image.open("cat.jpg")
pixels = im.load()

for i in range(im.width):
    for j in range(im.height):
        r,g,b = pixels[i,j]
        # инвертируем
        r = 255 - r
        g = 255 - g
        b = 255 - b
        # добавляем красного
        r = min(255, r + 150)
        pixels[i, j] = (r,g,b)
im.show()
im.save("result.jpg")