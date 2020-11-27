$(document).ready(function(){
	var check = $("input[type='checkbox']").is(":checked");

	if (check == true) {
		$(".get_money_contents").toggle();
	}
});

function toggleclick(){
		var check = $("input[type='checkbox']").is(":checked");
		if (check == true) {
			$(".get_money_contents").toggle();
			console.log(a);

		}
		if (check == false) {
			$(".get_money_contents").hide();
			location.href="http://localhost:5000/checklimit/false";
		}

}
