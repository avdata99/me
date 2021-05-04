<html><body><p>Buscar datos liberados de municipios no es tarea fácil. Hay casos interesantes pero la norma general es que es difícil encontrar municipios que tengan sitio web y se actualice con regularidad. En el siguiente análisis -por ejemplo- solo 8 de 168 comunas estudiadas (en Córdoba son ciudades con menos de 2000 habitantes) tienen sitio web (2012).

Existen numerosas normativas para la transparencia de la gestión municipal en Córdoba. El estado provincial en su ley orgánica (que rige a todos los municipios hasta que tienen 10.000 habitantes, el 90% de las localidades) indica que debe informarse mensualmente a la ciudadanía mediante un boletín informativo (<a href="http://www.cba.gov.ar/wp-content/4p96humuzp/2012/06/mcr-ley8102.pdf" target="_blank">ley 8.102, artículo 38</a>). Esto lamentablemente no se cumple en general (no conozco casos). Atendiendo a la conservación y publicación de estos datos el gobierno de Córdoba obliga a los municipios a enviar estos datos a la administración provincial que lo publicará en el <a href="http://www.boletinoficialcba.gov.ar/archivos12/160412_seccion1.pdf" target="_blank">Registro Provincial de Legislacion Municipal</a>. Esta institución lamentablemente no entrega datos por internet.

Como si estas normas no fueran suficientes existe además la <a href="http://www.cba.gov.ar/wp-content/4p96humuzp/2012/06/mcr-ley9206.pdf" target="_blank">ley 9.206</a> de regionalización. Es un excelente instrumento para crear organizaciones supra-municipales que puedan pensar problemas zonales y sumar el esfuerzos de las localidades vecinas. Los artículos 22 y 23 de esta ley prevén la creación de innovadores "Indicadores de desarrollo regional". Estos indices (que nos permitirían saber mucho de los municipios)  pasaron por un exhaustivo análisis luego del cual se arribo a la definición de numerosos indicadores que hubieran sido muy interesante de conocer. Las definiciones técnicas de los indices regionales, no tiene desperdicio y pueden leerse aquí: <a href="http://ifg.org.ar/ckfinder/userfiles/files/Indicadores%20de%20Desarrollo%20Regional%20-%20Informe%20Final.pdf" target="_blank">SISTEMA DE INDICADORES DE DESARROLLO REGIONAL EN LA PROVINCIA DE CORDOBA</a>. Hay indices de transparencia, de desarrollo, actividad económica, etc. Gran trabajo, vale nombrar a los investigadores: Dr. Victor Mazzalay, Mg. Matías Bianchi, Dra. María Marta Santillan Pizarro, Dr. Sebastian Freille, Mg. Daniel Scandizzo y Lic. Pablo Sofﬁetti

<a href="http://ifg.org.ar/ckfinder/userfiles/files/Indicadores%20de%20Desarrollo%20Regional%20-%20Informe%20Final.pdf" target="_blank"><img class="aligncenter wp-image-92 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_056-300x216.png" alt="Selection_056" width="300" height="216"></a>

Previo a este material <a href="https://twitter.com/marioriorda" target="_blank">Mario</a> <a href="http://www.marioriorda.com/" target="_blank">Riorda</a> y <a href="https://twitter.com/JEmilioGraglia" target="_blank">Emilio</a> <a href="http://joseemiliograglia.wordpress.com/" target="_blank">Graglia</a> escribieron un excelente documento analizando las virtudes de la regionalización de Córdoba. El material esta disponible y es ineludible para pensar en municipios y regionalización: <a href="http://www.cba.gov.ar/wp-content/4p96humuzp/2012/07/Desarrollo-Municipalismo-y-Regionalizacion.pdf" target="_blank">Desarrollo, municipalismo y regionalización</a>.

<a href="http://www.cba.gov.ar/wp-content/4p96humuzp/2012/07/Desarrollo-Municipalismo-y-Regionalizacion.pdf" target="_blank"><img class="aligncenter wp-image-93 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_057-300x190.png" alt="Selection_057" width="300" height="190"></a>

<strong>A pesar de toda esta serie de normativas no es posible acceder a datos de municipios de manera simple</strong>. Lo que si se puede conseguir es una de las fuentes principales de ingresos de los municipios, <strong>la coparticipación provincial</strong>.

El siguiente análisis parte de los datos que libera la provincia de Córdoba en cuanto al dinero que envía a municipios y comunas en concepto de coparticipación. Los datos pueden verse en el sitio <a href="http://www.cba.gov.ar/coparticipacion/" target="_blank">cba.gov.ar/coparticipacion/</a>.

Lamentablemente los datos se encuentran en formato PDF (son 44 documentos del período 2009/2014), que presenta numerosas complicaciones para su análisis.

* Los archivos no están nombrados siguiendo una serie (que permita una descarga automática). Más bien parecen nombrados manualmente cada trimestre de publicación.
* Algunos archivos presentan errores extraños.

