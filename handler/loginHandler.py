# -*- coding:utf-8 -*-
import json
from tornado.template import Loader
from tornado.escape import xhtml_escape
from modules import LDAPTool
import re
from baseHandler import BaseHandler
import tornado.web

class LoginHandler(BaseHandler):

	# login
	# ajax post request
	# data : username, password
	#		if admin login, have another data named verifycode
	@tornado.web.asynchronous
	def post(self):
		username = xhtml_escape(self.get_argument("username", strip=True))
		password = xhtml_escape(self.get_argument("password", strip=True))
		try:
			result = {"status": False, "message": "用户名或密码错误"}
			result["status"] = LDAPTool().ldap_get_vaild(username, password)
			if result["status"]:
				self.set_secure_cookie("username", username, expires_days=None)
				result["message"] = "登陆成功"
		except Exception as e:
			result["message"] = "用户不存在"
		self.write(json.dumps(result))
		self.finish()
