# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class MagazineCategory:

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def query_all(self):
        query = "SELECT mgz_cate_id id, mgz_cate_name name\
                FROM magazine_category ORDER BY id DESC"
        return self._db.query(query)

    def add(self, name):
        query = "INSERT INTO magazine_category(mgz_cate_name) VALUES (%(name)s)"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name)
        return lastrowid

    def delete(self, id):
        query = "DELETE FROM magazine_category WHERE mgz_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, id=id)
        return lastrowid

    def update(self, id, name):
        query = "UPDATE magazine_category SET mgz_cate_name=%(name)s\
                WHERE mgz_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, id=id)
        return lastrowid
