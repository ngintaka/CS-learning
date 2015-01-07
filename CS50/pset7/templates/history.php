<ul class="nav nav-pills">
    <li><a href="quote.php">Quote</a></li>
    <li><a href="buy.php">Buy</a></li>
    <li><a href="sell.php">Sell</a></li>
    <li><a href="deposit.php">Deposit</a></li>
    <li><a href="history.php">History</a></li>
    <li><a href="logout.php"><strong>Log Out</strong></a></li>
</ul>

<div>
<table id="portfolio">

    <thead>
        <tr>
            <th>Transaction</th>
            <th>Date/Time</th>
            <th>Symbol</th>
            <th>Shares</th>
            <th>Price</th>
            <th>Cash Value</th>
        </tr>
    </thead>

    <tbody>
<?php 

foreach ($deals as $deal)
        {
            print("<tr>");
            print("<td>{$deal["transaction"]}</td>"); 
            //reformat sql datetime format
            print("<td>" . date("D j/n/y, g:ma T", strtotime($deal["timestamp"])) . "</td>");           
            print("<td>{$deal["symbol"]}</td>");
            print("<td>{$deal["shares"]}</td>");
            print("<td>" . number_format($deal["price"], 2) . "</td>");
            print("<td>" . number_format($deal["amount"], 2) . "</td>");
            print("</tr>");
        }      

?>
    </tbody>
</table>

</div>
