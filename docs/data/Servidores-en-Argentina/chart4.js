$(document).ready(function() {
    google.setOnLoadCallback(drawChart4);
    });


      function drawChart4() {
        var data = google.visualization.arrayToDataTable([
          ['Version', 'Sitios'],
          ['Desconocido',83824], ['Apache 1.3',3339], ['Apache 2.0',729], ['Apache 2.2',59944], ['Apache 2.4',10778]
        ]);

        var options = {
          title: 'Versiones de Apache',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart4'));

        chart.draw(data, options);
      }
