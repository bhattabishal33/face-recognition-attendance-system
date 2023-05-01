<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>CRUD operation in system</title>
	<style>
		body{
			background-color: peachpuff;
		}
		table,thead,th,td{
			border:2px solid black;
			padding:2px;
		}
		#nav{
			margin: 10px;
			
			display:flex;
			justify-content: center;
			
		}
		.lin{
			border:2px solid black;
			padding: 5px;
			margin:10px;
		
		}
		a{
			text-decoration: none;
			color: black;
		}
		#content{
			display:flex;
			justify-content: center;
		}
	</style>
</head>
<body>
	<div id="nav">
		<a href="add.php" class="lin">Add</a>
		<a href="logout.php" class="lin">Logout</a>
		<a href="index.php" class="lin">Go back to home</a>
	</div>
<!--<a href="edit.php">Edit</a>
<a href="delete.php">Delete</a>
-->
<div id="content">
<table boarder="3">
	<thead>
		<th>Name</th>
		<th>Roll_no</th>
		<th>Address</th>
		<th>Category</th>
		<th>Date</th>
        <th>Time</th>
	</thead>
	<tbody>
		<?php
			//include our connection
			include 'dbconfig.php';
 
			//query from the table that we create
			$sql = "SELECT  * FROM student";
			$query = $db->query($sql);
 
			while($row = $query->fetchArray()){
				echo "
					<tr>
						<td>".$row['Name']."</td>
						<td>".$row['Roll_no']."</td>
						<td>".$row['Address']."</td>
						<td>".$row['Category']."</td>
                        <td>".$row['Date']."</td>
                        <td>".$row['Time']."</td>
						<td>
							<a href='delete.php?id=".$row['Name']."&&date=".$row['Date']."'>Delete</a>
						</td>
					</tr>
				";
			}
		?>
	</tbody>
</table>
</div>
</body>
</html>