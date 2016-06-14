<!DOCTYPE html>
<html lang="zh-CN">
<head>
	<meta charset="UTF-8">
	<title>{% block title %}首页{% end %}-科达文库</title>
	<link rel="stylesheet" href="{{static_url('css/reset.css')}}">
	<link rel="stylesheet" href="{{static_url('css/public.css')}}">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
	<meta content="" name="keywords">
	<meta content="" name="description">
	<script type="text/javascript" src="{{static_url('js/sub_page.js')}}"></script>
	<script type="text/javascript" src="{{static_url('js/jquery.js')}}"></script>
</head>
<body>
	{% block bd-header %}
	<link rel="stylesheet" href="{{static_url('css/index.css')}}">
	<link rel="stylesheet" href="{{static_url('css/sub_page.css')}}">

	<div id="header">
		<div class="user_bar">
			<div class="wrap">
				<h1 class="fl">您好，欢迎来到科达文库百科！</h1>
				<p class="fr" id="user_section">
					{% if login %}
						<span>Welcome, </span>
						<span>{{username}}</span>
						<a href="/logout" class="login">注销</a>
					{% else %}
						您还没有登录，请 <a href="javascript:;" class="login" id="login">登录</a>
					{% end %}
				</p>
			</div>
		</div>
		<div class="search wrap clear">
			<div class="logo">
				<a href="/"><img src="{{static_url('img/logo.png')}}"></a>
			</div>
			<!-- 搜索 -->
			<div class="search_con">
				<div class="con_tab">
					<a href="#" class="active">文档</a>
					<a href="#">文集</a>
					<a href="#">会员</a>
				</div>
				<form action="#" name="search" method="post">
					<input type="text" id="search_text" name="word" placeholder="请输入关键字查询">
					<input type="submit" id="search_btn" name="submit" value="搜索">
				</form>
			</div>
			<!-- 搜索 END -->
			<img src="{{static_url('img/slogan.png')}}" class="slogan">
		</div>
		<!-- 导航 -->
		<div class="nav">
			<ul class="wrap">
				<li><a href="/">首页</a></li>
				<li class="active"><a class="nav_first" href="/document?type=common">分类</a></li>
				<li><a class="nav_first" href="/document?type=topic">专题</a></li>
				<li><a class="nav_first" href="/document?type=book">图书</a></li>
				<li><a class="nav_first" href="/document?type=magazine">杂志</a></li>
			</ul>
			{% block sub_nav %}
			<div class="nav_class" id="nav_class">
				{% if category %}
					<ul class="nav_title">
						{% for id, name in category[1].items() %}
						<li name="common_{{id}}" id="common_{{id}}">
							<a class="doc_list" href="/document?type=common&cid={{id}}">
								{{name}}<span>></span>
							</a>
						</li>
						{% end %}
					</ul>
					<div class="nav_sub" name="nav_sub" id="nav_sub">
						<i></i>
						<ul>
						{% for subcate in category %}
							{% if subcate != 1 %}
								{% for subid, subname in category[subcate].items() %}
								<li name="common_{{subcate}}">
									<a class="doc_list" href="/document?type=common&cid={{subid}}">{{subname}}</a>
								</li>
								{% end %}
							{% end %}
						{% end %}
						</ul>
					</div>
				{% end %}
			</div>
			{% end %}
			<!-- 登录 -->
			{% block login %}
			{% if not login %}
				<div class="login_box" id="login_box" >
					<div id="close" title="关闭">×</div>
					<h4 id="login_title">用户登录</h4>
					<form action="login" method="post" id="sign_in_form">
						{% raw xsrf_form_html() %}
						<p id="un_wrap">
							<label for="user_name"></label>
							<input type="text" name="username" id="user_name" placeholder="手机号/用户名/邮箱">
						</p>
						<p id="pw_wrap">
							<label for="password"></label>
							<input type="password" name="password" id="password" placeholder="请输入密码">
						</p>
						<span class="error">{{message}}</span>
						<!-- <p id="kl_wrap" class="clear">
							<label for="keep_pw">
								<input type="checkbox" id="keep_pw">
								<span class="checkbox_input"></span>
								记住密码
							</label>
							<a href="#" id="lost_pw" class="fr">忘记密码?</a>
						</p> -->
						<p id="btn_wrap">
							<input type="submit" value="登录" id="sign_in">
							<input type="button" value="注册" id="sign_up">
						</p>
					</form>
				</div>
				{% end %}
			{% end %}
			<!-- 登录 END -->
		</div>
		<!-- 导航 END -->
	</div>
	{% end %}

	{% block bd %}{% end %}

	{% block bd-footer %}
	<div id="footer">
		<p>
			<a href="#">关于我们</a>|
			<a href="#">联系我们</a>|
			<a href="#">加入我们</a>|
			<a href="#">法律声明</a>|
			<a href="#">媒体报道</a>|
			<a href="#">合作伙伴</a>
		</p>
		<p><a href="#">广东科达研发院 ©版权所有</a></p>
	</div>
	{% end %}
</body>
