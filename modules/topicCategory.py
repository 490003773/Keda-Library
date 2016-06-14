# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class TopicCategory:

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def query_all(self):
        query = "SELECT top_cate_id id, top_cate_name name FROM topic_category ORDER BY id DESC"
        return self._db.query(query)

    def query_limit(self, limit=4):
		query = "SELECT top_cate_id id, top_cate_name name, top_cate_cover cover\
				FROM topic_category ORDER BY top_cate_mtime DESC LIMIT 4"
		return self._db.query(query, id=id)

    def add(self, name, cover):
        query = "INSERT INTO topic_category(top_cate_name, top_cate_cover) \
                    VALUES (%(name)s, %(cover)s)"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, cover=cover)
        return lastrowid

    def delete(self, id):
        query = "DELETE FROM topic_category WHERE top_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, id=id)
        return lastrowid

    def update(self, id, name):
        query = "UPDATE topic_category SET top_cate_name=%(name)s\
                WHERE top_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, id=id)
        return lastrowid
