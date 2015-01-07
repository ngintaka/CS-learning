<?php

    // configuration
    require("../includes/config.php");
      
        // query database for current cash balance
    $cash_balance = query("SELECT cash FROM users WHERE id = ?", $_SESSION['id']);
    if ($cash_balance === false)
    {
        apologize("Something went wrong retrieving your cash balance");
    }

    // query database for user's stocks
    $stocks = query("SELECT symbol FROM stocks WHERE id = ?", $_SESSION['id']);
    
    if ($stocks == true)
    { 
    //update price for each stock held and store in database
    foreach($stocks as $stock)
    {
        $s = lookup($stock["symbol"]);
        $p = $s["price"];
        $update = query("UPDATE stocks SET price = ? WHERE id = ? AND symbol = ?", $p, $_SESSION['id'], $stock["symbol"]);
        if ($update === false)
        {
            apologize("Something went wrong updating your portfolio");
        }
        
        $positions = query("SELECT *, shares * price AS total FROM stocks WHERE id = ?", $_SESSION['id']);
        if ($positions === false)
        {
            apologize("Something went wrong retrieving your portfolio.");
        }
    }
    
    // render portfolio
    render("portfolio.php", ["positions" => $positions, "cash" => $cash_balance, "title" => "Portfolio"]);
    }
    else
    {
        render("portfolio.php", ["positions" => false, "cash" => $cash_balance, "title" => "Portfolio"]);
    }
    
?>
