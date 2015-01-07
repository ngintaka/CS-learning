<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="deposit.php">Deposit</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>
<br/>
<?php print("You currently have $" . number_format($cash["0"]["cash"], 2) . " in your cash account.
<br/> What stock would you like to buy?<p>"); ?>

<form action="buy.php" method="post">
    <fieldset>
        <div class="form-group">
            <input autofocus class="form-control" name="symbol" placeholder="Stock Symbol" type="text"/>
        </div>
        <div class="form-group">
            <input class="form-control" name="qty" placeholder="Quantity" type="text"/>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-default">BUY!!</button>
        </div>
    </fieldset>
</form>
