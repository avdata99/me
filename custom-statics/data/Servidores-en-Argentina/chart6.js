$(document).ready(function() {
    google.setOnLoadCallback(drawChart6);
    });


      function drawChart6() {
        var data = google.visualization.arrayToDataTable([
          ['Version', 'Sitios'],
          ['Desconocido',22411], 
            ['Nginx 0.6',2], 
            ['Nginx 0.7',360], 
            ['Nginx 0.8',18], 
            ['Nginx 1.0',78], 
            ['Nginx 1.1',133], 
            ['Nginx 1.2',235], 
            ['Nginx 1.3',3], 
            ['Nginx 1.4',720], 
            ['Nginx 1.5',4], 
            ['Nginx 1.6',9945], 
            ['Nginx 1.7',82], 


        ]);

        var options = {
          title: 'Versiones de Nginx',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart6'));

        chart.draw(data, options);
      }
