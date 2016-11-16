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
		img.src="images/cancel.png";	
		va.focus();
		return false;
	}else{
		txt.innerHTML="";
		img.src="images/ok.png";
		return true;
	}
}
/*邮箱*/
function identify2(){
	var reg=/^\w+@\w+(\.[a-z]{2,8}){1,2}$/;
	var va=document.getElementById('email');
	var val=va.value.trim();
	var txt=document.getElementById('email_p');
	var img=document.getElementById('email_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入正确的邮箱格式";
		img.src="images/cancel.png";
		va.focus();
		return false;
	}else{
		txt.innerHTML="";
		img.src="images/ok.png";
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
		img.src="images/cancel.png";
		va.focus();
		return false;
	}else{
		txt.innerHTML="";
		img.src="images/ok.png";
		return true;
	}
}
/*班级*/
function identify4(){
	var reg=/^[\u4E00-\u9FFF]{2,}[0-9]{4}$/;
	var va=document.getElementById('class');
	var val=va.value.trim();
	var txt=document.getElementById('class_p');
	var img=document.getElementById('class_i');
	if(!reg.test(val)){
		txt.innerHTML="请输入正确的格式(例:软件1401)";
		img.src="images/cancel.png";
		va.focus();
		return false;
	}else{
		txt.innerHTML="";
		img.src="images/ok.png";
		return true;
	}
}
