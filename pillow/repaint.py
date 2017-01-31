from PIL import Image

im = Image.open("cat.jpg").convert("RGB") # преобразование в RGB
pixels = im.load()

for i in range(im.width):  # i по ширине
    for j in range(im.height):  # j по высоте
        r, g, b = pixels[i, j]

        a = (r + g + b) // 3 # a - яркость пикселя

        if a > 180:
            pixels[i, j] = (255, g - 40, 255)
im.show()
im.save("result.jpg")
