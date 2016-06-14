function turn_page(url){
  $.ajax({
    url      : url,
    type     : "GET",
    dataType : "JSON",
    success  : function(data){
                  if (data.status){
                    $("#doc_list").html(data.list);
                    $(".paging").html(data.paging);
                  }
                  else{
                    console.log(data.message);
                  }
                },
    error    : function(){
                  console.log("paging request error")
                }
  });
}
$(function(){
  var type = $("input[name='type']").val();
  var current_page = parseInt($("input[name='current_page']").val());
  var total_pages = parseInt($("input[name='total_pages']").val());
  $("#d_paging a").click(function(){
    var page = $(this).attr("href")
    if (page == "-1"){
      page = current_page - 1;
    }
    else if (page == "+1"){
      page = current_page + 1;
    }
    if (page <= total_pages){
      url = "/admin/document?type="+type+"&page="+page
      turn_page(url)
    }
    return false;
  });
})
