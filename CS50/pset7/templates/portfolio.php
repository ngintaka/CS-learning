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
            <th>Symbol</th>
            <th>Name</th>
            <th>Shares</th>
            <th>Price</th>
            <th>TOTAL</th>
        </tr>
    </thead>

    <tbody>
<?php 
        if ($positions)
        {
            foreach ($positions as $position)
            {
                print("<tr>");
                print("<td>{$position["symbol"]}</td>"); 
                print("<td>{$position["stock"]}</td>");           
                print("<td>{$position["shares"]}</td>");
                print("<td>" . number_format($position["price"], 2) . "</td>");
                print("<td>" . number_format($position["total"], 2) . "</td>");
                print("</tr>");
            }
        }
        print("<tr>");
        print("<td><strong>CASH</strong></td>");
        print("<td COLSPAN = 3></td>");
        print("<td><strong>" . number_format($cash["0"]["cash"], 2) . "</strong></td>");
        print("</tr>");
        
?>
    </tbody>

</table>

</div>
