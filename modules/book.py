# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class Book:

	def __init__(self):
		df = DatabaseFactory()
		self._db = df.connection()

	def save(self, book):
		query = "INSERT INTO book(book_nickname, book_realname, book_intro, \
			book_cover, book_cate_id, book_path, book_realpath, book_realtype, \
			book_uploader, book_author, book_pages) \
			VALUES(%(nickname)s, %(realname)s, %(intro)s, %(cover)s, %(cid)s, \
			%(path)s, %(realpath)s, %(realtype)s, %(uploader)s, %(author)s, \
			%(pages)s)"
		return self._db.execute(query, nickname=book["nickname"], \
				realname=book["realname"], intro=book["intro"], \
				cover=book["cover"], cid=int(book["cid"]), \
				path=book["path"], realpath=book["realpath"], \
				realtype=book["type"], uploader=book["uploader"], \
				author=book["author"], pages=book["pages"])

	def delete(self, bid):
		lastrowid = -1
		for id in bid:
			query = "DELETE FROM book WHERE book_id=%(bid)s"
			lastrowid = self._db.execute(query, bid=id)
		return lastrowid

	def query(self):
		query = "SELECT book_id id, book_nickname name, book_intro intro,\
				book_mtime mtime, book_uploader uploader, \
				book_cate_name cname, book_cover cover \
				FROM book AS b, book_category AS bc \
				WHERE b.book_cate_id = bc.book_cate_id"
		return self._db.query(query)

	def query_by_id(self, id):
		query = "SELECT book_id id, book_nickname name, book_mtime mtime, \
					book_uploader uploader, book_cover cover, book_intro intro,\
					book_path path, book_realpath realpath, book_realtype type, \
					book_pages pages, b.book_cate_id cid, book_cate_name cname\
				FROM book b, book_category bc\
				WHERE book_id=%(id)s AND b.book_cate_id=bc.book_cate_id"
		return self._db.get(query, id=id)

	def query_by_cate_id(self, cid):
		query = "SELECT book_id id, book_nickname name, book_mtime mtime, \
					book_uploader uploader, book_cover cover, book_intro intro,\
					book_path path, book_realpath realpath, book_realtype type, \
					book_pages pages, book_cate_name cname\
				FROM book b, book_category bc\
				WHERE b.book_cate_id=%(cid)s AND b.book_cate_id=bc.book_cate_id"
		return self._db.query(query, cid=cid)

	def query_limit(self, limit=6):
		query = "SELECT book_id id, book_nickname name, book_cover cover\
				FROM book\
				ORDER BY book_mtime DESC LIMIT %(limit)s"
		return self._db.query(query, limit=limit)

	def query_by_page(self, pagination=1, records=20):
		pagination = int(pagination)
		query = "SELECT book_id id, book_nickname name, book_uploader uploader,\
				book_mtime mtime, book_cate_name cname\
				FROM book b, book_category bc\
				WHERE b.book_cate_id=bc.book_cate_id \
				LIMIT %(start)s, %(size)s"
		return self._db.query(query, start=(pagination-1)*records,\
									size=records)

	def count(self):
		query = "SELECT count(*) as cnt FROM book"
		return self._db.get(query)
