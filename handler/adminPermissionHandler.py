# -*- coding:utf-8 -*-
import tornado.web
import json
from modules import CommonCategory, Permission
from adminBaseHandler import AdminBaseHandler

class AdminPermissionHandler(AdminBaseHandler):

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        result = {"status": False}
        try:
            cid = self.get_argument("cid", "0")
            if cid == "0":
                com_cate = CommonCategory().query_all()
                result["message"] = self.render_string("admin/permission_manage.html", category=com_cate)
            else:
                result["pms"] = Permission().query_by_cate_id(cid)
            result["status"] = True
        except Exception as e:
            print e
            result["message"] = "权限管理请求错误"
        self.write(json.dumps(result))
        self.finish()

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def post(self):
        result = {"status": False}
        try:
            cid = self.get_argument("category")
            login = self.get_argument("login", "0")
            download = self.get_argument("download", "0")
            pms = Permission()
            # update if exists else add
            if pms.exist(cid):
                lastrowid = pms.update(cid, login, download)
            else:
                lastrowid = pms.add(cid, login, download)
            result["status"] = True
        except Exception as e:
            print e
            result["message"] = "权限添加错误"
        self.write(json.dumps(result))
        self.finish()
