<?php

    // configuration
    require("../includes/config.php");

    // if form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST")
    {
        // validate submission
        if (empty($_POST["symbol"]))
        {
            apologize("You must provide a Symbol.");
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
                //dump($s);
                render("../templates/quote.php", ["stock" => $s, "title" => "Quoted"]);
            }        
        }
    }
    else
    {
        // else render form
        render("../templates/quote_form.php", ["title" => "Quote Form"]);
    }

?>
