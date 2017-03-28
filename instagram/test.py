import requests, json

#https://oauth.vk.com/authorize?client_id=5718188&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token

x = 55.75987904604878
y = 37.618592977523804

token = ""

result = requests.get("https://api.vk.com/method/photos.search?lat={0}&long={1}&v=5.63&access_token=".format(x,y,token))

d = json.loads(result.text)

for photo in d["response"]["items"]:
    try:
        print(photo["photo_604"])
    except:
        pass

print(d)