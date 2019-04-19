<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Contour Line Printer</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" type="text/css" media="screen" href="css/bootstrap.min.css">
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
	
	<%!
	String fileName = "test";
	%>
	<%
	
	if (request.getParameter("data1")!= null) { // passback
		fileName = 	request.getParameter("data1");
	}
	else { // via upload
		fileName = request.getAttribute("file") + "";
	}

	%>

    <!-- Content -->
    <div class="container-fluid">
            <!-- Alert box that shows error messages -->
			<div class="alert alert-info alert-dismissible" id="alert" style="display:none">
		  		<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
		  		<strong><span id="alertText"><%=  request.getAttribute("message") %></span></strong>
			</div> 
		<div class="row justify-content-center">
			<div class="col-12 col-md-6 pt-3">
			
				<!-- Line Density Slider -->
				<div class="form-group row">
					<label  class="col-sm-3 col-form-label">Line Density</label>
					<div class="col-sm-9">
						<input type="range" class="form-control-range" id="formControlRange">
					</div>
				</div>
			    
				<!-- This is where we will show the contour image for user approval -->
				<img src=  "<%= "svg/"+ fileName + ".svg" %>" class="img-fluid mx-auto d-block img-thumbnail mt-3">
				
				<!-- Button to approve the image and begin printing -->
				<button onclick="printq()" class="btn btn-primary w-100 mt-3">Print</button>
			</div>

		</div>
    </div>

	
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
	<script src="js/movesvg.js"></script>

	
</body>

</html>
