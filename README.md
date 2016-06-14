科达文库
==
运行环境
--
- 操作系统 : Ubuntu-16.04
- 服务器 : Nginx-(需要手动编译安装)
 - 插件 : nginx_upload_module
 - 依赖 : openssl, zlib, pcre
- 开发语言 : Python
 - 框架 : tornado
 - 第三方库 :
    - MySQLDb
    - pillow
    - ldap
    - pypdf
- 数据库 : mysql5.7
- 系统工具
  - imagemagick
    - sudo apt-get install imagemagick
  - libreoffice
    - sudo apt-get install libreoffice
  - pdf2htmlex
    - sudo apt-get install pdf2htmlex

文件、文件夹说明
--
- conf : 需要的配置文件
 - db_config : 数据库配置
 - font_config : 字体配置
 - ftype : 上传文件白名单
 - paging_config : 分页设置
- fonts : 字体文件
- handler : 网站路由
- modules : 功能扩展以及数据库操作
- static : 静态文件
 - css : 样式表
 - js : javascript脚本
 - img : 图片
 - file : 存放文档
- templates : html文件
- tmp : 文档上传临时路径
