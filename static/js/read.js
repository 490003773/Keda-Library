window.onload = function() {
	var oRelates = document.getElementById('relates');
	var p = getPos(oRelates);
	window.onscroll = function() {
		if (p.top < document.body.scrollTop) {
			oRelates.style.position = 'fixed';
			oRelates.style.top = -40 + 'px';
			oRelates.style.left = p.left + 'px';
		} else {
			oRelates.style.position = 'static';
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
