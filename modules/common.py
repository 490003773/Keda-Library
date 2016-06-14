# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class Common:

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
			cover=common["cover"], cid=int(common["cid"]), path=common["path"], realpath=common["realpath"], realtype=common["type"],
			uploader=common["uploader"], pid=common["pid"], pages=common["pages"])

	def delete(self, cid):
		lastrowid = -1
		for id in cid:
			query = "DELETE FROM common WHERE com_id=%(cid)s"
			lastrowid = self._db.execute(query, cid=id)
		return lastrowid

	def query(self):
		query = "SELECT com_id AS id, com_nickname AS name, com_intro AS intro, \
				com_mtime AS mtime, com_uploader AS uploader, \
				com_cate_name AS cname, com_cover AS cover \
				FROM common AS c, common_category AS cc \
				WHERE c.com_cate_id = cc.com_cate_id"
		return self._db.query(query)

	def query_by_id(self, id):
		query = "SELECT com_id id, com_nickname name, com_mtime mtime, \
					com_uploader uploader, com_cover cover, com_intro intro,\
					com_path path, com_realpath realpath, com_realtype type, \
					com_pages pages, c.com_cate_id cid, c.com_cate_pid pid, \
					com_cate_name cname \
				FROM common c, common_category cc\
				WHERE com_id=%(id)s AND c.com_cate_pid=cc.com_cate_id"
		return self._db.get(query, id=int(id))

	def query_by_cate_id(self, cid):
		query = "SELECT com_id id, com_nickname name, com_mtime mtime, \
					com_uploader uploader, com_cover cover, com_intro intro,\
					com_path path, com_realpath realpath, com_realtype type, \
					com_pages pages, com_cate_name cname \
				FROM common c, common_category cc\
				WHERE c.com_cate_pid=cc.com_cate_id AND \
						(c.com_cate_id=%(cid)s OR c.com_cate_pid=%(cid)s)"
		return self._db.query(query, cid=int(cid))

	def query_limit(self, limit=4):
		query = "SELECT com_id id, com_nickname name, com_cover cover, \
						com_cate_name cname, com_realtype type, \
						c.com_cate_pid pid\
					FROM common c LEFT JOIN common_category cc \
						ON c.com_cate_pid=cc.com_cate_id \
					WHERE (\
							SELECT count(*) \
							FROM common \
							WHERE c.com_cate_pid=com_cate_pid \
								AND c.com_id<com_id\
							)<%(limit)s\
					ORDER BY com_mtime DESC"
		return self._db.query(query, limit=limit)

	def query_by_page(self, pagination=1, records=20):
		pagination = int(pagination)
		query = "SELECT com_id id, com_nickname name, com_mtime mtime, \
				com_uploader uploader, com_cate_name cname\
				FROM common c, common_category cc\
				WHERE c.com_cate_id=cc.com_cate_id\
				LIMIT %(start)s, %(size)s"
		return self._db.query(query, start=(pagination-1)*records, size=records)

	def count(self):
		query = "SELECT count(*) as cnt FROM common"
		return self._db.get(query)

	def dist(self):
		rows = self.query_limit()
		commons = {}
		for row in rows:
			if row["pid"] not in commons.keys():
				commons[row["pid"]] = []
			commons[row["pid"]].append({"id":row["id"], "name":row["name"],
							"type":row["type"], "cover":row["cover"]})
		return commons
