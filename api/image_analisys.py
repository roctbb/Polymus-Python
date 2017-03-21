import requests, json
from PIL import Image,ImageDraw

file = open("faces.jpg", "rb")
content = file.read()

result = requests.post("https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize", data=content,
                       headers={"Content-Type": "application/octet-stream",
                                "Ocp-Apim-Subscription-Key": "ed949f112a524980ad1907524eb7d32d"})
print(result.text)
face_result = json.loads(result.text)
image = Image.open("faces.jpg")
draw = ImageDraw.Draw(image)
for f in face_result:
    face = f["faceRectangle"]
    draw.rectangle([(face["left"], face["top"]), (face["left"]+face["width"], face["top"]+face["height"])])
image.show()