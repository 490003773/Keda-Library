# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class Permission:

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def add(self, cid, login, download):
        query = "INSERT INTO permission(per_login, per_download, per_cate_id)\
                VALUES(%(login)s, %(download)s, %(cid)s)"
        return self._db.execute(query, login=int(login), download=int(download), cid=int(cid))

    def query(self):
        query = "SELECT per_login login, per_download download, per_cate_id cid\
                FROM permission"
        return self._db.query(query)

    def update(self, cid, login, download):
        query = "UPDATE permission SET per_login=%(login)s, \
                                    per_download=%(download)s \
                WHERE per_cate_id=%(cid)s"
        return self._db.execute(query, cid=int(cid), login=int(login), download=int(download))

    def query_by_cate_id(self, cid):
        query = "SELECT per_login login, per_download download, per_cate_id cid\
                FROM permission WHERE per_cate_id=%(cid)s"
        return self._db.get(query, cid=int(cid))

    def exist(self, cid):
        query = "SELECT per_cate_id FROM permission WHERE per_cate_id=%(cid)s"
        return self._db.get(query, cid=int(cid))
