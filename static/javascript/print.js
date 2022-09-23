/*
 * @Date         : 2022-08-29 12:34:13
 * @Author       : BDFD,bdfd2005@gmail.com
 * @Github       : https://github.com/bdfd
 * @LastEditTime : 2022-09-07 22:49:48
 * @LastEditors  : BDFD
 * @Description  :
 * @FilePath     : \static\javascript\print.js
 * Copyright (c) 2022 by BDFD, All Rights Reserved.
 */

const buttonPrintOrSaveDocument = document.querySelector(
	".button-print-or-save-document"
);
function printOrSave() {
	window.print();
}
buttonPrintOrSaveDocument.addEventListener("click", printOrSave);
