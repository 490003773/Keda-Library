# -*- coding:utf-8 -*-
import tornado.web
from baseHandler import BaseHandler

class LogoutHandler(BaseHandler):

	@tornado.web.asynchronous
	@tornado.web.authenticated
	def get(self):
		self.set_secure_cookie("username", "")
		self.redirect("/")
