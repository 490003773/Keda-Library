# -*- coding:utf-8 -*-
import tornado.web
from modules import VerifyCode
import json
import os

class VerifyCodeHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        vpath = self.application.settings["static_path"]
        verifycode = VerifyCode(os.path.join(vpath, "img/verifycode"))
        self.set_secure_cookie("verifycode", verifycode.strs.upper())
        print verifycode
        self.write(json.dumps(verifycode.name))
        self.finish()
