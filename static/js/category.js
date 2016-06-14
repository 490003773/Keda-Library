/*
	category.js
	说明：获取级联菜单
	selector : 当前操作的标签
	cname 	 : 四大分类中的一个，[book, topic, magazine, common]
	cid 	 : 当前选择的分类的id
*/
function subcategory(selector, cname, cid)
{
	$.ajax({
		url 		: "/category/"+cname+"/"+cid,
		type 		: "GET",
		success : function(data){
								selector.nextAll("select").remove()
								selector.after(data)
							},
		error 	: function(){
								console.log("request error")
							}
	})
}
