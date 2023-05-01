<?php
    //Create a new SQLite3 Database
    $db = new SQLite3("sample.db");
//Create a new table to our database 
    $query = "CREATE TABLE IF NOT EXISTS student (Name varchar(100), Roll_no int(11), Address varchar(100), category varchar(100),Date date,Time time)";
    $db->exec($query);
    
?>