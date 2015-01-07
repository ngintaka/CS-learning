<?php

    // configuration
    require("../includes/config.php"); 

    // query database for current cash balance
    $row = query("SELECT cash FROM users WHERE id = ?", $_SESSION['id']);
    if($row === false)
    {
        apologize("Something went wrong checking your cash balance.");
    }    
    $cash_balance = $row[0]["cash"];
    
    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["topup"]))
        {
            apologize("You must provide a cash amount (positive numbers only).");
        }
        else if (preg_match('/^\d+$/', $_POST["topup"]) !== 1)
        {
            apologize("Please input whole positive numbers only.");
        }
        else
        {
        $topup = (int)$_POST["topup"];
        $new_balance = $cash_balance + $topup;
        $add_cash = query("UPDATE users SET cash = ?  WHERE id = ?", $new_balance, $_SESSION['id']);
    if($add_cash === false)
    {
        apologize("Something went wrong adding to your cash balance.");
    }    
        
        $add_cash_history = query("INSERT INTO history (id, timestamp, transaction, amount) VALUES(?, NOW(), ?, ?)", $_SESSION['id'], "DEPOSIT", $topup);
    if($add_cash_history === false)
    {
        apologize("Something went wrong adding your cash balance to history.");
    }    
        
        // render confirmation_form
        render("cash.php", ["new_balance" => $new_balance, "topup" => $topup, "title" => "Confirmation"]);
        
        }
    }

    else
    {

     // render cash input form_form
     render("deposit_form.php", ["cash_balance" => $cash_balance, "title" => "Cash Deposit"]);
    }

?>
