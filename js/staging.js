// Contains event driven js functions called on the staging.jsp page


// Updates the size once the image is loaded in
$("#preview").one("load", function() {
	console.log("image loaded");
	var img = document.getElementById('preview');
	var width  = img.naturalWidth;
	var height = img.naturalHeight;
	
	// convert px -> in  (we got this number by doing trials with our bot,  not by standard conversion at 72dpi
	width = width * 0.01296875;
	height = height * 0.01296875;
	document.getElementById('size').innerHTML += width.toFixed(2) + " in x " + height.toFixed(2) + " in";
}).each(function() {
  if(this.complete) {
      //$(this).load(); // For jQuery < 3.0 
      $(this).trigger('load'); // For jQuery >= 3.0 
  }
});