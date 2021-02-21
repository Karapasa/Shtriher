//function shtriher (number) {
//	clearHTML ();
//	var numberSht = number.value;
//	if (testNumber(numberSht)) {
//		sendReq(numberSht);
//	    setTimeout(function() {
//	        resultHtml(1, numberSht);
//	    }, 700);
//		getCoords();
//	}
//}


//function generator (form) {
//	clearHTML ();
//	var numberEAN =document.getElementById('number').value;
//
//	var name = form.name.value;
//	var product = form.product.value;
//	var sku = form.sku.value;
//	var description = form.description.value;
//
//	var datas = [name, product, sku, description];
//
//	var finDatas = [];
//	for (var i = 0; i < datas.length; i++) {
//		if (datas[i] != '') {
//			finDatas.push(datas[i]);
//		}
//	}
//
//	if (finDatas.length > 0 && testNumber(numberEAN)) {
//		sendReq (numberEAN, name, product, sku, description);
//        setTimeout(function() {
//            resultHtml(2, numberEAN);
//        }, 700);
//		getCoords ();
//	} else {
//		document.getElementById('hints').innerHTML = 'ВЫ НЕ ЗАПОЛНИЛИ НИ ОДНОГО ПОЛЯ!';
//	}
//}

function clearHTML () {
	var hintSht = document.getElementById('hintSht');
	var hintEtick = document.getElementById('hints');
	if (hintSht.textContent != '') {
		hintSht.innerHTML = "";
	}
	if (hintEtick.textContent != '') {
		hintEtick.innerHTML = "";
	}
}

//function testNumber (num) {
//	var a = Number (num);
//	if (num.length == 12 && Number.isInteger(a)) {
//		return True;
//	} else {
//		if (num = "") {
//			document.getElementById("hintSht").innerHTML = "ВЫ НЕ ВВЕЛИ НОМЕР ШТРИХКОДА!";
//			} else {
//			document.getElementById("hintSht").innerHTML = "Введите 12 чисел штрихкода, последний генерируется автоматически";
//		}
//		return False;
//	}
//}

//function sendReq (number, name = '', product = '', sku = '', description = '') {
//	var url = '/?number='+number+'&compy='+name+'&name='+product+'&sku='+sku+'&field='+description;
//	const req = new XMLHttpRequest();
//	req.open('get', url);
//	req.send();
//}

function resultHtml (view, number) {
	var nameSht = number + "_sht";
	var nameEtick = number + "_et";
	if (document.getElementById("resultBlock") != "") {
		document.getElementById("resultBlock").innerHTML = "";
	}
	if (view == 2) {
		var res = '<!--html код c одним блоком--> \
					<div class="col">             \
					    <div class="d-flex flex-column">        \
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/img/'+nameEtick+'.png" width="40%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/img/'+nameEtick+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать этикетку</a></div>       \
						</div>    \
					</div>     \
					<hr>     \
					<!-- Блок для штрихкода -->      \
					<div class="col align-self-end">      \
						<div class="d-flex flex-column">         \
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/img/'+nameSht+'.png" width="50%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/img/'+nameSht+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать штрикод</a></div>       \
						</div>     \
					</div>';
	} else {
		var res = '<!-- Блок для штрихкода -->      \
					<div class="col align-self-end">      \
						<div class="d-flex flex-column">         \
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/img/'+nameSht+'.png" width="25%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/img/'+nameSht+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать штрикод</a></div>       \
						</div>     \
					</div>';
	}
	document.getElementById("resultBlock").innerHTML = res;
}

function getCoords() {
	var elem = document.getElementById('resultBlock');
	var elemTop = elem.getBoundingClientRect();
	window.scrollTo(0, elemTop.top + window.pageYOffset);
}
