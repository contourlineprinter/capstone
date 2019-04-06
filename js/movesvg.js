// need to write javascript to post to a different spot for each shape
// need to have result on server side for moving the file.
function printq(){
	$.ajax({
	type: "POST",
	url: "/cgi-bin/movesvg.py",
	//data: { param: input}
	}).done(function(o) {
		console.log('svg sent');
			console.log(o);
	});
}