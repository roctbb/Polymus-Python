from PIL import Image

im = Image.open("cat.jpg").convert("RGB") # преобразование в RGB
pixels = im.load()

for i in range(im.width):  # i по ширине
    for j in range(im.height):  # j по высоте
        r, g, b = pixels[i, j]  # кортеж (r,g,b) автоматически раскладывается по переменным слева от присваивания
        # инвертируем
        r = 255 - r
        g = 255 - g
        b = 255 - b
        # добавляем красного
        r = min(255, r + 150)
        pixels[i, j] = (r, g, b)
im.show()
im.save("result.jpg")
