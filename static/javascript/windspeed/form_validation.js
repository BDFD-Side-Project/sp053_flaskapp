/*
 * @Date         : 2022-12-12 12:31:04
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2022-12-29 13:42:37
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\windspeed\form_validation.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */
console.log("Test for Windspeed Validation Form");
function validateForm() {
	let pos_real_number =
		/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/;

	// var _0xc9dd = [
	// 	"\x76\x61\x6C\x75\x65",
	// 	"\x6F\x32",
	// 	"\x77\x61\x76\x65\x46\x6F\x72\x6D",
	// 	"\u8BF7\u9009\u62E9\u98CE\u901F\x28\x55\x29\u7684\u7C7B\u578B\u7684\u6570\u636E\u7C7B\u578B",
	// 	"\x66\x6F\x63\x75\x73",
	// 	"\x63\x31",
	// ];
	// let o2 = document[_0xc9dd[2]][_0xc9dd[1]][_0xc9dd[0]];
	// switch (true) {
	// 	case o2 != 1 && o2 != 2 && o2 != 3 && o2 != 4:
	// 		alert(_0xc9dd[3]);
	// 		document[_0xc9dd[2]][_0xc9dd[5]][_0xc9dd[4]]();
	// 		return false;
	// }

	let o2 = document.waveForm.o2.value;
	switch (true) {
		case o2 != 1 && o2 != 2 && o2 != 3 && o2 != 4:
			alert("请选择风速(U)的类型的数据类型");
			document.waveForm.c1.focus();
			return false;
	}

	if (o2 == 1) {
		let zw_1 = document.waveForm.zw_1.value;
		switch (true) {
			case !zw_1.match(pos_real_number) ||
				parseFloat(zw_1) < 0.5 ||
				parseFloat(zw_1) > 100:
				alert("该参数的取值范围：[0.5,100]");
				document.waveForm.zw_1.focus();
				return false;
		}
	}

	if (o2 == 2) {
		let zw_2 = document.waveForm.zw_2.value;
		switch (true) {
			case !zw_2.match(pos_real_number) ||
				parseFloat(zw_2) < 0.5 ||
				parseFloat(zw_2) > 100:
				alert("该参数的取值范围：[0.5,100]");
				document.waveForm.zw_2.focus();
				return false;
		}

		let X_2 = document.waveForm.X_2.value;
		switch (true) {
			case !X_2.match(pos_real_number) ||
				parseFloat(X_2) < 0.05 ||
				parseFloat(X_2) > 100:
				alert("该参数的取值范围：[0.05,100]");
				document.waveForm.X_2.focus();
				return false;
		}
	}

	if (o2 == 3) {
		let zw_3 = document.waveForm.zw_3.value;
		switch (true) {
			case !zw_3.match(pos_real_number) ||
				parseFloat(zw_3) < 0.5 ||
				parseFloat(zw_3) > 100:
				alert("该参数的取值范围：[0.5,100]");
				document.waveForm.zw_3.focus();
				return false;
		}

		let Xlat_3 = document.waveForm.Xlat_3.value;
		switch (true) {
			case !Xlat_3.match(pos_real_number) ||
				parseFloat(Xlat_3) <= -89 ||
				parseFloat(Xlat_3) >= 89:
				alert("该参数的取值范围：(-89,89)");
				document.waveForm.Xlat_3.focus();
				return false;
		}

		let X_3 = document.waveForm.X_3.value;
		switch (true) {
			case !X_3.match(pos_real_number) ||
				parseFloat(X_3) < 0.05 ||
				parseFloat(X_3) > 100:
				alert("该参数的取值范围：[0.05,100]");
				document.waveForm.X_3.focus();
				return false;
		}
	}

	if (o2 == 4) {
		let Xlat_4 = document.waveForm.Xlat_4.value;
		switch (true) {
			case !Xlat_4.match(pos_real_number) ||
				parseFloat(Xlat_4) <= -89 ||
				parseFloat(Xlat_4) >= 89:
				alert("该参数的取值范围：(-89,89)");
				document.waveForm.Xlat_4.focus();
				return false;
		}

		let Rg_4 = document.waveForm.Rg_4.value;
		switch (true) {
			case Rg_4 == "":
				// alert("Rg 无任何输入,作为None输出");
				break;
			case Rg_4.trim() == "":
				// alert("Rg 输入为空格,作为None输出");
				break;
			case !Rg_4.match(pos_real_number) ||
				parseFloat(Rg_4) <= 0 ||
				parseFloat(Rg_4) >= 1:
				alert("输入了,但值不在(0,1)");
				document.waveForm.Rg_4.focus();
				return false;
		}
	}

	let beta = document.waveForm.beta.value;
	// console.log(beta);
	switch (true) {
		case !beta.match(pos_real_number) || parseFloat(beta) <= 0:
			alert("该参数必须大于零");
			document.waveForm.beta.focus();
			return false;
	}

	let atm = document.waveForm.atm.value;
	switch (true) {
		case !atm.match(pos_real_number) || parseFloat(atm) <= 0:
			alert("该参数必须大于零");
			document.waveForm.atm.focus();
			return false;
	}

	let Ta = document.waveForm.Ta.value;
	switch (true) {
		case !Ta.match(pos_real_number) ||
			parseFloat(Ta) < -95 ||
			parseFloat(Ta) > 60:
			alert("该参数的合理取值范围：[-95,60]");
			document.waveForm.Ta.focus();
			return false;
	}

	let zt = document.waveForm.zt.value;
	switch (true) {
		case !zt.match(pos_real_number) ||
			parseFloat(zt) < 0.5 ||
			parseFloat(zt) > 100:
			alert("该参数的取值范围：[0.5,100]");
			document.waveForm.zt.focus();
			return false;
	}

	let Tw = document.waveForm.Tw.value;
	switch (true) {
		case !Tw.match(pos_real_number) || parseFloat(Tw) < -2 || parseFloat(Tw) > 45:
			alert("该参数的合理取值范围：[-2,45]");
			document.waveForm.Tw.focus();
			return false;
	}

	let Taa = document.waveForm.Taa.value;
	switch (true) {
		case !Taa.match(pos_real_number) ||
			parseFloat(Taa) < -95 ||
			parseFloat(Taa) > 60:
			alert("该参数的合理取值范围：[-95,60]");
			document.waveForm.Taa.focus();
			return false;
	}

	let wdu = document.waveForm.wdu.value;
	switch (true) {
		case !wdu.match(pos_real_number) || parseFloat(wdu) <= 0:
			alert("该参数必须大于零");
			document.waveForm.wdu.focus();
			return false;
	}

	let zu = document.waveForm.zu.value;
	switch (true) {
		case !zu.match(pos_real_number) ||
			parseFloat(zu) < 20 ||
			parseFloat(zu) > 100:
			alert("该参数的建议取值范围：[20,100]");
			document.waveForm.zu.focus();
			return false;
	}
}
