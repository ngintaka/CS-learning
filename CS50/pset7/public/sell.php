<?php
    
    // configuration
    require("../includes/config.php"); 
      
    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        if (empty($_POST["sale"]))
        {
            apologize("Please select the stock you wish to sell.");
        }
    
        else
        {
            $keywords = preg_split('/,/', $_POST["sale"]);    
            $symbol = $keywords[0];
            $total = $keywords[1];
            $shares = $keywords[2]; 
            $price = $keywords[3];
                
            $sale_cash_update = query("UPDATE users SET cash = cash + ? WHERE id = ?", $total, $_SESSION['id']);
            if ($sale_cash_update === false)
            {
                apologize("Something went wrong updating your cash balance");
            }
            $sold_stock = query("DELETE FROM stocks WHERE id = ? and symbol = ?", $_SESSION['id'], $symbol);
            if($sold_stock === false)
            {
                apologize("Something went wrong registering the sale.");
            }  
            $sale_history_update = query("INSERT INTO history (id, timestamp, transaction, symbol, shares, price, amount) VALUES(?, NOW(), ?, ?, ?, ?, ?)", $_SESSION['id'], "SELL", $symbol, $shares, $price, $shares * $price);
            if ($sale_history_update === false)
            {
                apologize("Something went wrong updating your sale history.");
            }
    
            // redirect to portfolio
            redirect("/");
        }
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
        $sale_update = query("UPDATE stocks SET price = ? WHERE id = ? AND symbol = ?", $p, $_SESSION['id'], $stock["symbol"]);
        if ($sale_update === false)
        {
            apologise("Something went wrong registering your sale.");
        }
        $positions = query("SELECT *, shares * price AS total FROM stocks WHERE id = ?", $_SESSION['id']);
        if ($positions === false)
        {
            apologize("Something went wrong retrieving your portfolio.");
        }
    }
    
    // render sell_form
    render("sell_form.php", ["positions" => $positions, "title" => "Sell Stocks"]);
    }
    else
    {
        apologize("You have no stocks to sell at this time");
    }

?>
