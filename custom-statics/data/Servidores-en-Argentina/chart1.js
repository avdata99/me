$(document).ready(function() {
    google.setOnLoadCallback(drawChart);
    });


      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Servidor', 'Sitios'],
          ['Apache',157517], 
        ['Microsoft-IIS',34260], 
        ['nginx',33991], 
        ['GSE',1839], 
        ['LiteSpeed',1132], 
        ['Apache-AdvancedExtranetServer',563], 
        ['ghs',494], 
        ['ATS',352], 
        ['Microsoft-HTTPAPI',340], 
        ['Apache-Coyote',283], 
        ['lighttpd',262], 
        ['otros',3927], 

        ]);

        var options = {
          title: 'Servidores usados en los sitios webs argentinos (a marzo de 2015)',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.PieChart(document.getElementById('reg_chart'));

        chart.draw(data, options);
      }