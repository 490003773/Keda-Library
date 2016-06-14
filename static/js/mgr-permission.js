// 获取当前类别权限
function permission(url){
  $.ajax({
    url      : url,
    type     : "GET",
    dataType : "JSON",
    success  : function(data){
                if (data.status){
                  if (data.pms){
                    if (data.pms.login == 1){
                      $("input[name=login]").prop("checked", true)
                    }
                    if (data.pms.download == 1){
                      $("input[name=download]").prop("checked", true)
                    }
                  }
                  else{
                    $("input[type=checkbox]").prop("checked", false)
                  }
                }
                else{
                  $(".message").text(data.message)
                }
              },
    error    : function(){
                  console.log("permission request error")
                }
  });
}

$(function(){
  // 获取当前类别权限
  permission("/admin/permission?cid="+$("#sort").val())
  $("#sort").change(function(){
    $("input[type=checkbox]").prop("checked", false)
    permission("/admin/permission?cid="+$("#sort").val())
  });

  // 提交权限设置表单
  $("#pms_form").submit(function(){
    $.ajax({
      url      : "/admin/permission",
      type     : "POST",
      data     : $("#pms_form").serialize(),
      dataType : "JSON",
      success  : function(data){
                    if (data.status)
                      $("#n_permission").click();
                    else{
                      $(".message").text(data.message);
                    }
                  },
      error    : function(){
                    console.log("permission add error")
                  }
    });
    return false;
  });
})
