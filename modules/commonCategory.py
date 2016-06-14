# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class CommonCategory:

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def dist(self):
        rows = self.query_all()
        categories = {}
        for row in rows:
            if not row['pid'] in categories.keys():
                categories[row['pid']] = {}
            categories[row['pid']][row['id']] = row['name']
        return categories

    def query_all(self):
        query = "SELECT com_cate_id AS id, com_cate_name AS name, \
                com_cate_pid AS pid \
                FROM common_category WHERE com_cate_id>1 \
                ORDER BY id DESC, com_cate_pid, com_cate_level"
        return self._db.query(query)

    def query_by_pid(self, pid):
        query = "SELECT com_cate_id AS id, com_cate_name AS name\
                FROM common_category \
                WHERE com_cate_pid=%(pid)s AND com_cate_id>1\
                ORDER BY com_cate_level asc"
        return self._db.query(query, pid=pid)

    def add(self, name, pid, level=0):
        query = "INSERT INTO common_category(com_cate_name, com_cate_pid, \
                    com_cate_level)\
                    VALUES (%(name)s, %(pid)s, %(level)s)"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, pid=pid, level=level)
        return lastrowid

    def delete(self, id):
        query = "DELETE FROM common_category WHERE com_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, id=id)
        return lastrowid

    def update(self, id, name):
        query = "UPDATE common_category SET com_cate_name=%(name)s\
            WHERE com_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, id=id)
        return lastrowid

    def query_by_id(self, id):
        query = "SELECT com_cate_id id, com_cate_name cname FROM common_category \
                WHERE com_cate_pid=%(id)s"
        return self._db.get(query, id=id)
