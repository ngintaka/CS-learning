<?php

    // configuration
    require("../includes/config.php"); 
    
    // query database for current cash balance
    $cash_balance = query("SELECT cash FROM users WHERE id = ?", $_SESSION['id']);
    
    if ($cash_balance === false)
    {
        apologize("Something went wrong!");
    }
              
    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide a stock symbol.");
        }
        else if (empty($_POST["qty"]))
        {
            apologize("You must provide a quantity to buy.");
        }
        else if (preg_match('/^\d+$/', $_POST["qty"]) !== 1)
        {
            apologize("Please input whole positive numbers only");
        }
        
        else
        {
            $s = lookup($_POST['symbol']);
            
            if ($s === false)
            {
                apologize("That symbol doesn't exist.");
            }
            else
            {
                $new_balance = (int)$cash_balance[0]["cash"] - (int)($s["price"] * (int)$_POST["qty"]);
                if ($new_balance === false)
                {
                    apologize("Something went wrong updating the balance");
                }                        
                else if ($new_balance < 0)
                {
                    apologize("You don't have cash enough to cover that purchase.");
                }
                else
                {
                    $cash_update = query("UPDATE users SET cash = ?  WHERE id = ?", $new_balance, $_SESSION['id']);
                    if ($cash_update === false)
                    {
                        apologize("There was a problem updating the cash balance");
                    }
                    
                    $new_purchase = query("INSERT INTO stocks (id, symbol, stock, shares, price) VALUES (?,?,?,?,?) ON DUPLICATE KEY UPDATE shares = shares + ?", $_SESSION['id'], strtoupper($s["symbol"]), $s["name"], $_POST["qty"], $s["price"], $_POST["qty"]);
                    if ($new_purchase === false)
                    {
                        apologize("There was a problem updating the purchase records.");
                    }
                                        
                    $buy_history_update = query("INSERT INTO history (id, timestamp, transaction, symbol, shares, price, amount) VALUES(?, NOW(), ?, ?, ?, ?, ?)", $_SESSION['id'], "BUY", strtoupper($s["symbol"]), $_POST["qty"], $s["price"], $_POST["qty"] * $s["price"] * -1);
                    if ($buy_history_update === false)
                    {
                        apologize("There was a problem updating the purchase history.");
                    }
                    
                // redirect to portfolio
                redirect("/index.php");

                }
               
            }                    
        }
    }
    else
    {
     // render buy_form
    render("buy_form.php", ["cash" => $cash_balance, "title" => "Buy Shares"]);
    }
?>
