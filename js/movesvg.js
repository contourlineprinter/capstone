// need to write javascript to post to a different spot for each shape
// need to have result on server side for moving the file.
function printq(){
	//String input = filename;
	console.log("test");
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
