# Setting Up
# 1. pip3 install tornado
# 2. python3 api-main.py
# Sample request:- localhost:8000/url/https://abc.com

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,url):
        self.write(url)
        # return url

if __name__ == "__main__":
    application = tornado.web.Application([
        (r'/url/([A-Z a-z 0-9 . / % " $ & + , : ; = ? @ # | <> . ^ * () % ! - ]+)', MainHandler),
    ])
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
