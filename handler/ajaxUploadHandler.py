# -*- coding:utf-8 -*-
import tornado.web
import os
import json
from conf import ftype

class AjaxUploadHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def post(self):
        result = {"status": False}
        tmp_file = self.get_argument("tmp_path")
        suffix = self.get_argument("file_name").split(".")[-1]
        size = self.get_argument("size")
        try:
            if size > 0:
                if suffix in ftype.white_list:
                    os.rename(tmp_file, "%s.%s" %(tmp_file, suffix))
                    result["status"] = True
                    result["filename"] = "%s.%s" %(tmp_file, suffix)
                else:
                    result["message"] = "文件类型错误"
            else:
                result["message"] = "文件为空"
            if not result["status"]:
                os.remove(tmp_file)
        except Exception as e:
            print e
            result["message"] = "Ajax文件上传异常"
            os.remove(tmp_file)
        self.write(json.dumps(result))
        self.finish()
