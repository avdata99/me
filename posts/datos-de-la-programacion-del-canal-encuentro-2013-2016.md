<html><body><p>Hasta hace muy pocos días en el sitio web del <a href="http://www.encuentro.gob.ar/">Canal Encuentro</a> se publicaban archivos PDF con la programación diaria del canal. Bastante feos pero datos al fin.

<a href="https://github.com/avdata99/ScrapEncuentro/blob/gh-pages/grillaPDF/GrillaEncuentro-01-01-2014.pdf"><img class="aligncenter size-full wp-image-337" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_597.png" alt="seleccion_597" width="675" height="275"></a>

Uno podía acceder a todos los archivos PDF simplemente navegando uno por uno todos los días en el almanaque que mostraba. Decidí entonces hacer un pequeño programa de computadora que hiciera el trabajo por mí. Encontré que estos archivos PDF se publicaban desde mayo de 2013. El programa descargo entonces automáticamente los 1286 archivos con datos.

<strong>Lamentablemente y por <em>casualidad</em> el día posterior a descargar los 1286 archivos con datos estos desaparecieron, este análisis no podrá seguirse haciendo. Canal Encuentro al parecer cerró esos datos.
Hoy la programación se encuentra en <a href="http://www.encuentro.gob.ar/programacion">http://www.encuentro.gob.ar/programacion</a> pero hasta el día que hice este análisis el link era <a href="http://www.encuentro.gob.ar/sitios/encuentro/grilla/index">http://www.encuentro.gob.ar/sitios/encuentro/grilla/index</a> (todavía se redirige).
</strong>

Transforme a texto esos datos <a href="https://github.com/euske/pdfminer/blob/master/tools/pdf2txt.py">con una herramienta</a> disponible y finalmente los organicé con una tabla estructurada. Quedaron entonces dos datasets muy interesantes.

1.- La programación completa de los tres años y medio de emisiones (2013-2016) en <a href="https://raw.githubusercontent.com/avdata99/ScrapEncuentro/gh-pages/final.csv">CSV</a>.
2 .- Los datos acumulados por programa (sin considerar los capítulos específicos) también en <a href="https://raw.githubusercontent.com/avdata99/ScrapEncuentro/gh-pages/acumulado.csv">CSV</a>.

El primer dataset es más rico, se podrían hacer muchos análisis y visualizaciones con el. El segundo es más general pero también valioso y me permite saber si la programación 2016 (gestión Cambiemos) sigue la línea de los años anteriores (gestión FPV). Ponderando los programas según horario de transmisión (<a href="https://github.com/avdata99/ScrapEncuentro/blob/gh-pages/scrapencuentro.py#L76-L104">a ojo</a>, no soy experto en prime-time, horarios de TV, etc) y tomando los programas más <em>destacados</em> de 2016 puedo conocer cual fue su trayectoria anterior.

<a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2016/"><img class="aligncenter size-large wp-image-338" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_598-1024x457.png" alt="seleccion_598" width="790" height="353"></a>

<strong><a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2016/">Click para ampliar</a></strong>

El gráfico muestra lo que cualquier consumidor de este canal de televisión ha podido notar. Hubo (como era de esperar) bastantes cambios en la programación, de los programas más vistos hoy muchos no existían años atrás o se daban con menor relevancia. Sólo algunos programas siguen.

Análisis detallado de cada programa y sus capítulos a través del tiempo. Ejemplo <em><a href="https://avdata99.github.io/ScrapEncuentro/viz/detalle-programas/index.html?programa=filosofia-aqui-y-ahora&amp;anio=0">Filosofía aquí y ahora</a>:</em>

<a href="https://avdata99.github.io/ScrapEncuentro/viz/detalle-programas/index.html?programa=filosofia-aqui-y-ahora&amp;anio=0"><img class="aligncenter size-medium wp-image-346" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_608-300x141.png" alt="seleccion_608" width="300" height="141"></a>

Puede filtrarse por programa y por año. Ejemplo: <em><a href="https://avdata99.github.io/ScrapEncuentro/viz/detalle-programas/index.html?programa=a-fondo&amp;anio=2016">A fondo, 2016</a>:</em>

<a href="http://dev/otros/scrapencuentro/viz/detalle-programas/index.html?programa=a-fondo&amp;anio=2016"><img class="aligncenter size-medium wp-image-347" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_609-300x137.png" alt="seleccion_609" width="300" height="137"></a>

La finalidad de este análisis era también experimentar visualizaciones por lo que deje hechas algunas más.

<a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2015/">Evolución de la relevancia de los programas más importantes de 2015</a>

<a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2015/"><img class="aligncenter wp-image-339 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_599-300x136.png" alt="seleccion_599" width="300" height="136"></a>

 

<a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2015/">Evolución mensual de los programas más puntuados de toda la serie (2013-2016)</a>

<a href="https://avdata99.github.io/ScrapEncuentro/viz/historia-programas-mas-vistos-2015/"><img class="aligncenter size-medium wp-image-340" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_600-300x138.png" alt="seleccion_600" width="300" height="138"></a>

 

<a href="https://avdata99.github.io/ScrapEncuentro/viz/programas-por-anio/">Evolución anual de los programas más puntuados de toda la serie (2013-2016)</a>

<a href="https://avdata99.github.io/ScrapEncuentro/viz/programas-por-anio/"><img class="aligncenter size-medium wp-image-341" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_601-300x135.png" alt="seleccion_601" width="300" height="135"></a>

 

Los datos usados, el código para extraerlo y las visualizaciones quedaron en este repositorio de código abierto:
<a href="https://github.com/avdata99/ScrapEncuentro">https://github.com/avdata99/ScrapEncuentro</a>. Si te sirven los datos para hacer otros análisis o visualizaciones estaría agradecido que los compartas.

 </p></body></html>