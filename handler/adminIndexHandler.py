# -*- coding:utf-8 -*-
import tornado.web
from tornado.escape import xhtml_escape
from modules import VerifyCode, overview, User
import os
import json

class AdminIndexHandler(tornado.web.RequestHandler):

	@tornado.web.asynchronous
	def get(self):
		username = self.get_secure_cookie("admin")
		verifycode = None
		lib_info = {}
		if not username:
			vpath = self.application.settings["static_path"]
			verifycode = VerifyCode(os.path.join(vpath, "img/verifycode"))
			self.set_secure_cookie("verifycode", verifycode.strs.upper())
		self.render("admin/index.html", verifycode=verifycode, \
					username=username)

	@tornado.web.asynchronous
	def post(self):
		result={"status": False, "message": "用户名错误"}
		verifycode = xhtml_escape(self.get_argument("verifycode")).upper()
		if verifycode == self.get_secure_cookie("verifycode"):
			username = xhtml_escape(self.get_argument("username"))
			password = xhtml_escape(self.get_argument("password"))
			# sign_in : -1 - 用户名错误（default）
			# 			 0 - 密码错误
			# 			 1 - 正确
			sign_in = User().sign_in(username, password)
			if sign_in == 1:
				result["status"] = True
				self.set_secure_cookie("admin", username, expires_days=None)
			elif sign_in == 0:
				result["message"] = "密码错误"
		else:
			result["message"] = "验证码错误"
		self.write(json.dumps(result))
		self.finish()
