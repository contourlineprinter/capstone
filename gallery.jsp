<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %> 
<%@page import="java.util.ArrayList"%> 
<%@page import="java.util.List"%> 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <title>Contour Line Printer</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" type="text/css" media="screen" href="css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    </head>
  
    <body> 
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="index.html">Contour Line Printer</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSuppo$
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigatio$
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" href="index.html">Upload</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="gallery.html">Gallery</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="demo1.html">Demo1</a>
                </li>
            </ul>
        </div>
    </nav>
	<div class="album py-4">
		<div class="container">  
        <% ArrayList<String> images =  (ArrayList<String>)request.getAttribute("images"); 
         int index = 0;
         for(String s:images){%>  
           <% if(index%3 == 0) {%>
           		<div class="row">
           <% }%>
                <div class="col-sm-4"><img width="300" height="300" src=<%=s%>></img></div> 
             
             <% if(index%3 == 2) {%>
           		</div>
          	 <% }%>
            <% index++; }%>  
        </div>
    </div>

    
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap.bundle.min.js"></script>
    <script src="js/uploadTriggers.js"></script>

    </body>
</html>
