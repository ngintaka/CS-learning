<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="deposit.php">Deposit</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>
<br/>


<?php print("<strong>Which stock would you like to sell?</strong><p>");
?>

<form action="sell.php" method="post">
<table id="sell_form">

    <thead>
        <tr>
            <th>SELL?</th>
            <th>Symbol</th>
            <th>Name</th>
            <th>Shares</th>
            <th>Price</th>
            <th>TOTAL</th>
        </tr>
    </thead>

    <tbody>
<?php 

foreach ($positions as $position)
        {
            print("<tr>");
            print("<td><input type = 'radio' name = 'sale' value = {$position["symbol"]},{$position['total']},{$position["shares"]},{$position["price"]}></td>"); 
            print("<td>{$position["symbol"]}</td>"); 
            print("<td>{$position["stock"]}</td>");           
            print("<td>{$position["shares"]}</td>");
            print("<td>" . number_format($position["price"], 2) . "</td>");
            print("<td>" . number_format($position["total"], 2) . "</td>");
            print("</tr>");
        }
?>
    </tbody>

</table>
    <br/><button type="submit" class="btn btn-default">Sell!!</button>
</form>
