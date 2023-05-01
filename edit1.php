<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<?php
	//include our connection
	include 'dbcon.php';
 
	//get the row of selected id
	$sql = "SELECT * FROM studentinfo WHERE Name = '".$_GET['id']."'";
	$query = $db->query($sql);
	$row = $query->fetchArray();
 
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>CRUD Operation on SQLite3 Database using PHP</title>
</head>
<body>
<form method="POST">
	<a href="index.php">Back</a>
	<p>
		<label for="name">Firstname:</label>
		<input type="text" id="name" name="name" value="<?php echo $row['Name']; ?>">
	</p>
	<p>
		<label for="roll">Roll:</label>
		<input type="text" id="roll" name="roll" value="<?php echo $row['Roll']; ?>">
	</p>
	<p>
		<label for="address">Address:</label>
		<input type="text" id="address" name="address" value="<?php echo $row['Address']; ?>">
	</p>
    <p>
		<label for="cat">Category:</label>
		<input type="text" id="cat" name="cat" value="<?php echo $row['Category']; ?>">
	</p>
	<input type="submit" name="save" value="Save">
</form>

<?php
	if(isset($_POST['save'])){
		$firstname = $_POST['name'];
		$lastname = $_POST['roll'];
		$address = $_POST['address'];
        $catagory = $_POST['cat'];
		//update our table
		$sql = "UPDATE studentinfo SET Name = '$firstname', Roll = '$lastname', Address = '$address', Category = '$catagory' WHERE Name = '".$_GET['id']."'";
		$db->exec($sql);
 
		header('location: indexfor.php');
	}
?>
</body>
</html>