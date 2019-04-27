// Contains event driven js functions called on the staging.jsp page

var ratio;

// Updates the size once the image is loaded in
$("#preview").one("load", function() {
	console.log("image loaded");
	var img = document.getElementById('preview');
	var width  = img.naturalWidth;
	var height = img.naturalHeight;
	ratio = width/height;
	
	// convert px -> in  (we got this number by doing trials with our bot,  not by standard conversion at 72dpi
	width = width * 0.01296875;
	height = height * 0.01296875;
	document.getElementById('width').value=width.toFixed(2)
  document.getElementById('height').value=height.toFixed(2)
	$('#width').change(() => {
		document.getElementById('height').value=compute_height($('#width').val());
	});
}).each(function() {
  if(this.complete) {
      //$(this).load(); // For jQuery < 3.0 
      $(this).trigger('load'); // For jQuery >= 3.0 
  }
});

function show_value1(x)
{	
	if(x == -1){
		document.getElementById("slider_value1").innerHTML="Default";
	}else{
		document.getElementById("slider_value1").innerHTML=x;
	}
}

function show_value2(x)
{
	if(x == -1){
		document.getElementById("slider_value2").innerHTML="Default";
	}else{
		document.getElementById("slider_value2").innerHTML=x;
	}
}

function show_value3(x)
{
	if(x == -1){
		document.getElementById("slider_value3").innerHTML="Default";
	}else{
		document.getElementById("slider_value3").innerHTML=x;
	}
}

function compute_height(new_width) {
	// takes in new width
	// returns new height that maintains aspect ratio
	return (new_width) / ratio;
}