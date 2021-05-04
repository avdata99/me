$(document).ready(function() {
    google.setOnLoadCallback(drawChart3);
    });


      function drawChart3() {
        var data = google.visualization.arrayToDataTable([
          ['Powered', 'Sitios'],
          ['PHP',69823], 
        ['ASP.NET',30126], 
        ['Plesk (Lin + Win)',3820], 
        ['Servlet',488], 
        ['W3 Total Cache',177], 
        ['Otros',722], 

        ]);

        var options = {
          title: 'Tecnologia detrás del webserver',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart3'));

        chart.draw(data, options);
      }
