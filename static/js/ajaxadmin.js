/*
  ajaxadmin.js
  所有后台管理的异步请求
*/
function nav_select(nav)
{
  var url = "/admin/"+nav;
  // if (nav=="document")
  //   url += "?type=common&page=1"
  $.ajax({
    url      : url,
    type     : "GET",
    dataType : "JSON",
    success  : function(data){
      if (data.status){
        console.log(data)
        if (nav == "exit"){
          $("#main").html(data.message);
        }
        else{
          $("#nav_list").nextAll().remove();
          $("#nav_list").after(data.message);
        }
      }
    },
    error    : function(){
      console.log("nav request error")
    }
  });
}

$(function(){

  nav_select("overview")

  $("#nav_list li").click(function(){
    nav = $(this).attr("id").substr(2);
    nav_select(nav)
  });

})
