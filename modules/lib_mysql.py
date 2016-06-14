# -*- coding:utf-8 -*-

import MySQLdb
from database import Database

class Connection(Database):

	def __init__(self, conf):
		try:
			self.conf = conf
			self._connect()
		except MySQLdb.Error, e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

	def _connect(self):
		self.close()
		self._db = MySQLdb.connect(host=self.conf.host, port=self.conf.port,
				user=self.conf.user, passwd=self.conf.password,
				db=self.conf.database, charset=self.conf.charset)
		#self.cursor = self.connection.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		self._db.autocommit(True)

	def close(self):
		if getattr(self, "_db", None) is not None:
			self._db.close()
			self._db = None

	def query(self, query, *param, **kwparam):
		cursor = self._cursor()
		try:
			self._execute(cursor, query, param, kwparam)
			columns = [col[0] for col in cursor.description]
			return [dict(zip(columns, value)) for value in cursor]
		except MySQLdb.Error, e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
			raise
		finally:
			cursor.close()

	def get(self, query, *param, **kwparam):
		rows = self.query(query, *param, **kwparam)
		if not rows:
			return None
		else:
			return rows[0]

	def execute(self, query, *param, **kwparam):
		cursor = self._cursor()
		try:
			self._execute(cursor, query, param, kwparam)
			return cursor.lastrowid
		except MySQLdb.Error, e:
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
			raise
		finally:
			cursor.close()

	def _execute(self, cursor, query, param, kwparam):
		try:
			return cursor.execute(query, kwparam or param)
		except MySQLdb.Error, e:
			self.close()
			print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
			raise

	def _ensure_connect(self):
		if self._db is None:
			self._connect()

	def _cursor(self):
		self._ensure_connect()
		return self._db.cursor()

	def __del__(self):
		self.close()
