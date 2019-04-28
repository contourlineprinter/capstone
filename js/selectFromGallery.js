// called when an image is clicked on from the gallery
// Redierects to staging with the selected image passed as input
	
$(document).ready(function(){
	$( ".row" ).click(function(event) {
		console.log($(this).attr('id') + " clicked");  // row that was clicked
		var fname = $(this).find("img").attr("src");   // gets the src attribute of the image tag of the clicked on row
		var fname = fname.replace("images/", "");      // removes the file directory name
		console.log(fname);
		
		window.location.href = "staging.jsp?name="+fname;  // putting the filename into the url since there are no secrets here

	});
});
