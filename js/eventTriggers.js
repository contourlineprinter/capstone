$(document).ready(function(){
	
	// Hides the alert on index if there is no jsp response 
	if (document.getElementById('alertText').innerHTML ==  "null"){
		document.getElementById('alert').style.display= 'none';
	}
	else {
		document.getElementById('alert').style.display= 'block';
	}
	
	// Changes the label of the fileInput box to reflect the name of the file selected
	document.getElementById('fileInput').onchange = function()
		{
						
			var selectedFile = document.getElementById('fileInput').files[0].name;
			// Display name of file selected
			document.getElementById("fileName").innerHTML = selectedFile;
			
		};
		

});

