// need to write javascript to post to a different spot for each shape
// need to have result on server side for moving the file.
function shape(shapetype){
	input = shapetype
	if (shapetype == 0){ //line
		$.ajax({
			type: "POST",
			url: "/cgi-bin/helloworld.py",
			data: { param: input}
			}).done(function(o) {
			    console.log('shape ' + input + ' sent');
					console.log(o);
		});
		else if (shapetype == 1){ //circle
			$.ajax({
				type: "POST",
				url: "/cgi-bin/helloworld.py",
				data: { param: input}
				}).done(function(o) {
				    console.log('shape ' + input + ' sent');
						console.log(o);
				});
		}
		else if (shapetype == 2) { //rectangle
			$.ajax({
				type: "POST",
				url: "/cgi-bin/helloworld.py",
				data: { param: input}
				}).done(function(o) {
				    console.log('shape ' + input + ' sent');
						console.log(o);
				});
		
		}
		else {
			console.log( shapetype + " is not a valid shape");
		}

	}

}
