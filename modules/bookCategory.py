# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class BookCategory:

    def __init__(self):
        df = DatabaseFactory()
        self._db = df.connection()

    def query_all(self):
        query = "SELECT book_cate_id id, book_cate_name name FROM book_category ORDER BY id DESC"
        return self._db.query(query)

    def add(self, name):
        query = "INSERT INTO book_category(book_cate_name) VALUES (%(name)s)"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name)
        return lastrowid

    def delete(self, id):
        query = "DELETE FROM book_category WHERE book_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, id=id)
        return lastrowid

    def update(self, id, name):
        query = "UPDATE book_category SET book_cate_name=%(name)s\
            WHERE book_cate_id=%(id)s"
        lastrowid = -1
        lastrowid = self._db.execute(query, name=name, id=id)
        return lastrowid

    def query_by_id(self, id):
        query = "SELECT book_cate_id FROM book_category WHERE book_cate_id=%(id)s"
        return self._db.get(query, id=id)
