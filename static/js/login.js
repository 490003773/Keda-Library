/*
	login.js
	说明：无刷新登陆， ajax请求验证用户信息
*/
$(function(){
	$("#sign_in_form").submit(function(){
		$.ajax({
			url			 : "/login",
			type		 : "POST",
			data		 : $("#sign_in_form").serialize(),
			dataType : "json",
			success	 : function(data){
										console.log(data)
										if (data.status){
											location.href = "/"
											// $("#login_box").hide()
											// $("#filter").hide()
										}
										else{
											$(".error").html(data.message)
										}
									},
			error		 : function(){
										console.log("error")
									}
		});
		return false;
	});
})
