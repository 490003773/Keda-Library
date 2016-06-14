# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class Magazine:

	def __init__(self):
		df = DatabaseFactory()
		self._db = df.connection()

	def save(self, magazine):
		query = "INSERT INTO magazine(mgz_nickname, mgz_realname, mgz_intro,\
		 		mgz_cover, mgz_cate_id, mgz_path, mgz_realpath, mgz_realtype,\
				 mgz_uploader, mgz_publisher, mgz_issue, mgz_pages) \
				 VALUES(%(nickname)s, %(realname)s, %(intro)s, %(cover)s, \
				 %(cid)s, %(path)s, %(realpath)s, %(realtype)s, %(uploader)s,\
				  %(publisher)s, %(issue)s, %(pages)s)"
		return self._db.execute(query, nickname=magazine["nickname"], \
				realname=magazine["realname"], intro=magazine["intro"], \
				cover=magazine["cover"], cid=int(magazine["cid"]), \
				path=magazine["path"], realpath=magazine["realpath"], \
				realtype=magazine["type"], uploader=magazine["uploader"], \
				publisher=magazine["publisher"], issue=magazine["issue"],\
				pages=magazine["pages"])

	def delete(self, mid):
		lastrowid = -1
		for id in mid:
			query = "DELETE FROM magazine WHERE mgz_id=%(mid)s"
			lastrowid = self._db.execute(query, mid=id)
		return lastrowid

	def query(self):
		query = "SELECT mgz_id AS id, mgz_nickname AS name, mgz_mtime AS mtime,\
				mgz_uploader AS uploader, mgz_cate_name AS cname, \
				mgz_cover AS cover, mgz_intro intro \
				FROM magazine AS m, magazine_category AS mc WHERE \
				m.mgz_cate_id = mc.mgz_cate_id"
		return self._db.query(query)

	def query_by_id(self, id):
		query = "SELECT mgz_id id, mgz_nickname name, mgz_mtime mtime, \
					mgz_uploader uploader, mgz_cover cover, mgz_intro intro,\
					mgz_path path, mgz_realpath realpath, mgz_realtype type,\
					mgz_pages pages, m.mgz_cate_id cid, mgz_cate_name cname \
				FROM magazine m, magazine_category mc\
				WHERE mgz_id=%(id)s AND m.mgz_cate_id=mc.mgz_cate_id"
		return self._db.get(query, id=id)

	def query_by_cate_id(self, cid):
		query = "SELECT mgz_id id, mgz_nickname name, mgz_mtime mtime, \
					mgz_uploader uploader, mgz_cover cover, mgz_intro intro,\
					mgz_path path, mgz_realpath realpath, mgz_realtype type,\
					mgz_pages pages, mgz_cate_name cname \
				FROM magazine m, magazine_category mc\
				WHERE m.mgz_cate_id=%(cid)s AND m.mgz_cate_id=mc.mgz_cate_id"
		return self._db.query(query, cid=cid)

	def query_limit(self, limit=7):
		query = "SELECT mgz_id id, mgz_nickname name, mgz_cover cover,\
				mgz_publisher publisher, mgz_issue issue\
				FROM magazine\
				ORDER BY mgz_mtime DESC LIMIT %(limit)s"
		return self._db.query(query, limit=limit)

	def query_by_page(self, pagination=1, records=20):
		pagination = int(pagination)
		query = "SELECT mgz_id id, mgz_nickname name, mgz_mtime mtime, \
				mgz_uploader uploader, mgz_cate_name cname\
				FROM magazine m, magazine_category mc\
				WHERE m.mgz_cate_id=mc.mgz_cate_id\
				LIMIT %(start)s, %(size)s"
		return self._db.query(query, start=(pagination-1)*records,\
									size=records)

	def count(self):
		query = "SELECT count(*) as cnt FROM magazine"
		return self._db.get(query)
