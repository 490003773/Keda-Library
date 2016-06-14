# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.httpclient

import os
from settings import settings
from url import urls

from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

class LibraryApplication(tornado.web.Application):

	def __init__(self):
		tornado.web.Application.__init__(self, handlers=urls, **settings)

def main():
	tornado.options.parse_command_line()
	print "Run on the port: %d" % options.port
	http_server = tornado.httpserver.HTTPServer(LibraryApplication())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
