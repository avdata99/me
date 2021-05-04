<html><body><p>En el año 2009 note que no había un servicio de whois para los dominios argentinos. No sólo eso, <a href="http://nic.ar" target="_blank">NIC argentina</a> no tenía un API ni la posibilidad de automatizar tareas como registros y alertas más efectivas ante la caida de dominios. Decidí entonces tener mi propia base de datos y proveer de algunos servicios sobre dominios .com.ar

Si no te interesa la historia y quieres ir derecho a la documentación del API, <a href="http://andresvazquez.com.ar/data/nic-argentina/home/especificaciones" target="_blank">dirígete aquí</a>

La única forma de hacer esto en aquel momento (y al día de hoy, finales de 2013, también) es leer directo desde la página web. Para esto desarrollé un pequeño programa que hacia las consultas, leía la página web, tomaba la información y la guardaba en una base de datos.
No me malinterpreten, no hice esto para robar dominios que personas o empresas descuidaban y perdían o para buscar marcas y despues venderlas. En general todos condenamos esas acciones, yo también.

Surgió en ese momento otro desafío. ¿Como consigo que dominios buscar, que palabras, que frases?
Tomar toda la combinatoria posible era imposible, la cantidad estimada era de 38<sup>19</sup>
Tomé entonces texto aleatorios de la web y fue interesante, las palabras mas comunes empezaron a cargarse. Me di cuenta que no solo tenía que buscar palabras sueltas, cualquier grupo de palabras unidas sin espaciones o sepadas por "-" tambien servían.
Empezaron a aparecer dominios registrados y datos válidos pero la mayoría seguían siendo dominios no existentes.
Tome entonces libros argentinos completo en formato TXT y los resultados comenzaron a mejorar, nosotros registramos dominios así como escribimos.
Fui un poco más alla y cargué un diccionario completo en español (vía <a href="http://www.openoffice.org/es/" target="_blank">OpenOffice</a>) de 70.000 palabras.

Me di cuenta despues por cuales caminos había mas resultados, mi mayor desafío era no consultar dominios no existentes para no desperdiciar tiempo y esfuerzo del software que realizaba la tarea.
Tome entonces listas concretas de sustantivos en sus versiones masculinas y femeninas. Las conecte con articulos como prefijos, use listas de adjetivos.
Me metí en un terreno en el que me hubierá servido mucho saber de análisis semántico y gramatical

Finalmente todas estas heramientas juntas corrían diariamente en horários específicos y lo suficientemente distanciados en tiempo para que el servidor de NIC no empezara a rechazar mis conexiones. Use un servidor en mi propia casa con IP variable, sin eso no hubiera sido posible.

Finalmente NIC dejo de atender pedidos y di de baja mi servicio a mediados de 2012 (que se podía consultar en línea). Estimo que yo no era el único y los muchachos del servidor de NIC argentina se cansaron de atender este tipo demanda.

El resultado final son casi 375.000 dominios encontrados sobre un total de 2.2 millones totales en Argentina (segun datos que me compartieron desde NIC en el año 2012).
El historial de cambios en los dominios esta guardado, periodicamente hacía pings sobre los dominios, tambien se incluye esta información
Resguarde la mayoría los datos personales de los dueños de los dominios por cuestiones de privacidad, solo se publican sus nombres.

Cuento esto y pongo disponible el API porque no quiero tirar esta información, puede ser de utilidad para alguien. Tambien como ejemplo de que no es tan complicado, que NIC argentina debería tener un servicio de whois y un API para empresas que tienen muchos clientes y son responsables de la administración masiva de dominios.

Finalmente decidí continuar el proyecto y liberé la herramienta que uso. Puede <a href="https://github.com/avdata99/nic.ar.scrape" target="_blank">descargarse aquí</a>. Actualmente los datos se están actualizando manualmente y agregándose a la base de datos.

<a href="http://andresvazquez.com.ar/data/nic-argentina/home/especificaciones"><img class="alignleft size-medium wp-image-52" alt="api para nic.ar" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2013/12/nic.ar_-300x168.jpg" width="300" height="168"></a></p></body></html>