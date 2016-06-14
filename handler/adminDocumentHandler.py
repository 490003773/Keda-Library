# -*- coding:utf-8 -*-
import tornado.web
from modules import Common, Book, Topic, Magazine
from conf import paging_config
import json
import re
from adminBaseHandler import AdminBaseHandler

class AdminDocumentHandler(AdminBaseHandler):

    number = re.compile(r"[^\d]")

    @tornado.web.asynchronous
    def prepare(self):
        self.category = globals()

    '''
        获取文档信息
        url : 1. /admin/document                - 请求管理文档
              2. /admin/document?type=[type]    - 请求某个类别
    '''

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        result = {"status": False}
        try:
            d_type = self.get_argument("type", "")
            if not d_type:
                result["message"] = self.render_string("admin/document_manage.html")
                result["status"] = True
            else:
                if d_type.capitalize() in self.category.keys():
                    page = self.get_argument("page", "1")
                    if not self.number.search(page):
                        page = int(page)
                        d_type_category = self.category[d_type.capitalize()]()
                        total_records = d_type_category.count()["cnt"]
                        total_pages = total_records / paging_config.records + 1
                        # 页码正确，查找信息
                        if page <= total_pages:
                            docs = d_type_category.query_by_page(
                                            pagination=page, records=paging_config.records)
                            result["list"] = self.render_string("admin/doc_list.html",
                                                        docs=docs, type=d_type)
                            result["paging"] = self.render_string("admin/doc_paging.html",
                                                total_pages=total_pages, type=d_type,
                                                current_page=page)
                            result["status"] = True
                        else:
                            result["message"] = "页码超出范围"
                    else:
                        result["message"] = "PAGE错误"
                else:
                    result["message"] = "该分类不存在"
        except Exception as e:
            print e
            result["message"] = "文档管理请求错误"
        self.write(json.dumps(result))
        self.finish()

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def delete(self):
        result = {"status": False}
        try:
            cname = self.get_argument("type")
            cid = self.get_arguments("docid")
            if cname and cid:
                if cname.capitalize() in self.category.keys():
                    lastrowid = self.category[cname.capitalize()]().delete(cid)
                    result["status"] = True
                    result["message"] = "删除成功"
                else:
                    result["message"] = "文档不属于该分类"
            else:
                result["message"] = "删除失败，信息不完整"
        except Exception as e:
            print e
            result["message"] = "删除文档异常"
        self.write(json.dumps(result))
        self.finish()
