# -*- coding:utf-8 -*-
import os.path

settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
	static_path=os.path.join(os.path.dirname(__file__), "static"),
	temp_path=os.path.join(os.path.dirname(__file__), "tmp"),
	module_path=os.path.join(os.path.dirname(__file__), "modules"),
	conf_path=os.path.join(os.path.dirname(__file__), "conf"),
	debug=True,
	cookie_secret="AGXX++GhTO2vnDHJ9g9Tp/kcfebMwkO/nlredcRWPPI=",
	xsrf_cookies=True,
	login_url="/login",
	admin_login_url="/admin"
)
