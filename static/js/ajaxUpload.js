/*
	ajaxUpload.js
	1. 异步获取表单
	2. 异步上传文件并判断其类型
*/
$(function(){
	var fileType = ['pdf', 'jpg', 'png', 'doc', 'xls', 'docx', 'ppt', 'wps', 'txt'];
	$("input[type='file']").change(function(){
		// 当选择的文件发生变化时，
		// 清空提示信息以及文件信息的表单
		$(".message").text("")
		var filename = $(this).val()
		if (filename != ""){
			// 判断文件后缀名是否合法
			var dotindex = filename.lastIndexOf(".");
			var suffix = filename.substr(dotindex+1).toLowerCase();
			if ($.inArray(suffix, fileType) != -1){
				// 请求文件信息的表单
				$("#title").attr("placeholder", filename.substr(0,dotindex));
				oubClick();
				$("#cfm_upload_btn").hide();
				// 使用 FormData 异步上传，是 html5 的对象，对浏览器有限制
				var fd = new FormData(document.getElementById("upload"));
				fd.append("_xsrf", $("#upload input[name='_xsrf']").val());
				$.ajax({
					url 				: "/nginxupload",
					type 				: "POST",
					data 				: fd,
					dataType 		: "json",
					processData : false,
					contentType : false,
					success			: function(data){
													// status=True : file is valid
													console.log(data)
													if (data.status){
														$("#cfm_upload_btn").show();
														$("p[class='message']").text("文档上传成功");
														$("#upload_fileinfo input[name='tmp_file']").val(data.filename);
														$(".message").text("");
													}
													else{
														ocfmClick();
														ocuClick();
														$(".message").text(data.message);
														$("#category option:first").attr("selected", "selected")
														subcategory(category, "common", 1);
													}
												},
					error				: function(data, XMLHttpRequest, textStatus, errorThrown){
													$(".message").text(textStatus)
												}
				});
			}
			else{
				// 文件类型错误
				$(".message").text("文件类型错误");
			}
		}
	});
});
