import requests, json
from PIL import Image,ImageDraw

file = open("image1.jpg", "rb")
content = file.read()

result = requests.post("https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize", data=content,
                       headers={"Content-Type": "application/octet-stream",
                                "Ocp-Apim-Subscription-Key": "YOUR_KEY"})
print(result.text)
face_result = json.loads(result.text)
for f in face_result:
    face = f["faceRectangle"]
    image = Image.open("image1.jpg")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(face["left"], face["top"]), (face["left"]+face["width"], face["top"]+face["height"])])
image.show()