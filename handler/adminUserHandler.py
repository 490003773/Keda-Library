# -*- coding:utf-8 -*-
import tornado.web
from tornado.escape import xhtml_escape
from modules import User
import json
import re

class AdminUserHandler(tornado.web.RequestHandler):

    number = re.compile(r"[^\d]")

    @tornado.web.asynchronous
    def get(self):
        result = {"status": False}
        try:
            users = User().query()
            result["message"] = self.render_string("admin/user_manage.html", users=users)
            result["status"] = True
        except Exception as e:
            print e
            result["message"] = "用户管理请求错误"
        self.write(json.dumps(result))
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        result = {"status": False}
        try:
            username = xhtml_escape(self.get_argument("username"))
            password = xhtml_escape(self.get_argument("password"))
            realname = xhtml_escape(self.get_argument("realname"))
            lastrowid = User().add(username, password, realname)
            if lastrowid > 0:
                result["status"] = True
                result["message"] = "添加成功"
            elif lastrowid == 0:
                result["message"] = "添加失败"
            elif lastrowid == -1:
                result["message"] = "用户名存在"
            else:
                # unexcept
                result["message"] = "情况未知"
                pass
        except Exception as e:
            print e
            result["message"]="添加用户异常"
        self.write(json.dumps(result))
        self.finish()

    @tornado.web.asynchronous
    def delete(self):
        result = {"status" : False}
        try:
            uid = self.get_argument("uid")
            if not self.number.search(uid):
                lastrowid = User().delete(uid)
                result["message"] = "删除成功"
                result["status"] = True
            else:
                result["message"] = "UID错误"
        except Exception as e:
            print e
            result["message"] = "删除用户异常"
        self.write(json.dumps(result))
        self.finish()

    @tornado.web.asynchronous
    def put(self):
        result = {"status" : False}
        try:
            uid = self.get_argument("uid")
            username = self.get_argument("username")
            realname = self.get_argument("realname")
            password = self.get_argument("password", "")
            if not self.number.search(uid):
                lastrowid = User().update(username, password, realname, uid)
                result["message"] = "删除成功"
                result["status"] = True
            else:
                result["message"] = "UID错误"
        except Exception as e:
            print e
            result["message"] = "删除用户异常"
        self.write(json.dumps(result))
        self.finish()
