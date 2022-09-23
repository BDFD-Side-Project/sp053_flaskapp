/*
 * @Author: BDFD
 * @Date: 2022-03-08 10:24:33
 * @LastEditTime: 2022-06-17 12:02:35
 * @LastEditors: BDFD
 * @Description:
 * @FilePath: \SideProject053_LakeBlue\static\javascript\wavespectra\form_validation.js
 */
function validateForm() {
	/*console.log("msg from wave validtin function!");function jsonp(url,callback){var oscript=document.createElement("script");if(oscript.readyState){oscript.onreadystatechange=function(){if(oscript.readyState==="complete"||oscript.readyState==="loaded")*/ let pos_real_number =/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/; /*{callback()}}}else{oscript.onload=function(){callback()}}oscript.src=url;document.body.appendChild(oscript)}*/

	console.log(jsonp);
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

	let c1 = document.waveForm.radio.value;
	console.log("type is ", c1);
	if (c1 == 1) {
		let d = document.waveForm.d.value;
		switch (true) {
			case d == "":
				// alert("d 无任何输入,作为None输出");
				break;
			case d.trim() == "":
				// alert("d 输入为空格,作为None输出");
				break;
			case !d.match(pos_real_number) || parseFloat(d) <= 0:
				alert("输入的 d 值必须大于零。");
				document.waveForm.d.focus();
				return false;
		}

		let X_1 = document.waveForm.X_1.value;
		switch (true) {
			case X_1 == "" && d == "":
				alert("d 和 X 不能都为空。");
				document.waveForm.X_1.focus();
				return false;
			case X_1.trim() == "" && d.trim() == "":
				alert("d 和 X 不能都为空。");
				document.waveForm.X_1.focus();
				return false;
			case X_1 == "":
				// alert("X 无任何输入,作为None输出");
				break;
			case X_1.trim() == "":
				// alert("X 输入为空格,作为None输出");
				break;
			case !X_1.match(pos_real_number) || parseFloat(X_1) <= 0:
				alert("输入的 X 值必须大于零。");
				document.waveForm.X_1.focus();
				return false;
		}

		let U_1 = document.waveForm.U_1.value;
		switch (true) {
			case U_1 == "" && d == "":
				alert("d 和风要素(U、z) 不能都为空。");
				document.waveForm.U_1.focus();
				return false;
			case U_1.trim() == "" && d.trim() == "":
				alert("d 和风要素(U、z) 不能都为空。");
				document.waveForm.U_1.focus();
				return false;
			case U_1 == "":
				// alert("U 无任何输入,作为None输出");
				break;
			case U_1.trim() == "":
				// alert("U 输入为空格,作为None输出");
				break;
			case !U_1.match(pos_real_number) || parseFloat(U_1) <= 0:
				alert("输入的 U 值必须大于零。");
				document.waveForm.U_1.focus();
				return false;
		}

		let el_1 = document.waveForm.el_1.value;
		switch (true) {
			case el_1 == "" && U_1 == "":
				// alert("el 和 U 同时不输入");
				break;
			case el_1.trim() == "" && U_1.trim() == "":
				// alert("el和U 可以输入为空格 但是必须同时不输入,或者同时输入");
				break;
			case el_1 == "" || U_1 == "":
				alert("z 和 U 必须同时输入。");
				document.waveForm.el_1.focus();
				return false;
			case el_1.trim() == "" || U_1.trim() == "":
				alert("z 和 U 必须同时输入。");
				document.waveForm.el_1.focus();
				return false;
			case el_1 == "":
				// alert("el 无任何输入,作为None输出");
				break;
			case el_1.trim() == "":
				// alert("el 输入为空格,作为None输出");
				break;
			case !el_1.match(pos_real_number) || parseFloat(el_1) <= 0:
				alert("输入的 z 值必须大于零。");
				document.waveForm.el_1.focus();
				return false;
		}

		let gamma_1 = document.waveForm.gamma_1.value;
		switch (true) {
			case gamma_1 == "":
				// alert("gamma 无任何输入,作为None输出");
				break;
			case gamma_1.trim() == "":
				// alert("gamma 输入为空格,作为None输出");
				break;
			case !gamma_1.match(pos_real_number) ||
				parseFloat(gamma_1) < 1 ||
				parseFloat(gamma_1) > 7:
				alert("输入的 γ 值必须在[1,7]中。");
				document.waveForm.gamma_1.focus();
				return false;
		}

		let Hs_1 = document.waveForm.Hs_1.value;
		switch (true) {
			case Hs_1 == "":
				// alert("H(1/3) 无任何输入,作为None输出");
				break;
			case Hs_1.trim() == "":
				// alert("H(1/3) 输入为空格,作为None输出");
				break;
			case !Hs_1.match(pos_real_number) || parseFloat(Hs_1) <= 0:
				alert("输入的 H1/3 值必须大于零。");
				document.waveForm.Hs_1.focus();
				return false;
		}

		let Tz_1 = document.waveForm.Tz_1.value;
		switch (true) {
			case Tz_1 == "":
				// alert("Tz 无任何输入,作为None输出");
				break;
			case Tz_1.trim() == "":
				// alert("Tz 输入为空格,作为None输出");
				break;
			case !Tz_1.match(pos_real_number) || parseFloat(Tz_1) <= 0:
				alert("输入的 Tz 值必须大于零。");
				document.waveForm.Tz_1.focus();
				return false;
		}

		let Ts_1 = document.waveForm.Ts_1.value;
		switch (true) {
			case Ts_1 == "":
				// alert("Ts 无任何输入,作为None输出");
				break;
			case Ts_1.trim() == "":
				// alert("Ts 输入为空格,作为None输出");
				break;
			case !Ts_1.match(pos_real_number) || parseFloat(Ts_1) <= 0:
				alert("输入的 T1/3 值必须大于零。");
				document.waveForm.Ts_1.focus();
				return false;
		}
	}
	if (c1 == 2) {
		// let X_2 = document.waveForm.X_2.value;
		// switch (true) {
		// 	case X_2 == "":
		// 		// alert("d 无任何输入,作为None输出");
		// 		break;
		// 	case X_2.trim() == "":
		// 		// alert("d 输入为空格,作为None输出");
		// 		break;
		// 	case !X_2.match(pos_real_number) || parseFloat(X_2) <= 0:
		// 		alert("请为“X_2”指定一个正实数。");
		// 		document.waveForm.X_2.focus();
		// 		return false;
		// }
		let U_2 = document.waveForm.U_2.value;
		switch (true) {
			case U_2 == "":
				// alert("U_2 无任何输入,作为None输出");
				break;
			case U_2.trim() == "":
				// alert("U_2 输入为空格,作为None输出");
				break;
			case !U_2.match(pos_real_number) || parseFloat(U_2) <= 0:
				alert("输入的 U 值必须大于零。");
				document.waveForm.U_2.focus();
				return false;
		}

		let el_2 = document.waveForm.el_2.value;
		switch (true) {
			case el_2 == "" && U_2 == "":
				// alert("el_2 和 U_2 同时不输入");
				break;
			case el_2.trim() == "" && U_2.trim() == "":
				// alert("el_2 和 U_2 可以输入为空格 但是必须同时不输入,或者同时输入");
				break;
			case el_2 == "" || U_2 == "":
				alert("z 和 U 必须同时输入。");
				document.waveForm.el_2.focus();
				return false;
			case el_2.trim() == "" || U_2.trim() == "":
				alert("z 和 U 必须同时输入。");
				document.waveForm.el_2.focus();
				return false;
			case el_2 == "":
				// alert("el 无任何输入,作为None输出");
				break;
			case el_2.trim() == "":
				// alert("el 输入为空格,作为None输出");
				break;
			case !el_2.match(pos_real_number) || parseFloat(el_2) <= 0:
				alert("输入的 z 值必须大于零。");
				document.waveForm.el_2.focus();
				return false;
		}

		let gamma_2 = document.waveForm.gamma_2.value;
		switch (true) {
			case gamma_2 == "":
				// alert("gamma 无任何输入,作为None输出");
				break;
			case gamma_2.trim() == "":
				// alert("gamma 输入为空格,作为None输出");
				break;
			case !gamma_2.match(pos_real_number) ||
				parseFloat(gamma_2) < 1 ||
				parseFloat(gamma_2) > 7:
				alert("输入的 γ 值必须在[1,7]中。");
				document.waveForm.gamma_2.focus();
				return false;
		}

		let Hs_2 = document.waveForm.Hs_2.value;
		switch (true) {
			case U_2 == "" && Hs_2 == "":
				alert("H1/3 和风要素(U、z) 不能都为空。");
				document.waveForm.Hs_2.focus();
				return false;
			case U_2.trim() == "" && Hs_2.trim() == "":
				alert("H1/3 和风要素(U、z) 不能都为空。");
				document.waveForm.Hs_2.focus();
				return false;
			case Hs_2 == "":
				// alert("H(1/3)_2 无任何输入,作为None输出");
				break;
			case Hs_2.trim() == "":
				// alert("H(1/3)_2 输入为空格,作为None输出");
				break;
			case !Hs_2.match(pos_real_number) || parseFloat(Hs_2) <= 0:
				alert("输入的 H1/3 值必须大于零。");
				document.waveForm.Hs_2.focus();
				return false;
		}

		let Tz_2 = document.waveForm.Tz_2.value;
		switch (true) {
			case Tz_2 == "":
				// alert("Tz 无任何输入,作为None输出");
				break;
			case Tz_2.trim() == "":
				// alert("Tz 输入为空格,作为None输出");
				break;
			case !Tz_2.match(pos_real_number) || parseFloat(Tz_2) <= 0:
				alert("输入的 Tz 值必须大于零。");
				document.waveForm.Tz_2.focus();
				return false;
		}

		let Ts_2 = document.waveForm.Ts_2.value;
		switch (true) {
			case Ts_2 == "":
				// alert("Ts 无任何输入,作为None输出");
				break;
			case Ts_2.trim() == "":
				// alert("Ts 输入为空格,作为None输出");
				break;
			case !Ts_2.match(pos_real_number) || parseFloat(Ts_2) <= 0:
				alert("输入的 T1/3 值必须大于零。");
				document.waveForm.Ts_2.focus();
				return false;
		}

		let Tp_2 = document.waveForm.Tp.value;
		switch (true) {
			case Tp_2 == "":
				// alert("Tp 无任何输入,作为None输出");
				break;
			case Tp_2.trim() == "":
				// alert("Tp 输入为空格,作为None输出");
				break;
			case !Tp_2.match(pos_real_number) || parseFloat(Tp_2) <= 0:
				alert("输入的 Tp 值必须大于零。");
				document.waveForm.Ts_2.focus();
				return false;
		}
	}
}
