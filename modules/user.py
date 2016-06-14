from DatabaseFactory import DatabaseFactory
import hashlib

class User:

	username = None
	password = None

	def __init__(self):
		df = DatabaseFactory()
		self._db = df.connection()

	# add user
	# lastrowid : return value
	#				-1 : username exists
	#				 0 : insert failed
	#				>0 : insert success
	def add(self, username, password, realname):
		lastrowid = -1
		if not self.is_username(username):
			query = "insert into user(username, password, realname) values(%s, %s, %s)"
			lastrowid = self._db.execute(query, username, \
								hashlib.sha1(password).hexdigest(),\
								realname)
		return lastrowid

	def query(self):
		query = "select uid, username, realname, password, mtime from user"
		return self._db.query(query)

	def delete(self, uid):
		lastrowid = -1
		query = "DELETE FROM user WHERE uid=%(uid)s"
		lastrowid = self._db.execute(query, uid=uid)
		return lastrowid

	def update(self, username, password, realname, uid):
		query = "UPDATE user SET username=%(username)s, realname=%(realname)s"
		if password:
			passwd = ",password='%s'" %hashlib.sha1(password).hexdigest()
			query += passwd
		query += " WHERE uid=%(uid)s"
		return self._db.execute(query, username=username, realname=realname, uid=uid)

	def sign_in(self, username, password):
		query = "select username, password from user where username=%(username)s"
		row = self._db.get(query, username=username)
		result = -1
		if row:
			if row["password"] == hashlib.sha1(password).hexdigest():
				result = 1
			else:
				result = 0
		return result

	# check user exists
	def is_username(self, username):
		result = False
		query = "select username from user where username=%(username)s"
		row = self._db.get(query, username=username)
		if row:
			result = True
		return result

	def is_user(self, uid):
		result = False
		query = "select username from user where uid=%(uid)s"
		row = self._db.get(query, uid=uid)
		if row:
			result = True
		return result
