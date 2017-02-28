import os
import random
import uuid
import json

import tornado.ioloop
import tornado.web

from filter import process

class CommentHandler(tornado.web.RequestHandler):
    def post(self):
        name = self.get_argument('name')
        text = self.get_argument('text')

        f = open('comments.json', 'r')
        comments = json.loads(f.read())
        f.close()

        comments.append({"name": name, "text":text})

        f = open('comments.json', 'w')
        f.write(json.dumps(comments))
        f.close()

        self.redirect('/')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        f = open('comments.json', 'r')
        comments = json.loads(f.read())
        f.close()

        self.render('upload.html', comments=comments)
    def post(self):
        fileinfo = self.request.files['image'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open('images/' + cname, 'wb')
        fh.write(fileinfo['body'])

        process('images/' + cname, 'results/' + cname)

        self.render('result.html', name=cname)




settings = [
    ('/', MainHandler),
    ('/addComment', CommentHandler),
    ('/results/(.*)', tornado.web.StaticFileHandler, {'path': 'results'}),
]
app = tornado.web.Application(settings, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()