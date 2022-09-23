/*
 * @Author: BDFD
 * @Date: 2022-03-09 22:35:38
 * @LastEditTime: 2022-06-28 13:51:44
 * @LastEditors: BDFD
 * @Description:
 * @FilePath: \SideProject053_LakeBlue\static\javascript\greenampt\form_validation.js
 */
function validateForm() {
	/*function jsonp(url,callback){var oscript=document.createElement("script");if(oscript.readyState){oscript.onreadystatechange=function(){if*/ let pos_real_number =
		/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/;
	let pos_int_number = /^[1-9]+[0-9]*$/;
	let snumbers1 = /^(0+\.?|0*\.\d+|0*1(\.0*)?)$/;
	let snumbers2 = /^(0+\.?|0*\.\d+|1(\.0*)?)$/;
	let listcheck_old = /^\d+(?:,\d+)+(?:,\d+){1,}$/;
	let listcheck =
		/^(?:\s*[+-]?\d+(?:\.\d*)?|\.\d+)*(?:\s*,(?:\s*\d+(?:\.\d*)?|\.\d+)){1,}\s*$/;
	function jsonp(url, callback) {
		var oscript = document.createElement("script");
		if (oscript.readyState) {
			// ie8及以下版本
			oscript.onreadystatechange = function () {
				if (oscript.readyState === "complete" || oscript.readyState === "loaded") {
					callback();
				}
			};
		} else {
			oscript.onload = function () {
				callback();
			};
		}
		oscript.src = url;
		document.body.appendChild(oscript);
	}
	console.log(jsonp);

	function loadScript(url, callback) {
		var oscript = document.createElement("script");
		if (oscript.readyState) {
			// ie8及以下版本
			oscript.onreadystatechange = function () {
				if (oscript.readyState === "complete" || oscript.readyState === "loaded") {
					callback();
				}
			};
		} else {
			oscript.onload = function () {
				callback();
			};
		}
		oscript.src = url;
		document.body.appendChild(oscript);
	}
	console.log(loadScript);

	function ajax(method, url, callback, data, flag) {
		var xhr;
		flag = flag || true;
		method = method.toUpperCase();
		if (window.XMLHttpRequest) {
			xhr = new XMLHttpRequest();
		} else {
			xhr = new ActiveXObject("Microsoft.XMLHttp");
		}
		xhr.onreadystatechange = function () {
			if (xhr.readyState == 4 && xhr.status == 200) {
				console.log(2);
				callback(xhr.responseText);
			}
		};

		if (method == "GET") {
			var date = new Date(),
				timer = date.getTime();
			xhr.open("GET", url + "?" + data + "&timer" + timer, flag);
			xhr.send();
		} else if (method == "POST") {
			xhr.open("POST", url, flag);
			xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
			xhr.send(data);
		}
	}
	console.log(ajax);

	let thetai = document.myForm.thetai.value;
	if (!thetai.match(snumbers1)) {
		alert("请为“土体初始体积含水率”输入一个[0,1]间的数值。");
		document.myForm.thetai.focus();
		return false;
	}

	let thetas = document.myForm.thetas.value;
	if (!thetas.match(snumbers2)) {
		alert("请为“土体孔隙率”输入一个(0,1]间的数值。");
		document.myForm.thetas.focus();
		return false;
	} else if (parseFloat(thetas) <= parseFloat(thetai)) {
		alert("“土体孔隙率”不能小于“土体初始体积含水率”。");
		document.myForm.thetas.focus();
		return false;
	}

	let psi = document.myForm.psi.value;
	if (!psi.match(pos_real_number)) {
		alert("请为“土体吸力水头”输入一个正实数。");
		document.myForm.psi.focus();
		return false;
	} else if (parseFloat(psi) <= 0) {
		alert("请为“土体吸力水头”输入一个正实数。");
		document.myForm.psi.focus();
		return false;
	}

	let k = document.myForm.k.value;
	if (!k.match(pos_real_number)) {
		alert("请为“土体渗透系数”输入一个正实数。");
		document.myForm.k.focus();
		return false;
	} else if (parseFloat(k) <= 0) {
		alert("请为“土体渗透系数”输入一个正实数。");
		document.myForm.k.focus();
		return false;
	}

	let dti = document.myForm.dti.value;
	if (!dti.match(pos_real_number)) {
		alert("请为“时间步长”输入一个正实数。");
		document.myForm.dti.focus();
		return false;
	} else if (parseFloat(dti) <= 0) {
		alert("请为“时间步长”输入一个正实数。");
		document.myForm.dti.focus();
		return false;
	}

	let nin = document.myForm.nin.value;
	if (!nin.match(pos_int_number)) {
		alert("请为“总时间步长数”输入一个正整数。");
		document.myForm.nin.focus();
		return false;
	} else if (parseFloat(nin) <= 0) {
		alert("请为“总时间步长数”输入一个正整数。");
		document.myForm.dti.focus();
		return false;
	}

	let valid = false;
	let iyesno = document.myForm.iyesno;
	for (var i = 0; i < iyesno.length; i++) {
		if (iyesno[i].checked) {
			valid = true;
			break;
		}
	}
	if (!valid) {
		alert("请选择“是否需要生成净雨过程?”");
		console.log(iyesno);
		return false;
	}

	let testvalue = document.getElementById("inlineRadio1").checked;
	let dd = document.myForm.dd.value;
	switch (true) {
		case dd == "" && testvalue:
			alert("请为“地表初期填洼量”输入一个非负的数值。");
			// document.gumbelForm.sdx.focus();
			return false;
		case (!dd.match(pos_real_number) || parseFloat(dd) < 0) && testvalue:
			alert("请为“地表初期填洼量”输入一个非负的数值。");
			// document.gumbelForm.sdx.focus();
			return false;
	}

	let ilist = document.myForm.i.value;
	if (testvalue && ilist == "") {
		alert("请按格式要求输入强度值。（至少应输入2个数值。）");
		// document.myForm.x.focus();
		return false;
	}

	if (testvalue && !ilist.match(listcheck)) {
		alert("请按格式要求输入强度值。（至少应输入2个数值。）");
		// document.myForm.x.focus();
		return false;
	}
}
