<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>PotHead</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">

  </head>
  <body>

    <div class="container-fluid">
	<div class="row">
		<div class="col-md-1">
		</div>
		<div class="col-md-10">
			<ul class="nav nav-tabs">
				<li class="active">
					<a href="./view.php">View</a>
				</li>
				<li>
					<a href="./inputView.php">Input</a>
				</li>
				<li class="disabled">
					<a href="#">Under Dev.</a>
				</li>
				
			</ul>
			<h2 class="text-center">
				PotHead. Small footprint, log all connection attempts!
			</h2>
			<dl>
				<dt>
					Description
				</dt>
				<dd>
					Pothead, a small footprint and lightweight logging script for general purposes.
				</dd>
				<dt>
					Warning
				</dt>
				<dd>
					This script is still under development and should not be used in a production environment.
				</dd>
				<dd>
					Please. send your review to me directly!
				</dd>
				<dt>
					Support
				</dt>
				<dd>
					Support isn't available 24/7. if you have a question please send these to the thread hosted on HackForums
				</dd>
				<dt>
					I will try to help you.
				</dt>
				<dd>
					If you can contribute to this project please send me a PM directly.
				</dd>
			</dl>
			<table class="table table-hover table-condensed table-striped">
				<thead>
					<tr>
						<th>
							#
						</th>
						<th>
							Time
						</th>
						<th>
							Internet Protocol address
						</th>
						<th>
							Port
						</th>
					</tr>
				</thead>
				<tbody>

<?php
include './includes/config.php';

class TableRows extends RecursiveIteratorIterator { 
    function __construct($its) { 
        parent::__construct($its, self::LEAVES_ONLY); 
    }

    function current() {
        return "<td>" . ( filter_var(parent::current(), FILTER_VALIDATE_IP) ? '<a href="http://www.ipvoid.com/scan/'.parent::current().'/">'.parent::current().'</a>' : parent::current()) . "</td>";
    }

    function beginChildren() { 
        echo "<tr>"; 
    } 

    function endChildren() { 
        echo "</tr>" . "\n";
    } 
} 


try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT * FROM ( SELECT id, time, ip, port FROM iplog ORDER BY id DESC LIMIT 30 ) sub ORDER BY id ASC"); 
    $stmt->execute();

    // set the resulting array to associative
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC); 
    foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v) { 
        echo $v;
    }
}
catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
$conn = null;
?>



				</tbody>
			</table>
			
		</div>
		<div class="col-md-1">
		</div>
	</div>
</div>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>
  </body>
</html>