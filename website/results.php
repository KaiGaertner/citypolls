<?php
$page = $_SERVER['PHP_SELF'];
$sec = "5";
header("Refresh: $sec; url=$page");


$servername = "kaigaertner.de";
$username = "citypolls";
$password = "Hml8h30#";
$dbname = "citypolls";
$poll_id=1;
$box_id=1;

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT yes, no, creation FROM boxes WHERE boxid=".$box_id." AND pollid=".$poll_id." ORDER BY creation DESC LIMIT 1";
$result = $conn->query($sql);
$last_update = $now;
$yes_votes = 0;
$no_votes = 0;

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
		$last_update = $row["creation"]. "<br>";
        $yes_votes = $row["yes"]. "<br>";
		$no_votes = $row["no"] . "<br>";
    }
} else {
    echo "0 results";
}

?>

 <html>
 <head>
  <title>CityPoll</title>
 </head>
 <body>
 <?php echo '<p>VoteBox results</p>'; ?> 
 <table style="width:30%; text-align:left;">
  <tr>
    <th>Date</th>
    <th>YES</th>
    <th>NO</th>
  </tr>
  <tr>
    <td><?php echo $last_update ?></td>
    <td><?php echo $yes_votes?></td>
    <td><?php echo $no_votes?></td>
  </tr>
</table> 
 </body>
</html>
<?php
$conn->close(); 
?>