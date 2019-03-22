function shape(shapetype){
	input = shapetype
	$.ajax({
		type: "POST",
		url: "/demo1/testscript.py",
		data: { param: input}
		}).done(function(o) {
		    console.log('shape ' + input + ' sent');
	});
}
