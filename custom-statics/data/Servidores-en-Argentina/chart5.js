$(document).ready(function() {
    google.setOnLoadCallback(drawChart5);
    });


      function drawChart5() {
        var data = google.visualization.arrayToDataTable([
          ['Version', 'Sitios'],
          ['Microsoft-IIS 4.0',13], 
        ['Microsoft-IIS 5.0',1584], 
        ['Microsoft-IIS 5.1',23], 
        ['Microsoft-IIS 6.0',9992], 
        ['Microsoft-IIS 7.0',3934], 
        ['Microsoft-IIS 7.5',16764], 
        ['Microsoft-IIS 8.0',1103], 
        ['Microsoft-IIS 8.5',847]


        ]);

        var options = {
          title: 'Versiones de Microsft-IIS',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart5'));

        chart.draw(data, options);
      }
