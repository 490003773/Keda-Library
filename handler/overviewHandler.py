# -*- coding:utf-8 -*-
import tornado.web
from modules import overview
from baseHandler import BaseHandler
import json

class OverviewHandler(BaseHandler):

    @tornado.web.asynchronous
    #@tornado.web.authenticated
    def get(self):
        result = {"status": False}
        try:
            lib_info = overview(self.application.settings["static_path"],\
                                self.application.settings["conf_path"])
            result["message"] = self.render_string("admin/overview.html", \
                                                    **lib_info)
            result["status"] = True
        except Exception as e:
            print e
            result["message"] = "概览请求错误"
        self.write(json.dumps(result))
        self.finish()
