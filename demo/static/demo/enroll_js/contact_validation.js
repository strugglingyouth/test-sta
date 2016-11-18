/*表单验证*/
/*姓名*/
function identify1(){
	var reg=/^[\u4E00-\u9FFF]{2,10}$/;
	var va=document.getElementById('name');
	var val=va.value.trim();
	var txt=document.getElementById('name_p');
	var img=document.getElementById('name_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入长度为2-10位的汉字";
		img.src="../static/demo/enroll_images/b_cancel.png";	
		return false;
	}else{
		txt.innerHTML="";
		img.src="../static/demo/enroll_images/b_ok.png";
		return true;
	}
}
/*邮箱*/
function identify2(){
	var reg=/^\d{8}$/;
	var va=document.getElementById('id');
	var val=va.value.trim();
	var txt=document.getElementById('id_p');
	var img=document.getElementById('id_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入8位学号";
		img.src="../static/demo/enroll_images/b_cancel.png";
		return false;
	}else{
		txt.innerHTML="";
		img.src="../static/demo/enroll_images/b_ok.png";
		return true;
	}
}

/*电话*/
function identify3(){
	var reg=/^1[3-8][0-9]{9}$/;
	var va=document.getElementById('phone');
	var val=va.value.trim();
	var txt=document.getElementById('phone_p');
	var img=document.getElementById('phone_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入11位的电话号码";
		img.src="../static/demo/enroll_images/b_cancel.png";
		return false;
	}else{
		txt.innerHTML="";
		img.src="../static/demo/enroll_images/b_ok.png";
		return true;
	}
}
/*班级*/
function identify4(){
	var reg=/^[\u4E00-\u9FFF]{2,}[0-9]{4}$/;
	var va=document.getElementById('major');
	var val=va.value.trim();
	var txt=document.getElementById('major_p');
	var img=document.getElementById('major_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入正确的格式(例:软件1401)";
		img.src="../static/demo/enroll_images/b_cancel.png";
		return false;
	}else{
		txt.innerHTML="";
		img.src="../static/demo/enroll_images/b_ok.png";
		return true;
	}
}
