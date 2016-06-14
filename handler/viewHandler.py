# -*- coding:utf-8 -*-
import tornado.web
from baseHandler import BaseHandler
from modules import Common, Book, CommonCategory, Magazine, Topic, Permission
import os

class ViewHandler(BaseHandler):

    navdict = {
        "book"     : "图书",
        "common"   : "分类",
        "topic"    : "专题",
        "magazine" : "杂志"
    }
    # 最多读10页
    page_limit = 10

    @tornado.web.asynchronous
    def get(self, category, id):
        doc = globals()[category.capitalize()]().query_by_id(id)
        doc["category"] = category
        doc["view"] = True
        download_url = "javascript:;"
        username = self.get_secure_cookie("username")
        login = False
        if username:
            login = True
        real_pms = {"login":0, "download":0}
        # 权限控制
        if category == "common":
            p_pms = Permission().query_by_cate_id(doc["pid"])
            c_pms = Permission().query_by_cate_id(doc["cid"])
            if not p_pms:
                p_pms = {"login":0, "download":0}
            if not c_pms:
                c_pms = {"login":0, "download":0}
            real_pms = {"login": p_pms["login"]|c_pms["login"],
                        "download": p_pms["download"]|p_pms["download"]}
            if real_pms["login"]:
                if not login:
                    doc["view"] = False
        # 面包屑导航
        breadcrumb_nav = [self.navdict[category], doc["cname"]]
        if category == "common" and (doc["pid"] != doc["cid"]):
            next_cate = CommonCategory().query_by_id(doc["pid"])
            if next_cate:
                breadcrumb_nav.append(next_cate["cname"])
        # 如果权限允许，获取详情，样式
        if doc["view"]:
            doc["view"] = ""
            filedir = "/".join(doc["path"].split("/")[:-1])
            doc["css"] = [filedir+"/style.css",]
            static_path = self.application.settings["static_path"]

            srcdir = os.path.join(static_path, filedir)
            if doc["pages"]>self.page_limit:
                doc["tips"] = "文档过长，请下载阅读全部"
                doc["pages"] = self.page_limit
            for i in range(0, min(doc["pages"], self.page_limit)):
                filename = os.path.join(srcdir, "view%s.html"%str(i+1))
                if os.path.isfile(filename):
                    with open(filename, "rb") as f:
                        doc["view"] += f.read()
                else:
                    break
            download_url = "/download/%s/%s" %(doc["category"], doc["id"])
        else:
            doc["view"] = "登录后查看"
        self.render("read.html", doc=doc, username=username, login=login,
                        breadcrumb_nav=breadcrumb_nav,
                        download_url=download_url,
                        message="")
