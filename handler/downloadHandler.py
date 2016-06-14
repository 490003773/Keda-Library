# -*- coding:utf-8 -*-
import tornado.web
from baseHandler import BaseHandler
from modules import Common, Book, Magazine, Topic, Permission
import os

class DownloadHandler(BaseHandler):

    @tornado.web.asynchronous
    def get(self, category, id):
        doc = globals()[category.capitalize()]().query_by_id(id)
        isdownload = True
        real_pms = {"login":0, "download":0}
        message = "该文档不允许下载"
        if category == "common":
            p_pms = Permission().query_by_cate_id(doc["pid"])
            c_pms = Permission().query_by_cate_id(doc["cid"])
            if not p_pms:
                p_pms = {"login":0, "download":0}
            if not c_pms:
                c_pms = {"login":0, "download":0}
            real_pms = {"login": p_pms["login"]|c_pms["login"],
                        "download": p_pms["download"]|p_pms["download"]}
            username = self.get_secure_cookie("username")
            if real_pms["download"]:
                if not username:
                    isdownload = False
                    message = "登录后下载"
        print real_pms
        print message
        if isdownload:
            static_path = self.application.settings["static_path"]
            doc["realpath"] = os.path.join(static_path, doc["realpath"])
            self.set_header("Content-Type", "application/octed-stream")
            self.set_header('Content-Disposition',
                            "attachment;filename=%s.%s;charset=utf-8"
                                    % (doc["name"], doc["type"]))
            data = open(doc["realpath"], "r")
            self.write(data.read())
        else:
            self.write(message)
        self.finish()
        data.close()