<a href="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_054.png" target="_blank"><img class="aligncenter wp-image-88 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_054-300x110.png" alt="Selection_054" width="300" height="110"></a>

* No todos los PDFs estan generados con el mismo formato, margenes y estilo por lo que un conversor aplicado masivamente a todos los archivos no funcionaría.

Por suerte existe <a href="http://tabula.nerdpower.org" target="_blank">Tabula</a> que fue de gran ayuda y me permitió extraer los datos en relativamente poco tiempo. De todas formas los datos no pueden usarse a la primera, requieren de control. Una vez los datos en CSV que genera el software Tabula aplicamos una primera validación de los datos por los totales de las columnas que el mismo tabula extrajo. Si algún dato se extrae incorrectamente este error se podrá ver comparando la suma de los datos de cada columna con el total extraído por el software. Esta validación, cuando está disponible, difícilmente falla.

Corregidos algunos detalles menores y teniendo en cuenta que la <a href="http://www.mininterior.gov.ar/municipios/gestion/normativas/Cordoba.pdf" target="_blank">ley 8.663 de coparticipación</a> es bastante estricta en cuanto a como  se reparten estos fondos hay otros análisis para hacer. La variación de estos datos en cada municipio deben seguir crecimientos iguales. A la <a href="http://andresvazquez.com.ar/data/ruta-del-dinero-cordobes/resources/cba/CIUDADES-FULL.ods" target="_blank">planilla terminada de resultados finales</a> le agregamos planillas que duplican las series de datos pero contemplando para cada dato su variación con el mes anterior. Esto me permitió detectar fallas pero también variaciones no esperadas.

Estos son los casos de Bower e Ycho Cruz que pasaron de Comunas a Municipios y multiplicaron su coparticipación en marzo de 2011.

 

<a href="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_055.png" target="_blank"><img class="aligncenter wp-image-95 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_055-300x157.png" alt="Selection_055" width="300" height="157"></a>

 

 

Al parecer en Marzo de 2011 hubo además recategorizaciones o cambios en el cálculo ya que Ana Zumaran y Cerro Colorado (entre otros) tuvieron cambios con respecto a las demás localidades.

Un dato notable es que entre enero de 2009 y abril de 2014 (donde termina la serie de datos liberados) el crecimiento de la coparticipación en los municipios fue del 350%, mucho más que cualquier estimación de inflación.

Para hacer más interesante estos datos se mezclaron con los del censo provincial 2008 e información de disponibilidad de sitio web (datos extraídos de <a href="http://municipedia.com" target="_blank">Municipedia</a>) y se colocaron en un mapa interactivo. Este mapa muestra cada ciudad como un circulo cuyo tamaño cambia para mostrar diferentes indicadores mencionados en este estudio (la ciudad de Córdoba se reubicó para poder respetar sus proporciones sin interferir con el mapa).

<a href="http://andresvazquez.com.ar/data/ruta-del-dinero-cordobes?dato=coparticipacion&amp;z=7&amp;l1=-32.66712488302566&amp;l2=-61.4466406875" target="_blank"><img class="aligncenter wp-image-96 size-medium" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/06/Selection_058-300x191.png" alt="Selection_058" width="300" height="191"></a>
</p><p style="text-align: center;"><strong><span style="color: #ff0000;">Click en el mapa para usar la versión interactiva de todos los datos procesados</span></strong></p>
Hasta aquí llega este informe, quedan <strong>propuestas y caminos abiertos para continuar</strong> con el uso de estos datos (<em>journalist needed</em>):

.- Los 44 archivos PDF, las extracciones de Tabula en CSV (algunas reordenadas por mi) y todos los archivos que use en este proceso se pueden descargar <a href="http://andresvazquez.com.ar/data/ruta-del-dinero-cordobes/resources/cba/" target="_blank">aquí.
</a>.- Hay numerosos municipios que tienen esa categorización sin tener los 2.000 habitantes requeridos por ley. ¿Por que sucede?
.- Analizar los municipios que si tienen página web y estudiar cuales de ellos liberan información (hay casos interesantes).
.- Cruzar este mapa con información del <a href="http://andresvazquez.com.ar/blog/cordoba-a-nivel-de-radio-censal/" target="_blank">censo nacional 2010</a> o con datos de las <a href="http://democraciaconcodigos.github.io/election-2013/" target="_blank">elecciones en córdoba</a> que ya están disponibles.
.-  Uno de los coeficientes calculados y disponibles en el mapa es el de <strong>coparticipación / habitante</strong> (uso datos de censo Cba 2008). Este tiene valores similares pero no iguales para todos los casos. ¿Es posible que la provincia haya aplicado los datos del censo 2010 (que <a href="http://andresvazquez.com.ar/blog/los-municipios-de-cordoba-no-existen/" target="_blank">no esta oficialmente calculado para municipios</a>)?</body></html>