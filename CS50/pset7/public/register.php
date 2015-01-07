<?php

    // configuration
    require("../includes/config.php");

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["username"]))
        {
            apologize("You must provide your username.");
        }
        else if (empty($_POST["password"]))
        {
            apologize("You must provide your password.");
        }
        else if ($_POST["password"] != $_POST["confirmation"])
        {
            apologize("Your password & confirmation must match.");
        }
        else
        {
            $result = query("INSERT INTO users (username, hash, cash) VALUES(?, ?, 10000.00)",
            $_POST["username"], crypt($_POST["password"]));
            
            if ($result === false)
            {
                apologize("That username already exists.");
            }
            else
            {
                //grab user's id
                $rows = query("SELECT LAST_INSERT_ID() AS id");
                if($rows === false)
                {
                    apologize("Something went wrong retrieving your info.");
                }
                $id = $rows[0]["id"];
                
                // remember that user's now logged in by storing user's ID in session
                $_SESSION["id"] = $id;
                
                // redirect to portfolio
                redirect("/");
            }        
        }
    }
    else
    {
        // else render form
        render("register_form.php", ["title" => "Register"]);
    }

?>
