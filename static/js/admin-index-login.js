var oLoginIn = document.getElementById('login_in');
var oLoginInBtn = document.getElementById('login_in_btn');
$(function(){
  // 登录
  $("#sign_in").submit(function(){
    $.ajax({
      url      : "/admin",
      type     : "POST",
      data		 : $("#sign_in").serialize(),
      dataType : "json",
      success  : function(data){
                    console.log(data)
                    if (data.status){
                      location.href = "/admin"
                    }
                    else{
                      // 失败，刷新验证码
                      $("#flushcode").click();
                      $(".message").text(data.message)
                    }
                  },
      error    : function(){
                    console.log("admin login error")
                  }
    });
    return false;
  });

  // 刷新验证码
  $("#flushcode").click(function(){
    $.ajax({
      url      : $(this).attr("href"),
      type     : "GET",
      dataType : "JSON",
      success  : function(data){
                    $("#flushcode img").attr("src", "/static/img/verifycode/"+data)
                  },
      error    : function(){
                    console.log("flush code error")
                  }
    });
    return false;
  });
});
