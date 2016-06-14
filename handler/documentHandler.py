# -*- coding:utf-8 -*-
import tornado.web
from modules import Common, Book, Topic, Magazine, CommonCategory, \
                    BookCategory, TopicCategory, MagazineCategory
import json, datetime

class DatatimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class DocumentHandler(tornado.web.RequestHandler):

    '''/document?type={type}[&cid={cid}]'''
    @tornado.web.asynchronous
    def get(self):
        result = {}
        docs = []
        doc_cate = []
        try:
            d_type = self.get_argument("type", "common")
            d_cid = self.get_argument("cid", "0")
            doc = globals()[d_type.capitalize()]()
            docs = doc.query()
            if d_cid != "0":
                docs = doc.query_by_cate_id(d_cid)
            doc_cate = globals()["%sCategory" %d_type.capitalize()]().query_all()
            '''
                doc_cate is a dict
                keys:
                    id   : cate id,
                    name : cate name
            '''
            docs.append(d_type)
            ''' docs is a list, include some dicts and a d_type
                key:
                    id       : doc id
                    name     : doc name,
                    intro    : doc intro,
                    mtime    : doc make time,
                    cover    : doc cover dir,
                    uploader : who upload the doc,
                    cname    : doc category zh_name,
            '''
        except Exception as e:
            print e
        self.write(json.dumps(dict(docs=docs, doc_cate=doc_cate), cls=DatatimeEncoder))
        self.finish()
