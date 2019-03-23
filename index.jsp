<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>File Upload</title>
        <link rel="stylesheet" href="main.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
    </head>

    <body>
        <div class="topnav">
          <a class="active" href="index.jsp">Index</a>
          <a href="gallery.html">Gallery</a>
        </div>
        <div>
            <h3> Upload an image on server: </h3>
            <form action="image_upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*"/>
                <input type="submit" value="upload" />
            </form>
        </div>
    </body>
</html>