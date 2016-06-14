# -*- coding:utf-8 -*-

class Category:

	def __init__(self):
		pass

	def query_all(self):
		pass

	def add(self, name, intro, owner, path, cover=""):
		pass

	def delete(self, id):
		pass

	def update(self, id, name):
		pass
'''
def category_index(self, category, prefix):
	categories = {}
	for cate in category:
		id = cate["%s_cate_id"%prefix]
		name = cate["%s_cate_name"%prefix]
		pid = cate["%s_cate_pid"%prefix]
		if pid not in categories.keys():
			categories[pid] = {}
		categories[pid][id] = name
	return categories
'''
