<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<?php
header('Location:indexfor.php');
include 'dbcon.php';
$col1 = $_POST['Name'];
$col2 = $_POST['roll'];
$col3 = $_POST['address'];
$col4 = $_POST['category'];
$comd = "INSERT INTO `studentinfo` (`Name`, `Roll`, `Address`, `Category`) VALUES ('$col1', '$col2', '$col3', '$col4');";
if($db->exec($comd))
{
    echo "<script>alert('insert data');</script>";
}
else{
    echo "failed";
}
?>