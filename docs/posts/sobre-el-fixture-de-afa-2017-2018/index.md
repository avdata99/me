<html><body><p>En Argentina sucede desde algún tiempo algo que en otras ligas del mundo no; el fixture no incluye dos partidos contra todos los equipos (uno de local y uno de visitante). Esto implica que la <em>justicia</em> en los partidos que se sorteen no será igual para todos. Lamentablemente <a href="http://www.afa.org.ar/7918/torneos.php">no se publican muchos detalles</a> de los sorteo. En este caso se necesitaría mucho mayor transparencia.
</p><h2>¿Por que el fixture no es igualitario?</h2>
Por varios motivos:
<ul>
 	<li>En este caso comenzamos con que son 27 fechas. La mitad de los equipos van a jugar 14 partidos de local y la otra mitad 13. Teniendo en cuenta que en general los locales ganan más de la mitad de los partidos (la otra mitad se reparte entre empates y victorias visitantes) este no es un detalle menor.</li>
 	<li>Como no juego dos veces contra todos los rivales (local y visitante) podrían tocarme todos los partidos mas <em>difíciles</em> de visitante y los más <em>fáciles</em> de local (o alreves).</li>
</ul>
Ojo. Que no sea igualitario no quiere decir que estos datos indican una manipulación maliciosa en en sorteo.
<h2>Datos</h2>
Comenzamos con <strong>el fixture</strong> de la SuperLiga 2017-2018 sorteados por AFA. Se encuentra <a href="http://www.afa.org.ar/reglamentos/reglamentos_fixture.php">disponible</a> en PDF. No hay mejor version oficial. Por suerte existe <a href="http://tabula.technology/">TabulaPDF</a> y pude <a href="https://github.com/avdata99/fixture-afa-2017-2018/blob/master/datos/tabula-Fixture-Torneo-2017-2018-1ra-Div.csv">pasarlo a CSV.</a>

Por otro lado use una <strong><a href="https://github.com/avdata99/fixture-afa-2017-2018/blob/master/datos/promedios-actuales.csv">tabla de promedios</a></strong> para sumar los datos de las temporadas anteriores.
<h2>Gráficos</h2>
La primera pregunta es ¿quienes juegan 14 partidos de local y quienes 13?

<a href="https://docs.google.com/spreadsheets/d/14AY0JiLT3N3eTYOYDIGoZQ7jOcjhKh5raoiR8LObGy4/edit?usp=sharing"><img class="aligncenter size-full wp-image-417" src="/blog/wp-content/uploads/2018/03/Selecci%C3%B3n_0085.png" alt="" width="602" height="562"></a>Este es un detalle muy importante, hay una ventaja evidente (no gigante pero si clara) para el que juega 14 partidos de local.

Por otro lado surge la pregunta. ¿A todos los equipos los rivales mas y menos pesados se les distribuyen parecido en partidos de local y visitante?

Para saber cuan <em>pesado o fuerte </em>es un equipo use el puntaje de ese equipo el año pasado. La construcción de estos datos se hizo en Python y <a href="https://github.com/avdata99/fixture-afa-2017-2018">quedo abierta</a> en un repositorio.Los datos además se subieron a Google Drive para hacer visualizaciones rápidas. <a href="https://docs.google.com/spreadsheets/d/14AY0JiLT3N3eTYOYDIGoZQ7jOcjhKh5raoiR8LObGy4">Tambien quedó abierto</a>.

Si calculo el promedio de puntos de los equipos que tiene cada equipo de local y le resto el mismo número de visitante puede estimar el peso que queda de cada lado. Queda esto:

<a href="https://docs.google.com/spreadsheets/d/14AY0JiLT3N3eTYOYDIGoZQ7jOcjhKh5raoiR8LObGy4"><img class="aligncenter size-full wp-image-418" src="/blog/wp-content/uploads/2018/03/Selecci%C3%B3n_0086.png" alt="" width="931" height="533"></a>

Aquí se ve como Independiente tiene a los rivales mas <em>pesados</em> de local mientras que Olimpo los tiene de visitante. Pero esto es un promedio, veamos el detalle.
<h3>Independiente (los rivales mas "fáciles" arriba):</h3>
<img class="aligncenter size-full wp-image-419" src="/blog/wp-content/uploads/2018/03/Selecci%C3%B3n_0087.png" alt="" width="386" height="612">

Como puede verse, de los cinco rivales mas <em>pesados</em> juega cuantro de local. De los cinco mas <em>fáciles</em> juega cuatro de visitante.
<h3>En el otro extremo, Olimpo:</h3>
<img class="aligncenter size-full wp-image-420" src="/blog/wp-content/uploads/2018/03/Selecci%C3%B3n_0088.png" alt="" width="363" height="614">

Como puede verse, de los cinco rivales más <em>fáciles</em> juega cuatro de local. De los cinco mas <em>pesados</em> juega cuatro de visitante.

En el repositorio pueden verse las tablas de TODOS los equipos de primera división.
<h2>Conclusión</h2>
Las condiciones sobre las que se elabora el fixture hacen que inevitablemente las condiciones no sean iguales para todos. Como pasan los años y no parece ser un problema para nadie no me parece mal marcar el detalle.</body></html>