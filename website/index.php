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

<!DOCTYPE html>
<!--  Last Published: Sat Feb 22 2020 17:11:32 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="5c16253f8f692006f5f78216" data-wf-site="5c16253e8f692098e3f78213">
<head>
  <meta charset="utf-8">
  <title>CityPolls - Demonstrator</title>
  <meta content="CityPolls" property="og:title">
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/components.css" rel="stylesheet" type="text/css">
  <link href="css/uab-intelligents-top-notch-project.css" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">WebFont.load({  google: {    families: ["Oswald:200,300,400,500,600,700","Roboto:300,regular,500","Nanum Myeongjo:regular,700,800","Hind Siliguri:regular,500,600,700"]  }});</script>
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script>
  <link href="images/favicon.png" rel="shortcut icon" type="image/x-icon">
  <link href="images/webclip.png" rel="apple-touch-icon">
</head>
<body>
  <div class="section-6"><img src="images/try.png" srcset="images/try.png 500w, images/try.png 800w, images/try.png 1080w, images/try.png 1600w, images/try.png 2588w" sizes="100vw" alt="" class="image-13"></div>
  <div class="section-5">
    <div class="object w-container">
      <div>
        <div data-w-id="fd8f2146-f278-f9ee-06d7-a4fbcb28d286" class="tooltip">
          <p class="paragraph">Would you like to have a bike lane instead of car parking spots in Friedrichstrasse?</p>
          <div class="votesection">
            <div class="votesegment"><img src="images/thumbs-down.png" alt="" class="image-12">
              <p class="down"><?php echo $no_votes?></p>
            </div>
            <div class="votesegment"><img src="images/thumbs-up.png" alt="" class="image-11">
              <p class="up"><?php echo $yes_votes?></p>
            </div>
          </div>
        </div>
        <div class="dot"></div>
      </div>
    </div>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.4.1.min.220afd743d.js" type="text/javascript" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
  <script src="js/uab-intelligents-top-notch-project.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
</body>
</html>