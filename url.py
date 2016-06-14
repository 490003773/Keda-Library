import handler

urls = [
	# index, only get
	(r"/", handler.IndexHandler),
	# login, only post
	(r"/login", handler.LoginHandler),
	# logout, only post
	(r"/logout", handler.LogoutHandler),
	# upload/file, upload/fileinfo
	# get -> upload/ -> upload.html
	# post -> 1. upload/file, async upload file and valid file
	# 		  2. upload/fileinfo, insert into database
	(r"/upload", handler.UploadHandler),
	(r"/ajaxupload", handler.AjaxUploadHandler),
	# cascade query category and generate select list
	# only post
	(r"/category/(\w+)?/(\w+)?", \
			handler.CategoryHandler),
	(r"/view/(\w+)?/(\w+)?", handler.ViewHandler),
	(r"/download/(\w+)?/(\w+)?", handler.DownloadHandler),
	(r"/document", handler.DocumentHandler),
	(r"/verifycode", handler.VerifyCodeHandler),
	# Admin
	(r"/admin", handler.AdminIndexHandler),
	(r"/admin/category", handler.AdminCategoryHandler),
	(r"/admin/user", handler.AdminUserHandler),
	(r"/admin/overview", handler.OverviewHandler),
	(r"/admin/exit", handler.AdminExitHandler),
	(r"/admin/about", handler.AdminAboutHandler),
	(r"/admin/document", handler.AdminDocumentHandler),
	(r"/admin/permission", handler.AdminPermissionHandler)
]
