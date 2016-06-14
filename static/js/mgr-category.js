var aAddBtn = document.getElementsByClassName('add_row');
for (var i = 0; i < aAddBtn.length; i++) {
  aAddBtn[i].index = i;
  aAddBtn[i].onclick = function() {
    that = this.index;
    addRow(this, 0, that);
  };
}

var aDataType = [
  '<div class="class_2d">\
    <input type="text" name="cate_name" class="txt txts" \
          placeholder="新分类名" required="required">\
    <cover>\
    <a href="javascript:;" class="delete_row" title="删除" onclick="delRow(this)"></a>\
    </div>',
  '<div class="class_3d">\
    <input type="text" name="cate_name" class="txt txts" \
          placeholder="新分类名" required="required">\
    <a href="javascript:;" class="delete_row" title="删除" onclick="delRow(this)"></a>\
  </div>'
];

function addRow(obj, type, objIndex) {
  $(".edit").html("");
  $(".new_add").remove();
  var iCategory = document.getElementById("category");
  iCategory.value = obj.parentNode.parentNode.id.substr(2);
  var oTbody = document.getElementsByClassName('edit');
  var oTable = obj.parentNode.parentNode.parentNode.parentNode.parentNode;
  var oRow = null;
  if(objIndex + 1) {
    oRow = oTbody[objIndex].insertRow();
  } else {
    oRow = oTable.insertRow(obj.parentNode.parentNode.parentNode.rowIndex + 1);
  }
  oRow.setAttribute('class','new_add');
  oRow.insertCell();
  var oCell = oRow.insertCell();
  var row = aDataType[type];
  // 专题需要上传封面
  if (iCategory.value.indexOf("topic") >= 0)
    row = row.replace("<cover>", "<input type='file' name='cover' required />")
  else {
    row = row.replace("<cover>", "")
  }
  oCell.innerHTML = row;
}
/*
  Name         : delRow
  Description  : 删除一行,两种情况
                1.未添加到数据库中的，直接删除
                2.数据库中存在的，删除前要提示，确认后，从数据库中移除，否则不作处理
*/
function delRow(obj) {
  var oTable = obj.parentNode.parentNode.parentNode.parentNode.parentNode;
  var oTr = obj.parentNode.parentNode.parentNode;
  if (oTr.parentNode.className.match('(children)$') &&  oTr.className!="new_add") {
    if(confirm('是否确认删除?')){
      // oTable.deleteRow(oTr.rowIndex);
      $.ajax({
        url      : obj.href+"&_xsrf="+$("input[name='_xsrf']").val(),
        type     : "delete",
        dataType : "JSON",
        success  : function(data){
                      if (data.status){
                        oTable.deleteRow(oTr.rowIndex);
                        //$("#n_category").click();
                      }
                      else {
                        $(".message").text(data.message);
                      }
                    },
        error    : function(){
                      console.log("delete category error");
                    }
      });
    }
  } else {
    oTable.deleteRow(oTr.rowIndex);
  }
}
/*
  Name         : 修改分类名
  Description  : 如果没有变化，不操作数据库
*/
function update_click(){
  console.log("update");
  // 获取父结点的上一个兄弟节点的input
  pre = $(this).parent().prev().children("div").children("input");
  // 更改编辑状态
  if (pre.prop("readonly")){
    pre.prop("readonly", false);
    pre.attr("name", "cname");
    cname = pre.val();
    pre.focus();
    $(this).attr("value", "确定");
  }
  else{
    modify_cname = $.trim(pre.val());
    if (modify_cname == ""){
      alert("不能为空");
      return false;
    }
    pre.prop("readonly", true);
    pre.attr("name", "");
    pre.blur();
    $(this).attr("value","修改");
    //提交修改
    if (cname != modify_cname){
      id = pre.attr("id").split("_");
      cate_info = {
        "_xsrf" : $("#sort_form input[name='_xsrf']").val(),
        "cname" : modify_cname,
        "cid"   : id.pop(),
        "type"  : id.shift()
      }
      $.ajax({
        url      : "/admin/category",
        type     : "put",
        data     : cate_info,
        dataType : "JSON",
        success  : function(data){
                      console.log(data)
                      if (data.status)
                        //$("#n_category").click();
                        alert("修改成功");
                      else
                        $(".message").text(data.message);
                    },
        error    : function(){
                      console.log("update error")
                    }
      });
    }
  }
  return false;
}
$(".update").click(update_click);

// 提交添加分类表单
$("#sort_form").submit(function(){
  // 可能存在文件，使用FormData进行Ajax上传
  var fd = new FormData(document.getElementById("sort_form"));
  category = $("#sort_form input[name='category']").val()
  cate_name = $("#sort_form input[name='cate_name']").val()
  fd.append("_xsrf", $("#sort_form input[name='_xsrf']").val());
  fd.append("category", category);
  fd.append("cate_name", cate_name);
  $.ajax({
    url         : $("#sort_form").attr("action"),
    data        : fd,
    type        : "POST",
    dataType    : "JSON",
    processData : false,
    contentType : false,
    success     : function(data){
                    if (data.status){
                      alert("添加成功");
                      $(".new_add").append('\
                      <td align="right">\
                        <input type="button" value="修改" class="update" />\
                      </td>');
                      newDiv = $(".new_add").children(":first").next().children()
                      newDiv.parent().attr("id", "t_"+category.split("_")[0]+"_"+data.cid+"")
                      newDiv.html('\
                        <input type="text" class="txt txts"\
                              id="'+category.split("_")[0]+'_'+data.cid+'"\
                              value="'+cate_name+'" readonly />\
                        <a href="/admin/category?type='+category.split("_")[0]+'&cid='+data.cid+'"\
                            class="delete_row" title="删除"\
                            onclick="delRow(this);return false;">\
                        </a>');
                      if ($(".new_add").parent().attr("class")=="edit"){
                        newDiv.append('<a href="javascript:;" \
                                        class="add_row1" title="添加" \
                                        onclick="addRow(this, 1)">\
                                        </a>');
                        $(".new_add").parent().next().append($(".new_add"));
                      }
                      $(".new_add").removeAttr("class");
                      $(".update").off("click");
                      $(".update").click(update_click);
                    }
                    else{
                      $(".message").text(data.message);
                    }
                  },
    error        : function(){}
  });
  return false;
});

// 收起展开项
$("tbody[class$=children]").hide();
$("a[class$=children]").click(function(){
    $("tbody[class="+$(this).attr("class")+"]").toggle(200);
});
