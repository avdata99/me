$(document).ready(function() {
    google.setOnLoadCallback(drawChart);
    });


      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Renueva', 'Cantidad'],
          ['Baja de dominio', 125886],
          ['Renueva', 40847],
          ['Proroga/Especula', 21489],

          ]);

        var options = {
          title: 'Caida de dominios luego de que el servicio de NIC comenzo a ser pago',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart'));

        chart.draw(data, options);
      }
