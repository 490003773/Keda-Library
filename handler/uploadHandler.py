# -*- coding:utf-8 -*-
import tornado.web
from tornado.escape import xhtml_escape
import json
import time
import shutil
import os
from modules import Upload
from baseHandler import BaseHandler
import multiprocessing

class UploadHandler(BaseHandler):

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
		username = self.get_secure_cookie("username")
		self.render("upload.html", login=True, username=username)

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        result = {}
        try:
            tmp_file = self.get_argument("tmp_file")
            result["status"] = os.path.isfile(tmp_file)
            if result["status"]:
                result["message"] = "上传成功"
                self.write(json.dumps(result))
                self.finish()
                file_info = {
        			"nickname" : xhtml_escape(self.get_argument("nickname")),
                    "category" : self.get_argument("category"),
        			"intro"    : xhtml_escape(self.get_argument("intro")),
        			"uploader" : self.get_secure_cookie("username"),
                    "tmp_file" : tmp_file,
                }
                category = self.get_argument("category")
                sub_category = self.get_arguments("sub_category")
                file_info["cid"] = sub_category[-1]
                if category == "common":
                    # 常用分类，需要记录pid
                    file_info["pid"] = sub_category[0]
                if category == "book":
        			# 图书类，需要作者
                    file_info["author"] = self.get_argument("author", "anonymous")
                elif category == "magazine":
        			# 杂志类，需要出版社，刊号
                    file_info["publisher"] = xhtml_escape(
                                        self.get_argument("publisher", "unknown"))
                    file_info["issue"] = xhtml_escape(
                                        self.get_argument("issue", "unknown"))
                file_path = {
                    "static_path" : self.application.settings["static_path"],
                    "temp_path"   : self.application.settings["temp_path"]
                }
                pool = multiprocessing.Pool(processes=8)
                pool.apply_async(Upload, (file_info, file_path))
                pool.close()
                pool.join()
            else:
                result["message"] = "附件已丢失...请联系网站管理员或重新上传"
                self.write(json.dumps(result))
                self.finish()
                return

        except Exception as e:
            print e
            # result["status"] = False
            # result["message"] = e
            self.finish()
