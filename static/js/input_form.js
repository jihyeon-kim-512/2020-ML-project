function categoryChange(e) {
	var categorize_a = ["의류", "뷰티", "생활비", "여행", "교통비", "식비", "기타"];
	var categorize_b = ["월급", "용돈", "기타"];
	var target = document.getElementById("categorize");

	if(e.value == "a") var d = categorize_a;
	else if(e.value == "b") var d = categorize_b;

	target.options.length = 0;

	for (x in d) {
		var opt = document.createElement("option");
		opt.value = d[x];
		opt.innerHTML = d[x];
		target.appendChild(opt);
	}
}
