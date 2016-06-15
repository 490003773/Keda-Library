window.onload = function() {
	var oRelates = document.getElementById('relates');
	var oReadRelates = document.getElementById('read_relates');

	var p1 = getPos(oRelates);
	var p2 = getPos(oReadRelates);

	window.onscroll = function() {
		scroll(p1, oRelates);
		scroll(p2, oReadRelates);
	};

	function scroll(p, obj) {
		if (p.top < document.body.scrollTop) {
			obj.style.position = 'fixed';
			obj.style.top = -40 + 'px';
			obj.style.left = p.left + 'px';
		} else {
			obj.style.position = 'static';
		}
	};

	function getPos(obj) {
		var pos = {left: 0, top: 0};
		while(obj) {
			pos.left += obj.offsetLeft;
			pos.top += obj.offsetTop;
			obj = obj.offsetParent;
		}
		return pos;
	}

};
