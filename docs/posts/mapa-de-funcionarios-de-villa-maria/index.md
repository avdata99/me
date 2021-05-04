<html><body><p>Con motivo del Congreso Ecosistema de Datos (<a href="http://www.conecos.com.ar/">CONECOS16</a>) fuimos invitados como equipo de <a href="http://opendatacordoba.org/">OpenDataCordoba</a> a organizar el Hackathon que allí iba a desarrollarse.

En contra de lo que esperaba por ser organizado un día de semana por la mañana asistieron más de 50 personas y pudimos hacer 8 equipos de trabajo.

En mi caso decidí trabajar con la base de datos de funcionarios de la Ciudad de Villa María que el municipio <a href="http://datos.villamaria.gob.ar/dataviews/225794/funcionarios-municipales/">ya libera en su portal de datos</a>. La idea fue replicar el <a href="https://modernizacionmunicba.github.io/visualizaciones/dendograma/?radio=600">dendrograma que ya habíamos desarrollado desde la Municipalidad de Córdoba</a> y que dejamos como <a href="https://github.com/ModernizacionMuniCBA/visualizaciones/tree/gh-pages/dendograma">código abierto</a> para que cualquier gobierno reutilice con la línea con la idea de la <a href="http://andresvazquez.com.ar/blog/la-cooperacion-como-estrategia-de-desarrollo/">cooperación como estrategia para el desarrollo</a>.
</p><blockquote class="twitter-tweet" data-lang="en">
<p dir="ltr" lang="es">2 gobiernos de distintos signos políticos cooperan en Gobierno Abierto. Impresionante#CONECOS16 <a href="https://twitter.com/martinrgill">@martinrgill</a> <a href="https://twitter.com/MuniVillaMaria">@MuniVillaMaria</a> <a href="https://twitter.com/cossarmarcelo">@cossarmarcelo</a> <a href="https://t.co/28IipeXDy3">https://t.co/28IipeXDy3</a></p>
— Mariano Mosquera (@MarianoMosquera) <a href="https://twitter.com/MarianoMosquera/status/794973609638895617">November 5, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Los datos liberados eran bastante completos pero no tenían información de la relación entre los funcionarios. O sea, estaban todos los nodos pero no información a cerca de las conexiones entre ellos. Para esto conté con la colaboración de dos politólogos (Guido López Avakian (<a href="https://twitter.com/glopezavakian">@glopezavakian</a>) y Facundo Londero) que me ayudaron <a href="https://docs.google.com/spreadsheets/d/1rxLsTBDRPu5SRB5i0k8i3E3aJQGX1ZX-KyLC4TqzbBU/edit?usp=sharing">vía un documento compartido</a> a completar la información faltante. Los funcionarios del municipio de Villa María nos ayudaron también a obtener la información necesaria. Agregamos tambien el <em>género</em> de cada funcionario para que la visualización final permita conocer también este dato.

Luego un <a href="https://github.com/VillaMaria/dendrograma-funcionarios-villa-maria/blob/gh-pages/convert-csv-to-json.py">script simple para transformar estos datos</a> al formato necesario en la visualización y <em>voilà</em>, un nuevo dendrograma funcionando

<a href="https://villamaria.github.io/dendrograma-funcionarios-villa-maria/dendrograma/?radio=550"><img class="aligncenter wp-image-330 size-full" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/11/Selecci%C3%B3n_582.png" alt="dendrograma villa maría" width="776" height="291"></a>

 

El código completo de esta visualización quedó también <a href="https://github.com/VillaMaria/dendrograma-funcionarios-villa-maria">abierto y libre</a> para reutilizarse en otros gobiernos.</body></html>