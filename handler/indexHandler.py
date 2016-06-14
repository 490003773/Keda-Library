# -*- coding:utf-8 -*-
import tornado.web
from modules import Common, Book, Topic, Magazine, count,\
 				CommonCategory, TopicCategory

class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        try:
            message = self.get_argument("message", "")
            username = self.get_secure_cookie("username")
            login = True
            if not username:
                username = ""
                login = False
            # login = True if username else False
            # 分类信息
            com_cate = CommonCategory().dist()
            # 分类专区
            commons = Common().dist()
            # 热门专题func_nafunc_na
            topics = TopicCategory().query_limit()
            # 图书
            books = Book().query_limit()
            # 杂志
            magazines = Magazine().query_limit()
            # 统计文档数量
            total_records = count()["count"]
            total_records = str(total_records).zfill(7)
            result = dict(
                username  = username,
                login	  = login,
                message   = message,
                category  = com_cate,
                commons   = commons,
                topics    = topics,
                books     = books,
                magazines = magazines,
                count 	  = total_records
            )
            self.render("index.html", **result)
        except Exception as e:
            print e
            self.write("系统内部错误，请联系管理员!")
            self.finish()
