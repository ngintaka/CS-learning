<?php

    // configuration
    require("../includes/config.php"); 
    
    $deals = query("SELECT * FROM history WHERE id = ?", $_SESSION["id"]);
    if ($deals === false)
    {
        apologize("Something went wrong retrieving your transaction history."); 
    }
    
    // render sell_form
    render("history.php", ["deals" => $deals, "title" => "History"]);

?>
