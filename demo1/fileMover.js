// need to write javascript to post to a different spot for each shape
// need to have result on server side for moving the file.
function shape(shapetype){
	input = shapetype
	$.ajax({
		type: "GET",
		url: "/demo1/moveline.py",
		data: { param: input}
		}).done(function(o) {
		    console.log('shape ' + input + ' sent');
	});
}
