<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="insert1.php" method="post">
        <label for="Name">Name</label>
        <input type="text" name="Name" id="Name">
        <label for="roll">Roll</label>
        <input type="number" name="roll" id="roll">
        <label for="address">Address</label>
        <input type="text" name="address" id="address">
        <label for="category">category</label>
        <input type="text" name="category" id="category">
        <input type="submit" value="submit">
    </form>
</body>
</html>