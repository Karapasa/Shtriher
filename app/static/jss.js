function clearHtml () {
	var hintSht = document.getElementById('hintSht');
	var hintEtick = document.getElementById('hints');
	if (hintSht.textContent != '') {
		hintSht.innerHTML = "";
	}
	if (hintEtick.textContent != '') {
		hintEtick.innerHTML = "";
	}
}

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
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/static/labels/'+nameEtick+'.png" width="40%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/static/labels/'+nameEtick+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать этикетку</a></div>       \
						</div>    \
					</div>     \
					<hr>     \
					<!-- Блок для штрихкода -->      \
					<div class="col align-self-end">      \
						<div class="d-flex flex-column">         \
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/static/labels/"+nameSht+".png" width="50%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/static/labels/'+nameSht+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать штрикод</a></div>       \
						</div>     \
					</div>';
	} else {
		var res = '<!-- Блок для штрихкода -->      \
					<div class="col align-self-end">      \
						<div class="d-flex flex-column">         \
							<div class="d-flex p-2 justify-content-center"><img class="inst" src="/static/labels/'+nameSht+'.png" width="25%"></div>      \
							<div class="d-flex p-2 justify-content-center"><a href="/static/labels/'+nameSht+'.png" class="btn btn-primary btn-lg active button" role="button" aria-pressed="true" download>Скачать штрикод</a></div>       \
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
