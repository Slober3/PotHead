<?php
include '../../includes/config.php';

// get the HTTP method, path and body of the request


// retrieve the table and key from the path


// connect to the database
$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// excecute SQL statement
 
 
// print results, insert id or affected row count

 
// close connection
$conn = null;
?>