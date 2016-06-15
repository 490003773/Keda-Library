window.onload = function() {
 	var aNavFirst = document.getElementsByClassName('nav_first');
	var oSubPageNav = document.getElementById('sub_page_nav');
	var oH4 = document.getElementById('sub_page_l');
  if (oH4)
    oH4 = oH4.getElementsByTagName('h4')[0];
	var oConLi = document.getElementById('con_li');

	var oSecUl = document.createElement('ul');
	oSecUl.setAttribute('id', 'sec_ul');
	oSecUl.setAttribute('class', 'clear');

	var aNavCommon = document.getElementsByClassName('doc_list');
	for (var j = 0; j < aNavCommon.length; j++) {
		aNavCommon[j].onclick = function() {
      oSubPageNav.innerHTML = '';
      oH4.innerHTML = '';
      oConLi.innerHTML = '';
      href = this.href;
      var urlType = href.split('type=')[1].split('&')[0];
      var sUrl = 'document?type=' + href.split('type=')[1];

			ajax('get', sUrl, '', function(rData) {
				var commonUl = document.createElement('ul');
				commonUl.setAttribute('id', 'commonUl');
				commonUl.setAttribute('class', 'clear');
        var pid = 0;
        for (var i = 0; i < rData['doc_cate'].length; i++){
          if (rData['doc_cate'][i]['id'] == href.split('cid=')[1]){
            pid = rData['doc_cate'][i]['pid'];
            break;
          }
        }
				for (var i = 0; i < rData['doc_cate'].length; i++) {
					if (rData['doc_cate'][i]['pid'] == 1) {
						str = '<li class="fl <active>"><a class="commonUlLiA" href="document?type=common&cid=' + rData['doc_cate'][i]['id'] + '">' + rData['doc_cate'][i]['name'] + '</a></li>';
            if ((pid == 1 && rData['doc_cate'][i]['id'] == href.split('cid=')[1])
              || (pid != 1 && pid == rData['doc_cate'][i]['id']))
							str = str.replace("<active>", "active");
						else
							str = str.replace('<active>', '');
						commonUl.innerHTML += str;
					}
				}
				oSubPageNav.appendChild(commonUl);
				showCon(sUrl, '');
			});
              document.body.scrollTop = 0;
              showMain(false);
              return false;
		}
	}


	document.addEventListener('DOMSubtreeModified', function(event) {
		var aCommonUlLiA = document.getElementsByClassName('commonUlLiA');
		for (var i = 0; i < aCommonUlLiA.length; i++) {
			aCommonUlLiA[i].onclick = function() {
				for (var i = 0; i < aCommonUlLiA.length; i++) {
					aCommonUlLiA[i].parentNode.style.background = '#e6e6e6';
				}
				this.parentNode.style.background = '#fff';
				var sUrl = 'document?type=common&cid=' + this.href.split('cid=')[1];

				showCon(sUrl, '');

				return false;
			}
		}
	});

	for (var i = 0; i < aNavFirst.length; i++) {
		aNavFirst[i].index = i;
		aNavFirst[i].onclick = function() {
			oSubPageNav.innerHTML = '';
			for (var i = 0; i < aNavFirst.length; i++) {
				if (i < 4) {
					aNavFirst[i].style.background = '#19a97b';
				} else {
					document.body.scrollTop = 0;
				}
			}
			if (this.index > 3) {
				this.index -= 3;
			}
			aNavFirst[this.index].style.background = '#019875';
			showMain(false);

			switch(this.index) {
				case 0:
					// showMain(true);
          location.href = "/"
					break;
				case 1:
					showCon('topic');
					break;
				case 2:
					showCon('book');
					break;
				case 3:
					showCon('magazine');
					break;
			}

			return false;
		};
	}

	// Get all selectors by class name that were dynamically appended in vanilla JavaScript.
	document.addEventListener('DOMSubtreeModified', function(event) {
		var aSecLi = document.getElementsByClassName('li2');
		for (var i = 0; i < aSecLi.length; i++) {
			aSecLi[i].onclick = function() {
				for (var i = 0; i < aSecLi.length; i++) {
					aSecLi[i].style.color = '#666';
				}
				showCon(this.href.split('type=')[1], this.className);
				this.style.color = '#19a97b';
				oH4.innerHTML = this.innerHTML;
				return false;
			};
		}
		try {
			aSecLi[0].onclick = function() {
				if (this.type.indexOf('common') == -1) {
					showCon(this.type.split('&')[0], '');
				} else {
					showCon(this.type);
				}
			};
		} catch(e) {}
	});

	function showCon(urlType, obj) {
		if (urlType.indexOf('common') != -1) {
			if (urlType.indexOf('common') == 0) {
				var sUrl = 'document?type=' + urlType;
			} else {
				var sUrl = urlType;
			}
			var iCid = sUrl.split('cid=')[1];
			urlType = 'common';
			ajax('get', sUrl, '', function(rData) {
				if (obj != 'li2') {
					secUl(urlType, rData, iCid);
					oH4.innerHTML = '全部';
				}
				conLi(urlType, rData);
			});
		} else {
			var sUrl = 'document?type=' + urlType;
			ajax('get', sUrl, '', function(rData) {
				if ((urlType == 'topic') || (urlType == 'book') || (urlType == 'magazine')) {
					secUl(urlType, rData, '');
					oH4.innerHTML = '全部';
					document.getElementsByClassName('li2')[0].style.color = '#19a97b';
				}
				conLi(urlType, rData);
			});
		}
	}

	function ajax(method, url, data, success) {
		var xhr = null;
		try {
			xhr = new XMLHttpRequest();
		} catch (e) {
			xhr = new ActiveXObjext('Microsoft.XMLHTTP');
		}

		if (method == 'get' && data) {
			url += '?' + data;
		}
    if (url[0] != "/")
      url = "/"+url;
		xhr.open(method, url, true);
		if (method == 'get') {
			xhr.send();
		} else {
			xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
			xhr.send(data);
		}

		xhr.onreadystatechange = function() {
			if (xhr.readyState == 4) {
				if (xhr.status == 200) {
					success && success(JSON.parse(xhr.responseText));
				} else {
					alert('出错了,Err: ' + xhr.status);
				}
			}
		}
	}

	function secUl(urlType, rData, cid) {
    oSecUl.innerHTML = '';
    var pid = 0;
    for (var i = 0; i < rData['doc_cate'].length; i++){
      if (rData['doc_cate'][i]['id'] == cid){
        pid = rData['doc_cate'][i]['pid'];
        break;
      }
    }
    str = '<li class="fl"><a class="li2 <active>" href="javascript:;" type="' + urlType + '&cid=' + cid + '">全部</a></li>';
    if (pid != 1)
      str = str.replace("<active>", "");
    else
      str = str.replace('<active>', 'active');
    for (var i = 0; i < rData['doc_cate'].length; i++) {
			if (urlType == 'common') {
        if ((pid == 1 && rData['doc_cate'][i]['pid'] == cid) || (pid != 1 && rData['doc_cate'][i]['pid'] == pid)) {
            str += '<li class="fl"><a class="li2 <active>" href="/document?type=' + urlType + '&cid=' + rData['doc_cate'][i]['id'] + '">' + rData['doc_cate'][i]['name'] + '</a></li>';
            if (rData['doc_cate'][i]['id'] == cid)
              str = str.replace("<active>", "active");
            else
              str = str.replace('<active>', '');
        }
			} else {
				str += '<li class="fl"><a class="li2" href="/document?type=' + urlType + '&cid=' + rData['doc_cate'][i]['id'] + '">' + rData['doc_cate'][i]['name'] + '</a></li>';
			}
		}
    oSecUl.innerHTML += str;
    oSubPageNav.appendChild(oSecUl);
	}

	function conLi(urlType, rData) {
		oConLi.innerHTML = '';
		if (rData['docs'].length == 1) {
			//alert('此分类没有文件');
      oConLi.innerHTML = '此分类没有文件';
		}
		aUrlType = urlType.split('&');
		for (var j = 0; j < rData['docs'].length - 1; j++) {
			oConLi.innerHTML += '<li class="clear"><div class="fl"><a href="/view/'+ aUrlType[0] + '/' + rData['docs'][j]['id'] + '"><img src="http://10.9.36.201/static/' + rData['docs'][j]['cover'] + '"></a></div>'
							 + '<div class="fl"><h5><a href="/view/' + urlType + '/' + rData['docs'][j]['id'] + '">' + rData['docs'][j]['name'] + '</a><span class="fr">' + rData['docs'][j]['mtime'] + "</span></h5>"
							 + '<p>' + rData['docs'][j]['intro'] + '</p></div></li>';
		}
	};


	function showMain(bl) {
    var login_box = document.getElementById('login_box');
    var nav_class = document.getElementById('nav_class');
    var main = document.getElementById('main');
    var sub_page = document.getElementById('sub_page');
		if (bl) {
      if (nav_class)
			  nav_class.style.display = 'block';
      if (login_box)
			   login_box.style.display = 'block';
      if (main)
			   main.style.display = 'block';
      if (sub_page)
			   sub_page.style.display = 'none';
		} else {
      if (nav_class)
			  nav_class.style.display = 'none';
      if (login_box)
			   login_box.style.display = 'none';
      if (main)
			   main.style.display = 'none';
      if (sub_page)
			   sub_page.style.display = 'block';
		}
	}

};
