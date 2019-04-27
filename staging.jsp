<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Contour Line Printer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" type="text/css" media="screen" href="css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="css/staging.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="/">Contour Line Printer</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/">Upload</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="gallery.html">Gallery</a>
                </li>
            </ul>
        </div>
    </nav>

    <!-- Content -->
    <div class="container-fluid">
            <!-- Alert box that shows error messages -->
			<div class="alert alert-info alert-dismissible" id="alert" style="display:none">
		  		<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
		  		<strong><span id="alertText"><%=  request.getAttribute("message") %></span></strong>
			</div> 
		<div class="row justify-content-center">
			<div class="col-lg p-5">
			
				
			    
				<!-- This is where we will show the contour image for user approval -->
				<img id="preview" src="#" class="float-left col-lg-8 img-fluid mx-auto d-block img-thumbnail">
				
				<form action="reupload" metho="post">
				
					<!-- Hidden Input Tag with filename -->
					<input name="fname" id="fname" class="d-none" value="">
					
					<div class="form-group row ml-2 col-sm-4">
						<div class="w-10">
							<div class="form-group row">
								<label for="width" class="col-sm-4 col-form-label">Width (in.)</label>
								<div class="col-sm-8">
								<input id="width" type="number" step="0.01" class="form-control">
								</div>
							</div>
							<div class="form-group row">
								<label for="height" class="col-sm-4 col-form-label">Height (in.)</label>
								<div class="col-sm-8">
								<input id="height" type="number" step="0.01" class="form-control" readonly>
								</div>
							</div>
							<div class="form-group row">
								<label for="scale" class="col-sm-4 col-form-label">Scale Factor</label>
								<div class="col-sm-8">
								<input name="scale" id="scale" type="number" step="0.01" class="form-control" readonly>
								</div>
							</div>
						</div>
					</div> 
					
					<!-- XY Range Slider -->
					<div class="form-group row ml-2 col-sm-4">
						<label  class="col-form-label">x y range</label>
						<span id="slider_value1" ></span>
						<div class="w-100">
							<input name="xyslide" type="range" class="form-control-range slider" id="formControlRange" min="-1" max="100" value="-1" step="1" 
							onchange="show_value1(this.value);">
						</div>					
					</div>
					
					<!-- Point to skip Slider -->
					<div class="form-group row ml-2 col-sm-4">
						<label  class="col-form-label">Points to skip</label>
						<span id="slider_value2"></span>
						<div class="w-100">
							<input name="skipslide" type="range" class="form-control-range slider" id="formControlRange" min="-1" max="100" value="-1" step="1"
							onchange="show_value2(this.value);">
						</div>					
					</div> 
				
					<!-- Min area -->
					<div class="form-group row ml-2 col-sm-4">
						<label  class="col-form-label">Min area</label>
						<span id="slider_value3"></span>
						<div class="w-100">
							<input name="minslide" type="range" class="form-control-range slider" id="formControlRange" min="-1" max="1000" value="-1" step="10"
							onchange="show_value3(this.value);">
						</div>					

					</div> 
					
					
					<!-- Button to approve the image and begin printing -->
					<button class="btn col-sm-4 btn-primary w-100 mt-3">Reupload</button>
				</form>
			
			
				
				<!-- Button to approve the image and begin printing -->
				<button onclick="printq()" class="btn col-sm-4 btn-primary w-100 mt-3">Print</button>
			</div>

		</div>
    </div>
	
	<script>
		// This is how our preview image is recieved by staging.jsp
		var id = window.location.href;
		if (id.includes("&")){
			id = id.split('%2F').pop();
			console.log(id);
			id = id.substring(0, id.indexOf('&'));
			id = "svg/" + id;
			
		}
		else if (id.includes("?")){ // via gallery
			id = id.split('?').pop();
			console.log(id);
			id = "svg/" +id + ".svg";
		} else {  // via upload
			id = "svg/" + "<%= request.getAttribute("file")%>" + ".svg";
		}
		console.log(id);

		document.getElementById("preview").src= id;
		document.getElementById("fname").value = id;
	</script>
	
	
	
    <script src="js/jquery-3.3.1.min.js"></script>
    <!-- <script src="js/bootstrap.bundle.min.js"></script> -->
		<script src="js/staging.js"></script>
	<script src="js/movesvg.js"></script>


	
</body>

</html>
