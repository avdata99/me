<html><body><p>Este post es continuación de <a title="Anatomía de los censos en latinoamérica" href="http://andresvazquez.com.ar/blog/anatomia-de-los-censos-en-latinoamerica/" target="_blank">esta introducción a los censos en latinoamérica</a> y de la <a href="http://blog.jazzido.com/2014/02/24/resultados-censo-2010-radio-censal/" target="_blank">gran resolución que le dio Manuel Aristarán</a>

Según la <a href="http://www.opex.sig.indec.gov.ar/codgeo/index.php?pagina=definiciones" target="_blank">clasificación de INDEC</a> el <em>radio censal</em> es la menor unidad de agrupamiento que se publica sobre los datos un censo. En general corresponde a alrededor de 300 viviendas. Aún así los datos accesibles al público en general llegan solamente hasta el nivel departamental (de partidos en provincia de Buenos Aires o comunas en CABA).

Esto es interesante para hacer muchos análisis pero limitado para la búsqueda de un mapa con alta definición. Los datos del INDEC<a href="http://200.51.91.245/argbin/RpWebEngine.exe/PortalAction?&amp;BASE=CPV2010B" target="_blank"> están disponibles aquí</a> y se pueden consultar vía el software <a href="http://www.eclac.cl/redatam/" target="_blank">REDATAM</a> (versión servidor). Despues de conseguir los polígonos aproximados de los radios censales y teniendo en cuenta que no eran exactos decidí pasarlos a puntos.

Con el <a href="http://www.qgis.org/es/site/" target="_blank">software QGis</a> pase de polígonos a puntos y crucé los datos en CSV extraídos de REDATAM para poder colocarlos sobre un mapa. El resultado es un mapa con alta definición que permite mostrar cualquiera de las variables tomadas en el censo argentino 2010.

<a href="http://andresvazquez.com.ar/data/cordoba-argentina-segun-censo-2010/mapa/index/dato/H14_01/z/11/l1/-31.350705167260916/l2/-64.28420324853515/sel/absoluto/heat/1/"><img class="alignleft size-medium wp-image-47" alt="Cordoba en HD, censo 2010" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/04/Selection_007-300x176.png" width="300" height="176"></a>

Además del "mapa de calor" que es muy descriptivo se puede pasar a un modo mas analítico que muestra los números de cada variable para cada radio censal.

Un detalle que creo que es muy útil es que cualquier cambio en las variables o en la ubicación del mapa actualiza la URL de modo que se pueda compartir exactamente lo que se esta viendo.

Creo que es una herramienta interesante para investigación, muchas veces <em>mirar</em> los datos de esta forma ayuda a comprender grandes volúmenes de información muy rápido. Un ejemplo bastante común es conocer las características de una zona, ciudad o barrio si simplemente estamos buscando donde mudarnos.</p></body></html>