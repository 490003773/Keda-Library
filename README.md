科达文库
==
运行环境
--
- 操作系统 : Ubuntu16.04
- 开发语言 : Python
- 框架 : tornado
- 数据库 : mysql5.7
- 系统工具 : imagemagick, libreoffice, pdf2htmlex
 - sudo apt-get install imagemagick
 - sudo apt-get install libreoffice
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
