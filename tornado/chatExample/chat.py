import tornado.ioloop
import tornado.web
import random
from pymongo import MongoClient

connection = MongoClient("mongodb://user:password@ds061325.mlab.com:61325/chat")
db = connection['chat']

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        if self.get_current_user() == None:
            self.redirect('/login')
            return
        messages = db['messages'].find()

        self.render('chat.html', messages=messages)
    def post(self):
        text = self.get_argument("message", "")
        user = self.get_current_user()

        message = {"text":text, "user": user}

        db['messages'].insert_one(message)

        self.redirect('/')



class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")

app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")
app.listen(8888)
tornado.ioloop.IOLoop.current().start()