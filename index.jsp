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
                <li class="nav-item">
                    <a class="nav-link" href="demo1.html">Demo1</a>
                </li>
            </ul>
        </div>
    </nav>

    <!-- Content -->
    <div class="container-fluid">
             <div class="alert alert-info alert-dismissible" id="alert" style="display:none">
		  		<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
		  		<strong><span id="alertText"><%=  request.getAttribute("message") %></span></strong>
			</div>
        <div class="row justify-content-center">

            <div class="col-12 col-md-6 pt-3">
                <!-- Form for uploading an image -->
                <form action="image_upload" id="form" method="post" enctype="multipart/form-data">
                    <div class="form-group row">
                        <!-- Image Upload Button-->
                        <label  class="col-sm-3 col-form-label">Image</label>
                        <div class="col-sm-9">
                            <div class="custom-file">
                                <input type="file" class="custom-file-input" name="file" id="fileInput">
                                <label id="fileName" class="custom-file-label" for="fileInput">Choose file</label>
                            </div>
                        </div>
                    </div>
                    <div class="form-group row">
                        <!-- Line Density Slider -->
                        <label  class="col-sm-3 col-form-label">Line Density</label>
                        <div class="col-sm-9">
                            <input type="range" class="form-control-range" id="formControlRange">
                        </div>
                    </div>
                    <!-- Upload Button -->
                    <div class="form-group row">
                        <div class="col-12">
                            <input type="submit" name="submit" class="btn btn-primary w-100" value="Upload"></input>
                        </div>
                </form>
                


            </div>
        </div>
    </div>

    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
	<script src="js/eventTriggers.js"></script>
</body>

</html>
