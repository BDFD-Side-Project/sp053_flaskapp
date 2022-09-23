/*
 * @Date         : 2022-08-29 12:34:13
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2022-09-07 22:50:27
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\page-break.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */

function pagebreak(url, callback) {
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
