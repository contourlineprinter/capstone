// Changes input label to reflect the selected file
$(document).ready(function(){
	document.getElementById('fileInput').onchange = function()
		{
						
			var selectedFile = document.getElementById('fileInput').files[0].name;
			// Display name of file selected
			document.getElementById("fileName").innerHTML = selectedFile;
			
		};
});



// Populate the gallary with the contents of the upload folder
