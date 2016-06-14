# -*- coding:utf-8 -*-
import tornado.web
import json
import os
import time
from modules import Book, Common, Topic, Magazine, \
		CommonCategory, BookCategory, TopicCategory, MagazineCategory
from adminBaseHandler import AdminBaseHandler

class AdminCategoryHandler(AdminBaseHandler):
	# 添加分类
	@tornado.web.authenticated
	@tornado.web.asynchronous
	def post(self):
		result = {"status" : False}
		try:
			# category : "{type}[_{pid}]"
			category = self.get_argument("category").split("_")
			pid = 1 if len(category)==1 else int(category[1])
			cname = self.get_argument("cate_name")
			cate = globals()["%sCategory"%category[0].capitalize()]()
			result["cid"] = -1
			if category[0] == "common":
				result["cid"] = cate.add(cname, pid)
			elif category[0] == "topic":
				cover = self.request.files['cover'][0]
				cover_path = os.path.join(self.application.settings["static_path"], "img/cover")
				cover_name = "%s.%s" % (time.time(), cover["filename"].split(".")[-1])
				with open(os.path.join(cover_path, cover_name), "wb") as c:
					c.write(cover["body"])
				result["cid"] = cate.add(cname, cover_name)
			else:
				result["cid"] = cate.add(cname)
			result["status"] = True
		except Exception as e:
			print e
			result["message"] = "添加分类异常"
		self.write(json.dumps(result))
		self.finish()

	@tornado.web.authenticated
	@tornado.web.asynchronous
	def get(self):
		result = {"status": False}
		try:
			category = {}
			category["common"] = CommonCategory().dist()
			for cate in ["topic", "book", "magazine"]:
				category[cate] = globals()["%sCategory"%cate.capitalize()]().query_all()
			result["message"] = self.render_string("admin/category_manage.html", category=category)
			result["status"] = True
		except Exception as e:
			print e
			result["message"] = "请求分类异常"
		self.write(json.dumps(result))
		self.finish()
	# 更新分类信息
	@tornado.web.authenticated
	@tornado.web.asynchronous
	def put(self):
		result = {"status": False}
		try:
			c_type = self.get_argument("type")
			cid = self.get_argument("cid")
			cname = self.get_argument("cname")
			globals()["%sCategory"%c_type.capitalize()]().update(cid, cname)
			result["status"] = True
		except Exception as e:
			print e
			result["message"] = "修改分类异常"
		self.write(json.dumps(result))
		self.finish()
	# 删除分类
	@tornado.web.authenticated
	@tornado.web.asynchronous
	def delete(self):
		result = {"status" : False}
		try:
			c_type = self.get_argument("type")
			c_id = self.get_argument("cid")
			docs = globals()[c_type.capitalize()]().query_by_cate_id(c_id)
			isdel = False
			if docs:
				result["message"] = "该分类还有文章，无法删除"
			else:
				if c_type == "common":
					sub_cate = CommonCategory().query_by_pid(c_id)
					if sub_cate:
						result["message"] = "该分类有子类，无法删除"
					else:
						isdel = True
				else:
					isdel = True
			if isdel:
				lastrowid = globals()["%sCategory"%c_type.capitalize()]().delete(c_id)
				result["status"] = True
		except Exception as e:
			print e
			result["message"] = "分类删除异常"
		self.write(json.dumps(result))
		self.finish()
