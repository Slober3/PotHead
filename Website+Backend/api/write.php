<?
include '../includes/config.php';

/*
DO NOT EDIT ANYTHING BEYOND THIS POINT UNLESS YOU KNOW WHAT YOU'RE DOING!!!
*/


if ($api_key==$_POST["apikey"]){
if (isset($logfile)) {
//Get all params
foreach ($_POST as $param_name => $param_val) {
    $cur_data .= "$param_name: $param_val ";
}

//Generate newline
$cur_data .="\r\n";

//Write to file
file_put_contents($logfile, $cur_data,FILE_APPEND | LOCK_EX);
}

if (isset($servername)) {
$ipPostData = str_replace(array('(',')',"'",' '), '',$_POST["ip"]);
$ipExplodeDataArray=explode(",",$ipPostData);
$ip=$ipExplodeDataArray[0];
$portHacker=$ipExplodeDataArray[1];

try {
    $dbh = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

if (!isset($_POST["input"])) {
$stmt = $dbh->prepare("INSERT INTO iplog (ip, port, portHacker) VALUES (:ip, :port, :portHacker)");
$stmt->bindParam(':ip', $ip);
$stmt->bindParam(':port', $_POST["port"]);
$stmt->bindParam(':portHacker', $portHacker);
    // use exec() because no results are returned
    $stmt->execute();
}

if (isset($_POST["input"])) {
$stmt = $dbh->prepare("INSERT INTO loginput(ip, port, portHacker,input) VALUES (:ip, :port, :portHacker, :input)");
$stmt->bindParam(':ip', $ip);
$stmt->bindParam(':port', $_POST["port"]);
$stmt->bindParam(':portHacker', $portHacker);
$stmt->bindParam(':input', $_POST["input"]);
    // use exec() because no results are returned
    $stmt->execute();
}
    echo "New record created successfully";
    }
catch(PDOException $e)
    {
    echo $stmt . "<br>" . $e->getMessage();
    }

$dbh = null;
}
}
else{
echo 'Wrong key.';
}
?>