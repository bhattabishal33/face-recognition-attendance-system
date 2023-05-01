<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<?php
header('Location:indexx.php');
include 'dbconfig.php';
$col1 = $_POST['Name'];
$col2 = $_POST['roll'];
$col3 = $_POST['address'];
$col4 = $_POST['category'];

$col5 = $_POST['d'];

$col6 = $_POST['t'];
$comd = "INSERT INTO `student` (`Name`, `Roll_no`, `Address`, `Category`,`Date`,`Time`) VALUES ('$col1', '$col2', '$col3', '$col4','$col5','$col6');";
if($db->exec($comd))
{
    echo "<script>alert('insert data');</script>";
}
else{
    echo "failed";
}
?>