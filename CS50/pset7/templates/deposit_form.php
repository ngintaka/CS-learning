<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="deposit.php">Deposit</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>

<br/>
<?php print("You currently have $" . number_format($cash_balance, 2) . " in your account.
<br/> How much cash would you like to deposit?<p>"); ?>

<form action="deposit.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autofocus class="form-control" name="topup" placeholder="Deposit" type="text"/>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-default">Deposit Cash</button>
        </div>
    </fieldset>
</form>
