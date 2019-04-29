// Called when the print button is click on staging.jsp
// movesvg will move the most recent svg to a designated move folder
function printq(){
	//String input = filename;
	console.log("print clicked");
	$.ajax({
	type: "POST",
	url: "/cgi-bin/movesvg.py",
	//url: "/cgi-bin/movesvg.py?name=" + input,
	//data: { param: input}
	}).done(function(o) {
		console.log('svg sent');
			console.log(o);
	});
}
