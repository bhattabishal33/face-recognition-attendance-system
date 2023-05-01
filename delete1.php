<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<?php
    //include our connection
	include 'dbcon.php';

	//delete the row of selected id
	$sql = "DELETE FROM studentinfo WHERE Name = '".$_GET['id']."'";
	$db->query($sql);
 
	header('location: indexfor.php');
?>