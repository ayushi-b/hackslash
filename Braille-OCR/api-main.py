# Setting Up
# 1. pip3 install tornado
# 2. python3 api-main.py
# Sample request:- localhost:8000/url/https://abc.com

import tornado.ioloop
import tornado.web
import requests
import cv2
import numpy as np
from main import main


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write(url)

        image_id = self.get_argument("img")
        token = self.get_argument("token")
        ext = self.get_argument("format")
        url = 'https://firebasestorage.googleapis.com/v0/b/hackusit-1eb06.appspot.com/o/'
        url += 'images%2{}.{}?alt=media&token={}'.format(image_id, ext, token)
        print(url)
        url_response = requests.get(url).content
        print(url_response)
        img_array = np.array(bytearray(url_response), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        cv2.imwrite('braille_scan.jpg',img)
        print("TEXT EXTRACTED:- ")
        response = {
            'result': main(),
        }
        self.write(response)
        # return url

# ([A-Z a-z 0-9 . / % " $ & + , : ; = ? @ # | <> . ^ * () % ! - ]+)
if __name__ == "__main__":
    application = tornado.web.Application([
        (r'/url/', MainHandler),
    ])
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
