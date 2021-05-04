$(document).ready(function() {
    google.charts.load('current', {packages: ['corechart']});
    google.setOnLoadCallback(drawChart);
    });


      function drawChart() {
        var data = google.visualization.arrayToDataTable([
        ['DNS', 'Sitios'],
        ['DonWeb (dattatec + hostmar + donWeb)', 47194], 
        ['SIN DNS', 46885], 
        ['El Server (elserver + godns)', 19419], 
        ['En Venta (SEDO)', 14198], 
        ['ToWebs (dnspoint + toweb)', 12369], 
        ['Nuthost servidoraweb + nuthost)', 10233], 
        ['Cdmon', 6485], 
        ['000WebHost', 4347], 
        ['DreamHost', 4151], 
        ['dns1.www.com.ar - 190.61.5.251', 4037], 
        ['ns1.allytech.com', 3846], 
        ['ns1.mydomain.com', 3144], 
        ['ns1.afraid.org', 3138], 
        ['ns1.hostinger-ar.com', 3000], 
        ['dns1.cvtci.com.ar - 24.232.0.17', 2663], 
        ['ns1.wiroos.com', 2529], 
        ['ns3.freeservers.com', 2448], 
        ['ns1.mesi.com.ar - 69.25.11.11', 2394], 
        ['dns1.sucursalonline.com', 2204], 
        ['ns1.dixnet.com', 2050], 
        ['NEOLO', 2039], 
        ['dns1.iplanisp.com.ar - 200.69.193.111', 1728], 
        ['ns1.mediatemple.net', 1389], 
        ['ns1.bluehost.com', 1310], 
        ['ns1.datawebdns.com', 1250], 
        ['ns1.outdns.net', 1224], 
        ['ns1.wix.com', 1131], 
        ['dns1.calu.net', 1085], 
        ['ns1.unlugar.com', 1078], 
        ['OTROS', 171258], 


        ]);

        var options = {
          title: 'DNSs usadon en Argentina a marzo de 2015',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart'));

        chart.draw(data, options);
      }