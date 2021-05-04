$(document).ready(function() {
    google.setOnLoadCallback(drawChart2);
    });


      function drawChart2() {
        var data = google.visualization.arrayToDataTable([
          ['Servidor', 'Sitios'],
          ['Apache', 89780592],
           ['Microsoft-IIS', 19504039],
           ['nginx',	26481450],
           ['GSE (google)', 14137227],
           ['Otros', 27388540]
        ]);

        var options = {
          title: 'Servidores usados en sitios webs activos del mundo (a marzo de 2015 segun NetCraft)',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart2'));

        chart.draw(data, options);
      }
