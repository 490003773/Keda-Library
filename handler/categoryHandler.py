# -*- coding:utf-8 -*-
import tornado.web
from modules import CommonCategory, BookCategory, \
	TopicCategory, MagazineCategory
from baseHandler import BaseHandler

class CategoryHandler(BaseHandler):

	@tornado.web.asynchronous
	@tornado.web.authenticated
	def get(self, cname, pid):
		category = []
		if cname == "common":
			category = CommonCategory().query_by_pid(pid)
		else:
			category = globals()["%sCategory"%cname.capitalize()]().query_all()

		if category:
			html = self.render_string("category.html", category=category,
									cname=cname, pid=pid)
			self.write(html)
		self.finish()
