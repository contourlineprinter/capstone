// called when an image is clicked on from the gallery
// Redierects to staging with the selected image passed as input
	
$(document).ready(function(){
	$( ".row" ).click(function(event) {
		console.log($(this).attr('id') + " clicked");  // row that was clicked
		var fname = $(this).find("img").attr("src");   // gets the src attribute of the image tag of the clicked on row
		var fname = fname.replace("images/", "");      // removes the file directory name
		console.log(fname);
		//var url = "staging.jsp"
		
		window.location.href = "staging.jsp?"+fname;
		/*
		$.ajax({
		  type: 'POST',
		  url: "staging.jsp",
		  dataType: "html",
		  data: {data1: fname},
		  success: function(data) {
					console.log("Data: " + data);
					$( "html" ).html( data );
				  },
			async:   true
		});
		*/
		/*
		$.post(url,
		{ data1: fname},
		function(data, status){
				console.log("post sent");
				console.log("Data: " + data + "\nStatus: " + status);
				history.pushState({},"Your Title",url);
				//window.location.replace(url);
				$( "html" ).html( data );
			}
		); */
		
		//$.ajaxSetup({async: true}); //reset
	});
});
