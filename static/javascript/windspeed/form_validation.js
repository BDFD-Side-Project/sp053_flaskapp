/*
 * @Date         : 2022-12-12 12:31:04
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2023-01-10 13:00:49
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\windspeed\form_validation.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */
console.log("Test for Windspeed Validation Form");
function validateForm() {
	let pos_real_number =
		/([0-9]+\.?|^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)/;

	var _cs = [
		"\x77\x69\x6e",
		"\x6c\x75",
		"\x32",
		"\x76\x61",
		"\x79\x76\x32",
		"\x6d\x61\x74\x68",
		"\x31\x73\x67",
		"\x79\x37",
		"\x76\x65",
		"\x76\x61\x6c",
		"\x65\x66\x34",
		"\x78\x6e",
		"\x72\x75\x66",
		"\x6c\x33",
		"\x61\x77\x74",
		"\x74\x69\x6d\x65",
		"\x30\x75\x6e",
		"\x64\x33",
		"\x26",
		"\x69\x70\x67",
		"\x6d\x77\x30",
		"\x61\x62\x73",
		"\x38\x78\x62",
		"\x6d\x72\x6f",
		"\x70\x68",
		"\x31",
		"\x2b",
		"\x70\x6f\x70",
		"\x5f\x34",
		"\x70\x65\x7a",
		"\x67\x65\x74",
		"\x7a\x74",
		"\x61\x67",
		"\x7a\x75",
		"\x65\x70\x74",
		"\x74\x5f\x33",
		"\x77\x64\x75",
		"\x25",
		"\x52\x67",
		"\x67\x71",
		"\x76\x65\x46",
		"\x68\x66",
		"\x34",
		"\x58\x6c\x61",
		"\x62\x36\x34",
		"\x7a\x39\x79",
		"\x72\x6d",
		"\x39\x38\x78",
		"\x64\x6f\x77",
		"\x74\x5f",
		"\x31\x67",
		"\x77\x68\x69\x6c\x65",
		"\x33\x66",
		"\x54\x77",
		"\x77\x37\x71",
		"\x35\x65",
		"\x7a\x74",
		"\x61",
		"\x5f\x33",
		"\x35\x63",
		"\x37\x34\x33",
		"\x54\x61",
		"\x61\x74\x6d",
		"\x74\x69\x6f\x6e",
		"\x68\x6c\x7a",
		"\x7a\x6f\x6e\x65",
		"\x77\x61",
		"\x36\x61",
		"\x58\x5f\x32",
		"\x6f\x32",
		"\x67\x66",
		"\x38\x66",
		"\x62\x65\x74",
		"\x6a\x37",
		"\x45\x6c\x65",
		"\x30",
		"\x67\x79",
		"\x6d",
		"\x6f\x31",
		"\x76\x65",
		"\x42\x79",
		"\x6c\x6f\x63",
		"\x37\x77\x32",
		"\x75\x65",
		"\x6a\x31\x7a",
		"\x66\x75\x6e\x63",
		"\x65\x46",
		"\x64\x77\x78",
		"\x66\x6f\x72",
		"\x69\x67",
		"\x77\x6e\x76",
		"\x77\x61\x76",
		"\x7a\x77",
		"\x78\x39",
		"\x2d",
		"\x6f\x72",
		"\x6e\x61\x76",
		"\x58\x5f\x33",
		"\x6d\x6d",
		"\x36\x34",
		"\x7a\x77\x5f",
		"\x31\x79",
		"\x6b\x71",
		"\x49\x64",
		"\x74\x69\x6d\x65",
		"\x6c\x75\x65",
		"\x65\x46\x6f",
		"\x65",
		"\x76\x39",
		"\x6d\x65\x6e\x74",
		"\x72\x33\x36",
		"\x63\x34",
		"\x61\x39\x6b",
		"\x6f\x72\x6d",
		"\x46\x6f\x72",
		"\x31\x30\x32\x34",
		"\x76\x37\x75",
		"\x67\x65\x6f",
		"\x62\x62\x72",
		"\x54\x61\x61",
		"\x32\x37",
	];
	let _g0 =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[69]][_cs[9] + _cs[83]];
	let _g1 =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[100] + _cs[25]][
			_cs[3] + _cs[105]
		];
	let _g2 =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[100] + _cs[2]][
			_cs[9] + _cs[83]
		];
	let _g3 = document[_cs[91] + _cs[106] + _cs[46]][_cs[68]][_cs[9] + _cs[83]];
	let _g4 =
		document[_cs[66] + _cs[79] + _cs[114] + _cs[77]][_cs[92] + _cs[58]][
			_cs[9] + _cs[83]
		];
	let _g5 =
		document[_cs[91] + _cs[106] + _cs[46]][_cs[43] + _cs[35]][_cs[3] + _cs[105]];
	let _g6 =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[97]][_cs[3] + _cs[105]];
	let _g7 =
		document[_cs[66] + _cs[79] + _cs[114] + _cs[77]][_cs[43] + _cs[49] + _cs[42]][
			_cs[9] + _cs[83]
		];
	let _g8 =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[38] + _cs[28]][
			_cs[3] + _cs[1] + _cs[107]
		];
	let _g9 =
		document[_cs[91] + _cs[86] + _cs[95] + _cs[77]][_cs[72] + _cs[57]][
			_cs[3] + _cs[105]
		];
	let _ga = document[_cs[91] + _cs[86] + _cs[113]][_cs[62]][_cs[9] + _cs[83]];
	let _gb =
		document[_cs[66] + _cs[40] + _cs[95] + _cs[77]][_cs[61]][_cs[3] + _cs[105]];
	let _gc = document[_cs[91] + _cs[106] + _cs[46]][_cs[31]][_cs[9] + _cs[83]];
	let _gd =
		document[_cs[91] + _cs[86] + _cs[113]][_cs[53]][_cs[3] + _cs[1] + _cs[107]];
	let _ge = document[_cs[91] + _cs[106] + _cs[46]][_cs[119]][_cs[9] + _cs[83]];
	let _gf = document[_cs[91] + _cs[106] + _cs[46]][_cs[36]][_cs[9] + _cs[83]];
	let _gg = document[_cs[91] + _cs[106] + _cs[46]][_cs[33]][_cs[9] + _cs[83]];

	var o2,
		zw_1,
		zw_2,
		X_2,
		zw_3,
		Xlat_3,
		X_3,
		Xlat_4,
		Rg_4,
		beta,
		atm,
		Ta,
		zt,
		Tw,
		Taa,
		wdu,
		zu;
	(o2 = _g0),
		(zw_1 = _g1),
		(zw_2 = _g2),
		(X_2 = _g3),
		(zw_3 = _g4),
		(Xlat_3 = _g5),
		(X_3 = _g6),
		(Xlat_4 = _g7),
		(Rg_4 = _g8),
		(beta = _g9),
		(atm = _ga),
		(Ta = _gb),
		(zt = _gc),
		(Tw = _gd),
		(Taa = _ge),
		(wdu = _gf),
		(zu = _gg);

	switch (true) {
		case o2 != 1 && o2 != 2 && o2 != 3 && o2 != 4:
			alert("请选择风速(U)的类型的数据类型");
			document.waveForm.c1.focus();
			return false;
	}

	if (o2 == 1) {
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
		switch (true) {
			case !zw_2.match(pos_real_number) ||
				parseFloat(zw_2) < 0.5 ||
				parseFloat(zw_2) > 100:
				alert("该参数的取值范围：[0.5,100]");
				document.waveForm.zw_2.focus();
				return false;
		}

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
		switch (true) {
			case !zw_3.match(pos_real_number) ||
				parseFloat(zw_3) < 0.5 ||
				parseFloat(zw_3) > 100:
				alert("该参数的取值范围：[0.5,100]");
				document.waveForm.zw_3.focus();
				return false;
		}

		switch (true) {
			case !Xlat_3.match(pos_real_number) ||
				parseFloat(Xlat_3) <= -89 ||
				parseFloat(Xlat_3) >= 89:
				alert("该参数的取值范围：(-89,89)");
				document.waveForm.Xlat_3.focus();
				return false;
		}

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
		switch (true) {
			case !Xlat_4.match(pos_real_number) ||
				parseFloat(Xlat_4) <= -89 ||
				parseFloat(Xlat_4) >= 89:
				alert("该参数的取值范围：(-89,89)");
				document.waveForm.Xlat_4.focus();
				return false;
		}

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

	// console.log(beta);
	switch (true) {
		case !beta.match(pos_real_number) || parseFloat(beta) <= 0:
			alert("该参数必须大于零");
			document.waveForm.beta.focus();
			return false;
	}

	switch (true) {
		case !atm.match(pos_real_number) || parseFloat(atm) <= 0:
			alert("该参数必须大于零");
			document.waveForm.atm.focus();
			return false;
	}

	switch (true) {
		case !Ta.match(pos_real_number) ||
			parseFloat(Ta) < -95 ||
			parseFloat(Ta) > 60:
			alert("该参数的合理取值范围：[-95,60]");
			document.waveForm.Ta.focus();
			return false;
	}

	switch (true) {
		case !zt.match(pos_real_number) ||
			parseFloat(zt) < 0.5 ||
			parseFloat(zt) > 100:
			alert("该参数的取值范围：[0.5,100]");
			document.waveForm.zt.focus();
			return false;
	}

	switch (true) {
		case !Tw.match(pos_real_number) || parseFloat(Tw) < -2 || parseFloat(Tw) > 45:
			alert("该参数的合理取值范围：[-2,45]");
			document.waveForm.Tw.focus();
			return false;
	}

	switch (true) {
		case Taa == "":
			// alert("Rg 无任何输入,作为None输出");
			break;
		case Taa.trim() == "":
			// alert("Rg 输入为空格,作为None输出");
			break;
		case !Taa.match(pos_real_number) ||
			parseFloat(Taa) < -95 ||
			parseFloat(Taa) > 60:
			alert("该参数的合理取值范围：[-95,60]");
			document.waveForm.Taa.focus();
			return false;
	}

	switch (true) {
		case !wdu.match(pos_real_number) || parseFloat(wdu) <= 0:
			alert("该参数必须大于零");
			document.waveForm.wdu.focus();
			return false;
	}

	switch (true) {
		case !zu.match(pos_real_number) ||
			parseFloat(zu) < 20 ||
			parseFloat(zu) > 100:
			alert("该参数的建议取值范围：[20,100]");
			document.waveForm.zu.focus();
			return false;
	}
}
