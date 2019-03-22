function shape(shapetype){
	input = shapetype
	$.ajax({
		type: "POST",
		url: "~/testscript.py",
		data: { param: input}
		}).done(function(o) {
		    console.log(data);
		    console.log(input);
	});
}