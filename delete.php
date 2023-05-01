<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<?php
    
    //include our connection
	include 'dbconfig.php';

	//delete the row of selected id
	$sql = "DELETE FROM student WHERE Name = '".$_GET['id']."' And  Date = '".$_GET['date']."'";
	$db->query($sql);
 
	header('location: indexx.php');
?>