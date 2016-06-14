#!usr/bin/env python
#coding: utf-8
# 作者：谢勋
# 说明：
# 主要用于创建、修改、删除、验证LDAP用户

import os
import sys
import ldap
from ldap import modlist

# 配置LDAP服务器信息
LDAP_HOST = '10.9.33.81'
USER = 'cn=admin,dc=chinayus,dc=com'
PASSWORD = 'kedaadmin'
BASE_DN = 'dc=chinayus,dc=com'

# 定义一个LDAP工具类
class LDAPTool:
	def __init__(self,ldap_host=None,base_dn=None,user=None,password=None):
		if not ldap_host:
			ldap_host = LDAP_HOST
		if not base_dn:
			self.base_dn = BASE_DN
		if not user:
			user = USER
		if not password:
			password = PASSWORD
		try:
			# 连接LDAP服务器
			self.ldapconn = ldap.open(ldap_host)
			self.ldapconn.simple_bind(user,password)
		except ldap.LDAPError,e:
			print e

    # 搜索LDAP用户
	def ldap_search_dn(self,uid=None):
		# 连接LDAP服务器
		obj = self.ldapconn
		# 设置LDAP协议版本
		obj.protocal_version = ldap.VERSION3
		searchScope = ldap.SCOPE_SUBTREE
		# 设置过滤条件，None为不过滤，搜索所有属性
		retrieveAttributes = None
		# 设置过滤属性，这里只显示cn=uid的信息
		searchFilter = "cn=" + uid
		# 返回搜索结果，不存在则返回None

		try:
			ldap_result_id = obj.search(self.base_dn, searchScope, searchFilter, retrieveAttributes)
			result_type, result_data = obj.result(ldap_result_id, 0)
			if result_type == ldap.RES_SEARCH_ENTRY:
			    return result_data[0][0]
			else:
			    return None
		except ldap.LDAPError, e:
		        print e

    # 查询用户记录，返回用户的属性值
	def ldap_get_user(self,uid=None):
		obj = self.ldapconn
		obj.protocal_version = ldap.VERSION3
		searchScope = ldap.SCOPE_SUBTREE
		retrieveAttributes = None
		searchFilter = "cn=" + uid

        # 查询用户名、邮件地址、中文名
		try:
		    ldap_result_id = obj.search(self.base_dn, searchScope, searchFilter, retrieveAttributes)
		    result_type, result_data = obj.result(ldap_result_id, 0)
		    if result_type == ldap.RES_SEARCH_ENTRY:
		        username = result_data[0][1]['cn'][0]
		        email = result_data[0][1]['mail'][0]
		        nick = result_data[0][1]['sn'][0]
		        result = {'username':username,'email':email,'nick':nick}
		        return result
		    else:
		        return None
		except ldap.LDAPError, e:
		        print e

    # 进行用户名密码验证，验证通过后返回True
	def ldap_get_vaild(self,uid=None,passwd=None):
		obj = self.ldapconn
		# 此处先搜索用户DN
		target_cn = self.ldap_search_dn(uid)

		# 进行用户名密码验证，通过则返回True
		try:
		    if obj.simple_bind_s(target_cn,passwd):
		            return True
		    else:
		            return False
		except ldap.LDAPError,e:
		        print e

    # 修改用户名密码
	def ldap_update_passwd(self,uid=None,oldpass=None,newpass=None):
		modify_entry = [(ldap.MOD_REPLACE,'userpassword',newpass)]
		obj = self.ldapconn
		target_cn = self.ldap_search_dn(uid)

		try:
			obj.simple_bind_s(target_cn,oldpass)
			obj.passwd_s(target_cn,oldpass,newpass)
			# 退出连接LDAP服务器
			obj.unbind_s()
			return True
		except ldap.LDAPError,e:
		    return False

    # 修改用户邮箱,没有邮箱则新增邮箱
	def ldap_update_mail(self,uid=None,newmail=None):
		modify_entry = [(ldap.MOD_REPLACE,'mail',newmail)]
		# 重新以admin身份连接LDAP服务器，因为使用其它用户验证后无权限
		self.ldapconn = ldap.open(LDAP_HOST)
		self.ldapconn.simple_bind(USER,PASSWORD)
		obj = self.ldapconn
		target_cn = self.ldap_search_dn(uid)

		try:
			obj.modify_s(target_cn,modify_entry)
			obj.unbind_s()
			return True
		except ldap.LDAPError,e:
			return False


    # 添加用户
	def ldap_add_user(self,uid=None,password=None,sn=None,mail=None):
		# 连接LDAP服务器
		self.ldapconn = ldap.open(LDAP_HOST)
		self.ldapconn.simple_bind(USER,PASSWORD)
		obj = self.ldapconn
		obj.protocal_version = ldap.VERSION3
		# 定义需要添加的DN
		# 例如：加入用户到keda组
		addDN = ('cn=%s,cn=keda,dc=chinayus,dc=com' %uid)
		# 定义LDAP用户各属性值，可自由增减
		# 定义的属性值，必须LDAP服务器中admin添加objectClass值中存在，否则手动添加
		# 例如：添加uidNumber、homeDirectory、UserName属性值，必须在objectClass中包含posixAccount项
		modlist = {
		        "cn": [uid],
		        "objectClass": ["top","person","organizationalPerson","inetOrgPerson","posixAccount"],
		        "uid": [uid],
		        "sn": [sn],
		        "cn": [uid],
		        "userpassword": [password],
		        "mail": [mail],
		        # uidNumber可重复
		        "uidNumber": ["1000"],
		        # gidNumber为keda的组编号
		        "gidNumber": ["501"],
		        "loginShell": ["/bin/sh"],
		        "homeDirectory": ["/home/users/%s" %uid]
		}

		# 格式化modlist需要增加的属性值
		modlist = ldap.modlist.addModlist(modlist)

		# 将新增用户及属性值添加至LDAP服务器
		try:
			obj.add_s(addDN, modlist)
			obj.unbind_s()
			return True
		except ldap.LDAPError,e:
			return False


    # 删除用户
	def ldap_del_user(self,uid=None):
		# 连接LDAP服务器
		self.ldapconn = ldap.open(LDAP_HOST)
		self.ldapconn.simple_bind(USER,PASSWORD)
		obj = self.ldapconn
		try:
			target_cn = self.ldap_search_dn(uid)
			obj.delete_s(target_cn)
			obj.unbind_s()
			return True
		except ldap.LDAPError,e:
			return False


if __name__ == "__main__":
		# LDAPTool的用法，先进行类的实例化
        a = LDAPTool()
        # 搜索用户
        b = a.ldap_search_dn('xiexun')
        # 搜索用户信息
        c = a.ldap_get_user('wangzd')
        print c
        # 进行用户验证
        d = a.ldap_get_vaild('xiexun','xiexun')
        print d
        # 修改用户密码
        e = a.ldap_update_passwd('xiexun','xiexun','xiexun')
        print e
        # 修改用户邮箱
        f = a.ldap_update_mail('bbb','xie_xun@126.com')
        print f
        # 新增用户
        g = a.ldap_add_user('abc','abc','用户名','test@kedachina.com.cn')
        print g
        # 删除用户
        h = a.ldap_del_user('dfff')
        print h
