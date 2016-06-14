# -*- coding:utf-8 -*-
import tornado.web
import json

class AdminExitHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        result = {"status": True}
        self.set_secure_cookie("admin", "")
        self.set_secure_cookie("verifycode", "")
        self.set_secure_cookie("curpage", "")
        result["message"] = self.render_string("admin/exit.html")
        self.write(json.dumps(result))
        self.finish()
