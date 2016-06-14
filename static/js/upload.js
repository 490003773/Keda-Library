var oUploadStatus = document.getElementById('upload_status');
var aStatusInfo = oUploadStatus.getElementsByTagName('div');
var oStatusSection1 = document.getElementById('status_1_section');
var oStatusSection2 = document.getElementById('status_2_section');
var oStatusSection3 = document.getElementById('status_3_section');
var oUploadBtn = document.getElementById('upload_btn');
var oCfmUploadBtn= document.getElementById('cfm_upload_btn');
var oCtnUploadBtn = document.getElementById('ctn_upload_btn');

function oubClick(){
	oStatusSection1.style.display = 'none';
	oStatusSection2.style.display = 'block';
	aStatusInfo[0].id = '';
	aStatusInfo[1].id = 'active';
}
//oUploadBtn.onclick = oubClick;

function ocfmClick(){
	oStatusSection2.style.display = 'none';
	oStatusSection3.style.display = 'block';
	aStatusInfo[1].id = '';
	aStatusInfo[2].id = 'active';
}
//oCfmUploadBtn.onclick = ocfmClick;

function ocuClick(){
	oStatusSection3.style.display = 'none';
	oStatusSection1.style.display = 'block';
	aStatusInfo[2].id = '';
	aStatusInfo[0].id = 'active';
}

oCtnUploadBtn.onclick = function() {
	// oStatusSection3.style.display = 'none';
	// oStatusSection1.style.display = 'block';
	// aStatusInfo[2].id = '';
	// aStatusInfo[0].id = 'active';
	location.href = "/upload"
}
