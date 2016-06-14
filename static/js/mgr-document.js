function request_doc(dtype){
  $.ajax({
    url      : "/admin/document?type="+dtype,
    type     : "GET",
    dataType : "JSON",
    success  : function(data){
                  $("#doc_list").html(data.list);
                  $(".paging").html(data.paging);
                },
    error    : function(){
                  console.log("document slide error")
                }
  });
}

$(function(){
  // Tab页切换
  var oDocSubNav = document.getElementById('doc_sub_nav');
  var aDSNLi = oDocSubNav.getElementsByTagName('li');
  tabControl(aDSNLi);
  request_doc("common");
  $("#doc_sub_nav li").click(function(){
    dtype = $(this).attr("id");
    request_doc(dtype);
  });

  $(".delete").click(function(){
    if (confirm("确认删除?"))
      $("#delete_doc").submit();
    return false;
  });

  $("#delete_doc").submit(function(){
    $.ajax({
      url      : "/admin/document",
      type     : "delete",
      data     : $("#delete_doc").serialize(),
      dataType : "JSON",
      success  : function(data){
                    $("#n_document").click();
                  },
      error    : function(){
                    console.log("error")
                  }
    });
    return false;
  });
})
