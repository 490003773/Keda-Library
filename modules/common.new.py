# -*- coding:utf-8 -*-

from DatabaseFactory import DatabaseFactory
from documents import Document

class Common(Document):

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def save(self, common):
		query = "INSERT INTO common(com_nickname, com_realname, com_intro, \
			com_cover, com_cate_id, com_path, com_realpath, com_realtype, \
			com_uploader, com_cate_pid, com_pages) \
			VALUES(%(nickname)s, %(realname)s, %(intro)s, %(cover)s, %(cid)s, \
			%(path)s, %(realpath)s, %(realtype)s, %(uploader)s, %(pid)s, \
			%(pages)s)"
		return self._db.execute(query, nickname=common["nickname"],
			realname=common["realname"], intro=common["intro"],
			cover=common["cover"], cid=int(common["cid"]), path=common["path"],
            realpath=common["realpath"], realtype=common["type"],
			uploader=common["uploader"], pid=common["pid"], pages=common["pages"])

    def delete(self, id):
        pass

    def query(self):
        pass

    def query_by_id(self, id):
        pass

    def query_by_cate_id(self, cid):
        pass

    def query_latest(self, latest):
        pass

    def query_by_limit(self, start, record):
        pass

    def save(self, doc):
        pass

    def count(self):
        pass
