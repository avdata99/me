<html><body><h3>¿Se pueden liberar todos los datos <em>individualmente</em> pero en realidad no liberar una base de datos completa?</h3>
Si, veamos el caso de NICAr.

Después de varios días sin servicio (planificados) y muchos cambios en su sistema, <a href="https://es.wikipedia.org/wiki/NIC_Argentina" target="_blank">NIC Argentina</a> apareció con un <a href="https://es.wikipedia.org/wiki/Captcha" target="_blank">captcha</a>:

<img class="aligncenter size-medium wp-image-252" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/07/Selecci%C3%B3n_055-300x176.png" alt="Selección_055" width="300" height="176">

NIC Argentina es la oficina (pública) encarga de la gestión de todos los dominios de la zona .AR (dominios <em>.com.ar</em>, <em>.org.ar</em>, etc). Todos los sitios webs registrados y en uso en esta zona son administrados por esta oficina. Desde hace muchos años uno puede acceder al sitio <a href="https://nic.ar" target="_blank">nic.ar</a> y consultar información acerca de un dominio en particular. Por ejemplo, usted puede saber quien es el dueño de este dominio, andresvazquez.com.ar:

<img class="aligncenter size-medium wp-image-253" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/07/Selecci%C3%B3n_057-300x204.png" alt="Selección_057" width="300" height="204">

Ahora, si usted quisiera saber cosas como:
<ul>
 	<li>¿Que otros dominios tiene un registrante?</li>
 	<li>¿Quien es el que tiene más dominios registrados?</li>
 	<li>¿Cuantos dominios se registran por día?</li>
</ul>
y muchos otras cosas, no podría. Quiero decir, <strong>usted puede ver cada árbol pero nunca el bosque</strong>.

Pero ¿y si tomara lápiz y papel e ingresara a cada uno de los dominios existentes (aunque no exista la lista, adivinando palabras y combinaciones de letras) e hiciera una lista manual para analizar?

De esta forma podría ver el bosque. Podría saber mucho más. Podría revisar que los dominios -por ejemplo- no tengan mas de un año de vigencia como especifica el reglamento. O podría encontrar que no es así (<a href="http://www.lanacion.com.ar/1745843-presentan-una-herramienta-para-analizar-los-dominios-argentinos-registrados" target="_blank">ver dominio que vence dentro de 100 años</a>).

En la vida real no es viable humanamente leer millones de sitios webs para tomar notas y construir una base de datos de este tamaño. Desde hace mucho tiempo y mediante técnicas de <a href="https://es.wikipedia.org/wiki/Web_scraping" target="_blank">scraping</a> uno puede delegar esa tarea a una computadora. De esta forma la computadora puede pasar horas consultando uno o más sitios webs simultáneamente (cada uno de los dominios en NIC.ar por ejemplo) y guardando los datos importantes en forma de una base de datos organizada.

De esta forma <strong>uno puede construir la base de datos</strong> (el bosque) a la que se le niega el acceso. Si la información de cada dominio es libre (los árboles), entonces se entiende que es una base de datos libre. Más aún se entiende ya que desde hace algún tiempo NIC Argentina publica en una nueva sección del Boletín Oficial (construida ad-hoc) todos los días, todos los dominios que se registran junto a los datos completos del registrante.

¿Como hace un gobierno o empresa que quiere limitar el consumo masivo de sus datos?

<img class="aligncenter" src="http://www.extremetech.com/wp-content/uploads/2011/11/captcha-selection1.jpg" width="926" height="431">
Usa un <strong>captcha</strong>, una especie de <em>validador de humanos</em> que impide que las computadoras accedan a la información que se desea ocultar.

NIC Argentina entonces (como ya han hecho muchos otros antes) libera <strong>todos</strong> los datos pero sólo de a uno por vez.

Desde la agrupación <a href="http://opendatacordoba.org/" target="_blank">OpenDataCórdoba</a> desde hace algunos años mantenemos una base de datos muy detallada de dominios en NIC Argentina. Todos los datos se publican en <a href="http://nic.opendatacordoba.org/" target="_blank">un sitio web</a> y <a href="https://play.google.com/store/apps/details?id=com.phonegap.arnicapp" target="_blank">aplicación móvil</a>.

<img class="aligncenter size-medium wp-image-254" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2016/07/Selecci%C3%B3n_058-300x238.png" alt="Selección_058" width="300" height="238">

Los datos acerca de dominios de internet en el mundo en general escasean, no se liberan en general ya que representan activos muy valiosos. Sin embargo hemos liberado nuestra base de datos completa el año pasado en un evento llamando <a href="http://opendatacordoba.org/NICathon/" target="_blank">NICAthon</a> que invitaba a analistas de datos a producir información basada en estos datos.

Lamentablemente este trabajo de años debe discontinuarse hasta que NIC Argentina revea su decisión o exponga otros canales de información que nos permitan continuar con esta aplicación.

 </body></html>