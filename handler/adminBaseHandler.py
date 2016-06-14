# -*- coding:utf-8 -*-
import tornado.web

class AdminBaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("admin")

    def get_login_url(self):
        self.require_setting("admin_login_url", "@tornado.web.authenticated")
        return self.application.settings["admin_login_url"]
