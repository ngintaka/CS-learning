<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>


<br/>
<strong>
<?php printf("A share of " . $stock["name"] . " (" . $stock["symbol"] . ") costs $" .  number_format($stock["price"],2)); ?>
</strong>
</p>

