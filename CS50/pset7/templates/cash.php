<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="deposit.php">Deposit</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>


<br/>
<?php printf("You have sucessfully added <strong>$" . number_format($topup, 2) . "</strong> to your account.<br/> Your new cash balance is <strong>$" .  number_format($new_balance, 2) . "</strong>.<p> Please <a HREF = '/buy.php'> spend</a> it wisely!") ?>

<p>
