# -*- coding:utf-8 -*-
from DatabaseFactory import DatabaseFactory

class Topic:

	def __init__(self):
		df = DatabaseFactory()
		self._db = df.connection()

	def save(self, topic):
		query = "INSERT INTO topic(top_nickname, top_realname, top_intro, \
				top_cover, top_cate_id, top_path, top_realpath, top_realtype, \
				top_uploader, top_pages) \
				VALUES(%(nickname)s, %(realname)s, %(intro)s, %(cover)s, \
				%(cid)s, %(path)s, %(realpath)s, %(realtype)s, %(uploader)s,\
				%(pages)s)"
		return self._db.execute(query, nickname=topic["nickname"], \
				realname=topic["realname"], intro=topic["intro"], \
				cover=topic["cover"], cid=int(topic["cid"]), \
				path=topic["path"], realpath=topic["realpath"], \
				realtype=topic["type"], uploader=topic["uploader"],\
				pages=topic["pages"])

	def delete(self, tid):
		lastrowid = -1
		conn = Connection()
		for id in tid:
			query = "DELETE FROM topic WHERE top_id=%(tid)s"
			lastrowid = conn.execute(query, tid=id)
		return lastrowid

	def query(self):
		query = "SELECT top_id AS id, top_nickname AS name, top_mtime AS mtime,\
				top_uploader AS uploader, top_cate_name AS cname, \
				top_cover AS cover, top_intro intro \
				FROM topic AS t, topic_category AS tc \
				WHERE t.top_cate_id = tc.top_cate_id"
		return self._db.query(query)

	def query_by_id(self, id):
		query = "SELECT top_id id, top_nickname name, top_mtime mtime, \
					top_uploader uploader, top_cover cover, top_intro intro,\
					top_path path, top_realpath realpath, top_realtype type, \
					top_pages pages, t.top_cate_id cid, top_cate_name cname \
				FROM topic t, topic_category tc\
				WHERE top_id=%(id)s AND t.top_cate_id=tc.top_cate_id"
		return self._db.get(query, id=id)

	def query_by_cate_id(self, cid):
		query = "SELECT top_id id, top_nickname name, top_mtime mtime, \
					top_uploader uploader, top_cover cover, top_intro intro,\
					top_path path, top_realpath realpath, top_realtype type, \
					top_pages pages, top_cate_name cname \
				FROM topic t, topic_category tc\
				WHERE t.top_cate_id=%(cid)s AND t.top_cate_id=tc.top_cate_id"
		return self._db.query(query, cid=cid)

	def query_limit(self, limit=4):
		query = "SELECT top_id AS id, top_nickname AS name, top_cover AS cover\
				FROM topic ORDER BY top_mtime DESC LIMIT 4"
		return self._db.query(query, id=id)

	def query_by_page(self, pagination=1, records=20):
		pagination = int(pagination)
		query = "SELECT top_id id, top_nickname name, top_mtime mtime, \
				top_uploader uploader, top_cate_name cname\
				FROM topic t, topic_category tc\
				WHERE t.top_cate_id=tc.top_cate_id\
				LIMIT %(start)s, %(size)s"
		return self._db.query(query, start=(pagination-1)*records,\
								 size=records)

	def count(self):
		query = "SELECT count(*) as cnt FROM topic"
		return self._db.get(query)
