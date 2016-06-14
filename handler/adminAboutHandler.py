# -*- coding:utf-8 -*-
import tornado.web
import json
from adminBaseHandler import AdminBaseHandler

class AdminAboutHandler(AdminBaseHandler):

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        result = {"status": False}
        try:
            result["message"] = self.render_string("admin/about.html")
            result["status"] = True
        except Exception as e:
            print e
            result["message"] = "关于请求错误"
        self.write(json.dumps(result))
        self.finish()
