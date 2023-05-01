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
    <title>Admin page</title>
    <style>
        body{
            background-color: peachpuff;
        }
        div{
            justify-content : center;
            text-align : center;
            font-size: 5vh;
            margin: 5rem;
        }
        div:hover{
            background-color:#8B1874;
            border-radius: 50px;
            color: white;
        }
        a{
            text-decoration: none;
            color:black;
        }
        #boarder{
            border-style: groove; 
        }

        #bid{
            border-style:groove;
        }
        #log{
            border-style:groove;
        }

    </style>
</head>
<body>  
<a href="indexx.php">
    <div id="boarder">
        <p>
             Access for Student Attendacne 
        </p>
    </div>
</a>
<a href="indexfor.php">    
    <div id="bid">
        <p>
            Access for Student information 
            </p>
    </div>
</a>
<a href="logout.php" class="btn btn-warning">
    <div id="log">
        Logout
    </div>
</a>
</body>
</html>