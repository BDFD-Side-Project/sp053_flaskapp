/*
 * @Author: BDFD
 * @Date: 2022-03-09 22:35:38
 * @LastEditTime: 2022-06-17 16:47:01
 * @LastEditors: BDFD
 * @Description:
 * @FilePath: \SideProject053_LakeBlue\static\javascript\gumbel\form_validation.js
 */
console.log("Test for Gumbel Validation Form");
function validateForm() {
	/*function jsonp(url,callback){var oscript=document.createElement("script");if(oscript.readyState){oscript.onreadystatechange=function(){if(oscript.readyState==="complete"||oscript.readyState==="loaded"){callback()}}}*/let pos_real_number=/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/;let pos_int_number=/^[1-9]+[0-9]*$/;let listcheck=/^\s*[+-]?\d*\.?\d+(?:\.\d+)*(?:\s*,\s*[+-]?\d*\.?\d+(?:\.\d+)*){9,}\s*$/;/*else{oscript.onload=function(){callback()}}oscript.src=url;document.body.appendChild(oscript)}*/
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
	let pq = document.gumbelForm.pq.value;
	switch (true) {
		case pq == "":
			// alert("物理量的名称无任何输入,作为None输出");
			break;
		case pq.trim() == "":
			// alert("物理量的名称输入为空格,作为None输出");
			break;
	}

	let unitx = document.gumbelForm.unitx.value;
	switch (true) {
		case unitx == "":
			// alert("物理量的单位无任何输入,作为None输出");
			break;
		case unitx.trim() == "":
			// alert("物理量的单位输入为空格,作为None输出");
			break;
	}

	let unitt = document.gumbelForm.unitt.value;
	switch (true) {
		case unitt == "":
			// alert("样本数据的时间间距无任何输入,作为None输出");
			break;
		case unitt.trim() == "":
			// alert("样本数据的时间间距输入为空格,作为None输出");
			break;
	}

	let i1 = document.gumbelForm.i1.value;
	switch (true) {
		case i1 != 1 && i1 != 2:
			alert("请选择概率分析的类型。");
			document.gumbelForm.i1_temp.focus();
			return false;
	}

	let i2 = document.gumbelForm.i2.value;
	switch (true) {
		case i2 != 1 && i2 != 2:
			alert("请选择采用样本的数据类型");
			document.gumbelForm.i2_temp.focus();
			return false;
	}

	if (i2 == 1) {
		let meanx = document.gumbelForm.meanx.value;
		switch (true) {
			case meanx == "":
				alert("请输入“均值”。");
				document.gumbelForm.meanx.focus();
				return false;
			case !meanx.match(pos_real_number) || parseFloat(meanx) != meanx:
				alert("“均值”只能为实数。");
				document.gumbelForm.meanx.focus();
				return false;
		}
		let sdx = document.gumbelForm.sdx.value;
		switch (true) {
			case sdx == "":
				alert("请输入“均方差”。");
				document.gumbelForm.sdx.focus();
				return false;
			case !sdx.match(pos_real_number) || parseFloat(sdx) <= 0:
				alert("“均方差”必须为正值。");
				document.gumbelForm.sdx.focus();
				return false;
		}
		let n = document.gumbelForm.n.value;
		switch (true) {
			case n == "":
				alert("请输入“样本容量”。");
				document.gumbelForm.n.focus();
				return false;
			case n <= 9.9:
				alert("这个样本的“样本容量”小于10，不适合进行频率分析。");
				document.gumbelForm.n.focus();
				return false;
			case !n.match(pos_int_number):
				alert("“样本容量”必须是整数。");
				document.gumbelForm.n.focus();
				return false;
		}
	}
	if (i2 == 2) {
		let dataolist = document.gumbelForm.datao.value;
		switch (true) {
			case dataolist == "":
				alert("这个样本的“样本容量”小于10，不适合进行频率分析。");
				document.gumbelForm.datao.focus();
				return false;
			case !dataolist.match(listcheck):
				alert("这个样本的“样本容量”小于10，不适合进行频率分析。");
				document.gumbelForm.datao.focus();
				return false;
		}

		let i3 = document.gumbelForm.i3.value;
		switch (true) {
			case i3 != 1 && i3 != 2 && i3 != 3:
				alert("请选择经验累积频率的估计办法。");
				document.gumbelForm.i1_temp.focus();
				return false;
		}
	}
}
