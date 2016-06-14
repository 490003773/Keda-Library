var oControlPanel = document.getElementById('control_panel');
var aFnModule = [
	document.getElementById('overview'),
	document.getElementById('sort_manage'),
	document.getElementById('authority_manage'),
	document.getElementById('doc_manage'),
	document.getElementById('user_manage'),
	document.getElementById('library_info')
];
var aFnModuleLen = aFnModule.length;
var oNavList = document.getElementById('nav_list'); //The navigation of the control panel.
var aLi = oNavList.getElementsByTagName('li');

tabControl(aLi, aFnModule, function() {
	oControlPanel.style.display = 'none';
	oLoginOut.className = '';
});
/*
*	If an element belongs to an array,this function will be returning the index of this element.
*	If not,it returns -1.
*/
function arrIndexOf(arr, v) {
	for (var i = 0; i < arr.length; i++) {
		if (arr[i] == v) {
			return i;
		}
	}
	return -1;
}

function addClass(obj, className) {
	if (obj.className == '') {
		// if class value is empty.
		obj.className = className;
	} else {
		// if class value isn't empty.
		var arrClassName = obj.className.split(' ');
		var _index = arrIndexOf(arrClassName, className);
		if (_index == -1) {
			//if class value isn't repeated.
			obj.className += ' ' + className;
		}
	}
}

function removeClass(obj, className) {
	if (obj.className != '') {
		// if class value isn't empty.
		var arrClassName = obj.className.split(' ');
		var _index = arrIndexOf(arrClassName, className);
		if (_index != -1) {
			//and the className for deletion exist.
			arrClassName.splice(_index, 1);
			obj.className = arrClassName.join(' ');
		}
	}
}

function tabControl(tabList, fnModuleList, endFn) {
	var tabListLen = tabList.length;
	for (var i = 0; i < tabListLen; i++) {
		tabList[i].index = i;
		tabList[i].onclick = function() {
			for (var i = 0; i < tabListLen; i++) {
				removeClass(tabList[i], 'active');
			}
			addClass(this, 'active');
			try{
				if(fnModuleList) {
					var fnModuleListLen = fnModuleList.length;
					for (var j = 0; j < fnModuleListLen; j++) {
							fnModuleList[j].style.display = 'none';
					}
					if (this.index > fnModuleListLen - 1) {
						// if the tabList is longer than the fnModuleList, a function(if it exists) will be called when the extra list item is clicked.
						endFn && endFn();
					} else {
						// Every list item  matches its corresponding function module.
						fnModuleList[this.index].style.display = 'block';
					}
				}
			}
			catch (e) {
				;
			}
		};
	}
}

// function oLoginClick(e){
// 	oLoginIn.style.display = 'none';
// 	oControlPanel.style.display = 'block';
// }
// oLoginInBtn.onclick = oLoginClick;

// tabControl(aLi, aFnModule, function() {
// 	oControlPanel.style.display = 'none';
// 	oLoginOut.className = '';
// });
