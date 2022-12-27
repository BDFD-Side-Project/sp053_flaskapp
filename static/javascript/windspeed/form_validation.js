/*
 * @Date         : 2022-12-12 12:31:04
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2022-12-27 11:37:03
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\windspeed\form_validation.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */
console.log("Test for Windspeed Validation Form");
function validateForm() {
	let pos_real_number =
		/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/;
	// let pos_int_number = /^[1-9]+[0-9]*$/;

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
				alert("该参数-zw_1的合理取值范围：[0.5,100]");
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
				alert("该参数-zw_2的合理取值范围：[0.5,100]");
				document.waveForm.zw_2.focus();
				return false;
		}
	}

	if (o2 == 3) {
		let zw_3 = document.waveForm.zw_3.value;
		switch (true) {
			case !zw_3.match(pos_real_number) ||
				parseFloat(zw_3) < 0.5 ||
				parseFloat(zw_3) > 100:
				alert("该参数-zw_3的合理取值范围：[0.5,100]");
				document.waveForm.zw_3.focus();
				return false;
		}

		let Xlat_3 = document.waveForm.Xlat_3.value;
		switch (true) {
			case !Xlat_3.match(pos_real_number) ||
				parseFloat(Xlat_3) <= -89 ||
				parseFloat(Xlat_3) >= 89:
				alert("该参数-Xlat_3的合理取值范围：(-89,89)");
				document.waveForm.Xlat_3.focus();
				return false;
		}

		let X_3 = document.waveForm.X_3.value;
		switch (true) {
			case !X_3.match(pos_real_number) ||
				parseFloat(X_3) < 0.05 ||
				parseFloat(X_3) > 100:
				alert("该参数-X_3的合理取值范围：[0.05,100]");
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
				alert("该参数-Xlat_3的合理取值范围：(-89,89)");
				document.waveForm.Xlat_4.focus();
				return false;
		}

		let Rg_4 = document.waveForm.Rg_4.value;
		switch (true) {
			case !Rg_4.match(pos_real_number) ||
				parseFloat(Rg_4) <= 0 ||
				parseFloat(Rg_4) >= 1:
				alert("该参数-Rg_4的合理取值范围：(0,1)");
				document.waveForm.Rg_4.focus();
				return false;
		}
	}

	let beta = document.waveForm.beta.value;
	// console.log(beta);
	switch (true) {
		case !beta.match(pos_real_number) || parseFloat(beta) <= 0:
			alert("该参数-U必须大于零");
			document.waveForm.beta.focus();
			return false;
	}

	let atm = document.waveForm.atm.value;
	switch (true) {
		case !atm.match(pos_real_number) || parseFloat(atm) <= 0:
			alert("该参数-atm必须大于零");
			document.waveForm.atm.focus();
			return false;
	}

	let Ta = document.waveForm.Ta.value;
	switch (true) {
		case !Ta.match(pos_real_number) ||
			parseFloat(Ta) < -95 ||
			parseFloat(Ta) > 60:
			alert("该参数-Ta的合理取值范围：[-95,60]");
			document.waveForm.Ta.focus();
			return false;
	}

	let zt = document.waveForm.zt.value;
	switch (true) {
		case !zt.match(pos_real_number) ||
			parseFloat(zt) < 0.5 ||
			parseFloat(zt) > 100:
			alert("该参数-zt的合理取值范围：[0.5,100]");
			document.waveForm.zt.focus();
			return false;
	}

	let Tw = document.waveForm.Tw.value;
	switch (true) {
		case !Tw.match(pos_real_number) || parseFloat(Tw) < -2 || parseFloat(Tw) > 45:
			alert("该参数-Tw的合理取值范围：[-2,45]");
			document.waveForm.Tw.focus();
			return false;
	}

	let Taa = document.waveForm.Taa.value;
	switch (true) {
		case !Taa.match(pos_real_number) ||
			parseFloat(Taa) < -95 ||
			parseFloat(Taa) > 60:
			alert("该参数-Taa的合理取值范围：[-95,60]");
			document.waveForm.Taa.focus();
			return false;
	}

	let wdu = document.waveForm.wdu.value;
	switch (true) {
		case !wdu.match(pos_real_number) || parseFloat(wdu) <= 0:
			alert("该参数-wdu必须大于零");
			document.waveForm.wdu.focus();
			return false;
	}

	let zu = document.waveForm.zu.value;
	switch (true) {
		case !zu.match(pos_real_number) ||
			parseFloat(zu) < 20 ||
			parseFloat(zu) > 100:
			alert("该参数-zu的合理取值范围：[20,100]");
			document.waveForm.zu.focus();
			return false;
	}
}
