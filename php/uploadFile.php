<?php
	/*
	session_start();
	ob_start();
	//$_SESSION["dataArray"] = NULL;
	$target_dir = "../uploads/";
	//$temp = explode(".", $_FILES["file"]["name"]);
	//$file_name = "file1". '.' . strtolower(end($temp));
	$file_name = $_FILES["file"]["name"];

	print "cp1 <br>";

	echo "Upload: " . $_FILES["file"]["name"] . "<br>";
	echo "Type: " . $_FILES["file"]["type"] . "<br>";
	echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
	//echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br>";

	if ($_SERVER['REQUEST_METHOD'] == 'POST') {
		print "post <br>";
		if (move_uploaded_file($_FILES["file"]["tmp_name"], "../uploads/".$file_name)){
			print "cp3 <br>";
		}
		else {
			print "Error: ".UPLOAD_ERR_OK;	
		}
	}

	echo '<pre>';
	
	print "<br>";
	chdir('../ExifRead-2.1.2/');
	print "cp4 <br>";
	exec('pwd', $out1);
	var_dump($out1);
	print "<br>";
	chmod($file_name, 777);
	#exec('./EXIF.py ../uploads/'.$file_name.' 2>&1', $out);
	#$_SESSION["dataArray"] = $out;
	var_dump($out);
	echo '</pre>';
	
	
	# Redirect to the results page
	#header ('location: ../upload.html');
	ob_end_flush();
	
	print "fin";
	exit(); 
	*/

   if(isset($_FILES['file'])){
      $errors= array();
      $file_name = $_FILES['file']['name'];
	  echo "name: " . $_FILES['file']['name'] . "<br>";
      $file_size =$_FILES['file']['size'];
	  echo "size " . $_FILES['file']['size'] . "<br>";
      $file_tmp =$_FILES['file']['tmp_name'];
	  echo "tmp_name: " . $_FILES['file']['temp_name'] . "<br>";
      $file_type=$_FILES['file']['type'];
	  

      $file_ext=strtolower(end(explode('.',$_FILES['file']['name'])));
      
      $extensions= array("jpeg","jpg","png","gif");
      
      if(in_array($file_ext,$extensions)=== false){
         $errors[]="extension not allowed, please choose a jpg or png file.";
      }
      
      if($file_size > 2097152){
         $errors[]='File size must be greater than 2 MB';
      }
      
      if(empty($errors)==true){
         if(move_uploaded_file($file_tmp,"../uploads/".$file_name)){
			echo "Success"; 
		 }
		 else {
			print "move failed <br>";
		 }
         
      }else{
         print_r($errors);
      }
   }

?>