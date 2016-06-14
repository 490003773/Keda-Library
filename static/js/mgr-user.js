// Tab页面切换
var oUserManage = document.getElementById('user_manage');
var aUMLi = oUserManage.getElementsByTagName('li');
var aUserFnModule = [
  document.getElementById('um_table'),
  document.getElementById('um_form')
]
tabControl(aUMLi, aUserFnModule);

$("#all_user").click(function(){
  $("#n_user").click();
});
// 表单提交
$("#um_form").submit(function(){
  $.ajax({
    url      : $("#um_form").attr("action"),
    type     : $("#um_form").attr("method"),
    data     : $("#um_form").serialize(),
    dataType : "JSON",
    success  : function(data){
                if (data.status)
                  $("#n_user").click();
                else{
                  $(".message").text(data.message)
                }
              },
    error    : function(){
                  console.log("add user error")
                }
  });
  return false;
});
// 删除用户
$(".delete").click(function(){
  if (confirm("确认删除?"))
    $.ajax({
      url      : $(this).attr("href"),
      type     : "delete",
      data     : {"_xsrf":$("input[name='_xsrf']").val()},
      dataType : "JSON",
      success  : function(data){
                    $("#n_user").click();
                  },
      error    : function(){
                    console.log("delete user error")
                  }
    });
  return false;
});
// 修改用户信息
$(".update").click(function(){
  um_form = $("#um_form");
  um_form.attr("method", "put")
  $("#um_form input[name='username']").val($(this).parent().prev().prev().prev().text());
  $("#um_form input[name='realname']").val($(this).parent().prev().prev().text());
  $("#um_form input[name='password']").prop("required", false);
  um_form.append("<input type='hidden' name='uid' value='"+$(this).attr("href")+"' />");
  $("#um_form input[name='password']").prop("placeholder", "不输入则为原始密码");
  $("#um_form input[type='submit']").val("修改");
  aUMLi[1].innerHTML = "修改"
  aUMLi[1].click();
  return false;
})
