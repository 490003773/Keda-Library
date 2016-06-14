/*
	fileInfo.js
	说明：1. 请求获取级联菜单
		 2. 如有必要，动态添加表单额外信息
		 3. ajax 提交文件信息，包括文件名，文件描述，文件类型
*/
$(function(){
	var book = "\
				<label for='author'>\
					<span>作者</span>\
					<input type='text' name='author' required='required' />\
				</label>",
	 		magazine = "\
				<label for='publisher'>\
					<span>出版社</span>\
					<input type='text' name='publisher' required='required' />\
				</label>\
				<label for='issue'>\
					<span>刊号</span>\
					<input type='text' name='issue' required='required' />\
				</label>",
	 		common = "", topic = "";
	var category = $("#category");
	subcategory(category, "common", 1);
	category.change(function(){
		$("#extra").html("");
		var cval = category.val();
		subcategory(category, cval, 1);
		$("#extra").html(eval(cval));
	});
	// 提交表单
	var upload_fileinfo = $("#upload_fileinfo");
	upload_fileinfo.submit(function(){
		$("#cfm_upload_btn").hide();
		$.ajax({
			url			 : upload_fileinfo.attr("action"),
			type 		 : "POST",
			data 		 : upload_fileinfo.serialize(),
			dataType : "json",
			success	 : function(data){
										console.log(data)
										if (data.status){
											//上传成功
											ocfmClick();
											$("#cfm_upload_btn").show();
										}
										else{
											$(".message").text(data.message);
										}
									},
			error		 : function(){
										console.log("fileinfo submit error");
									}
		});
		return false;
	})

})
