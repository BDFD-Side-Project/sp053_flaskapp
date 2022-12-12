/*
 * @Date         : 2022-12-12 12:48:56
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2022-12-12 17:00:52
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\windspeed\button_control.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */

//reset
var waveForm = document.getElementById("waveForm");
var requiredC1 = document.getElementsByClassName("requiredC1");
var requiredC2 = document.getElementsByClassName("requiredC2");
var requiredC3 = document.getElementsByClassName("requiredC3");
var requiredC4 = document.getElementsByClassName("requiredC4");

console.log(waveForm);
// waveForm.radio.value = 1;

waveForm.o2[0].addEventListener("click", function () {
	if (this.checked) {
		waveForm.o2.value = 1;

		for (let i = 0; i < requiredC1.length; i++) {
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].disabled = false;
			requiredC2[i].disabled = true;
			requiredC3[i].disabled = true;
			requiredC4[i].disabled = true;
		}
	}
});

waveForm.o2[1].addEventListener("click", function () {
	if (this.checked) {
		waveForm.o2.value = 2;

		for (let i = 0; i < requiredC1.length; i++) {
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].disabled = true;
			requiredC2[i].disabled = false;
			requiredC3[i].disabled = true;
			requiredC4[i].disabled = true;
		}
	}
});
// waveForm.o2[2].addEventListener("click", function () {
// 	if (this.checked) {
// 		waveForm.o2.value = 3;

// 		for (let i = 0; i < requiredC1.length; i++) {
// 			requiredC1[i].value = "";
// 			requiredC2[i].value = "";
// 			requiredC1[i].value = "";
// 			requiredC2[i].value = "";
// 			requiredC1[i].disabled = true;
// 			requiredC2[i].disabled = true;
// 			requiredC3[i].disabled = false;
// 			requiredC4[i].disabled = true;
// 		}
// 	}
// });
waveForm.o3[0].addEventListener("click", function () {
	if (this.checked) {
		waveForm.o3.value = 1;

		for (let i = 0; i < requiredC1.length; i++) {
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].disabled = true;
			requiredC2[i].disabled = true;
			requiredC3[i].disabled = false;
			requiredC4[i].disabled = true;
		}
	}
});
waveForm.o3[1].addEventListener("click", function () {
	if (this.checked) {
		waveForm.o3.value = 2;

		for (let i = 0; i < requiredC1.length; i++) {
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].value = "";
			requiredC2[i].value = "";
			requiredC1[i].disabled = true;
			requiredC2[i].disabled = true;
			requiredC3[i].disabled = true;
			requiredC4[i].disabled = false;
		}
	}
});
