var oNavClass = document.getElementById('nav_class');
var aNavLi = oNavClass.getElementsByTagName('li');
var oSub = document.getElementById('nav_sub');
var iLiHeigth = 39;
$(".nav_title").hover(
	function(){
		$("#nav_sub").addClass("hover");
	},
	function(){
		$("#nav_sub").removeClass("hover");
		$("#nav_sub").hide();
	}
);
$("#nav_sub").hover(
	function(){
		$(this).show();
	},
	function(){
		$(this).hide();
	}
);
$(".nav_title li[name^=common_]").hover(
	function(){
		$("#nav_sub li[name="+$(this).attr("name")+"]").show();
		$("#nav_sub li[name!="+$(this).attr("name")+"]").hide();
		$("#nav_sub").css("top", $(this).index() * iLiHeigth + 65 + 'px');
		$("#nav_sub").css("background-color", "#f7fbfb");
		$("#nav_sub").show();
	},
	function(){
		if (!$("#nav_sub").hasClass("hover")){
			$("#nav_sub li[name="+$(this).attr("name")+"]").hide();
			$("#nav_sub").hide();
		}
	}
);

// function hoverShowSubNav(aNavList, iLiHeigth, oNavSub) {
// 	var aSubLi = oNavSub.getElementsByTagName('li');
// 	var that;
// 	var anlLen = aNavList.length;
// 	var aslLen = aSubLi.length;
// 	for (var i = 0; i < anlLen; i++) {
//
// 		aNavList[i].index = i;
// 		function over() {
// 			oNavSub.style.display = 'block';
// 			that.style.backgroundColor = '#f7fbfb';
// 		}
// 		function out() {
// 			oNavSub.style.display = 'none';
// 			that.style.backgroundColor = '';
// 		}
//
// 		aNavList[i].onmouseover = function() {
// 			that = this;
// 			oNavSub.style.top = this.index * iLiHeigth + 65 + 'px';
// 			over();
// 		}
// 		oNavSub.onmouseover = over;
// 		aNavList[i].onmouseout = oNavSub.onmouseout = out;
// 		for (var j = 0; j < aslLen; j++) {
// 			aSubLi[j].onmouseover = over;
// 			aSubLi[j].onmouseout = out;
// 		}
// 	}
// }
//
// hoverShowSubNav(aNavLi, 39, oSub);

var oLogin = document.getElementById('login');
var oLoginBox = document.getElementById('login_box');
var oClose = document.getElementById('close');
var oLoginTitle = document.getElementById('login_title');
var oUserName = document.getElementById('user_name');
var oFilter = document.getElementById('filter');

function getStyle(obj, attr) {
	return obj.currentStyle ? obj.currentStyle[attr] : getComputedStyle(obj)[attr];
}

function shake(obj, attr, step, interval, endFn) {
	var	num = 0;
	var arr = [];
	var pos = parseInt(getStyle(obj, attr));

	for(var i = step; i > 0; i -= 2) {
		arr.push(i, -i);
	}
	arr.push(0);

	clearInterval(obj.timer);
	obj.timer = setInterval(function() {
		obj.style[attr] = pos + arr[num] + 'px';
		num++;
		if (num == arr.length) {
			clearInterval(obj.timer);
			endFn && endFn();
		}
	}, interval)
}
if (oLogin)
	oLogin.onclick = function() {
		oLoginTitle.style.color = '#000';
		oLoginBox.style.background = 'rgba(255,255,255,1)';
		oClose.style.display = 'block';
		oFilter.style.display = 'block';
		oUserName.focus();
		shake(oLoginBox, 'right', 10, 30);
	}
if (oClose)
	oClose.onclick = function() {
		oLoginTitle.style.color = '#fff';
		oLoginBox.style.background = 'rgba(0,0,0,0.4)';
		oClose.style.display = 'none';
		oFilter.style.display = 'none';
	}
