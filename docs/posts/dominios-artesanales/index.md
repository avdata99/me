<html><body><p>Finalmente, después de años de recolección de datos sobre dominios argentinos de la zona ComAr los datos fueron liberados y <a title="Datos libres sobre dominios argentinos" href="http://opendatacordoba.org/NICathon/data.html" target="_blank">se pueden descargar</a>.

Antes de hacer un análisis duro de los datos (hay varios muy interesantes para hacer y que esperamos compartir pronto) quiero compartir algunas impresiones sobre estos datos.

La primera impresión que tengo es que los datos en <a href="https://nic.ar" target="_blank">NIC Argentina</a> son administrados artesanalmente, me refiero a que algunos de los eventos no suceden automáticamente. Más bien parecen administrados a mano. Algunos ejemplos:

<strong>Caída de dominios</strong>
Según el reglamento de NIC, los dominios vencidos no quedan automáticamente disponibles para registro, hay 30 días extras de tolerancia. Luego de estos 30 días de <em>espera</em> los dominios deberían caer. Nuestra herramienta de monitoreo de sitios detecta en general caídas luego de los 33 días en general. A veces llega a 40 y en otros casos no caen nunca. No hay un evento automático que libere los dominios, <a href="http://nic.opendatacordoba.org/#deberianCaer" target="_blank">no parece tener una lógica</a>.

<strong>Renovación máxima de un año</strong>

Hay dominios que se han renovado por más del año que permite según <a href="https://nic.ar/normativa-vigente.xhtml" target="_blank">reglamento NIC</a>. Además del caso del dominio justich.com.ar que <a href="http://www.lanacion.com.ar/1745843-presentan-una-herramienta-para-analizar-los-dominios-argentinos-registrados" target="_blank">vence dentro de 100 años</a> hay otros casos donde la renovación fue por mas un año. Hemos encontrado casos que luego de reclamos se volvio atrás la fecha vencimiento del dominio. Los datos se pueden analizar en la base, lo que esta a la vista es que no es un sistema automático el que asigna las nuevas fechas de vencimiento al renovar sino que esto puede hacerse a mano. El caso del dominio eventoplus.com.ar que al momento de registrase aparecio con fecha de inicio 16/1/2015 y vencimiento 21/1/2015 (solo 5 días despues) es uno de mucho ejemplos. Quiero decir, los administradores de NIC tienen acceso directo a las fechas de inicio y vencimiento de los dominios. La base de datos muestra muchos ejemplos de esto. Se hace a mano.

<strong>Fechas de vencimiento hacia atrás</strong>
Hay detectados algunos casos donde la fecha de vencimiento del dominio vuelve hacia atrás. Los casos detectados pueden verse <a href="http://andresvazquez.com.ar/data/Dominios-para-atras/" target="_blank">aquí</a>.

<strong>Situación legal de los dominio</strong>
Muchos dominios están con <a href="http://nic.opendatacordoba.org/index.html#listByStatus/medida%20cautelar" target="_blank">medidas cautelares pendientes</a> y esto se aclara al hacer la consulta vía web, pero otros, que posiblemente estén sufriendo disputas similares no lo informan y sin embargo siguen funcionando. Este es el caso del dominio argentina.com.ar que no se renovo desde el 01/01/2014 y sin embargo funciona. Quiero decir con esto que no imagino una función interna y automática en NIC que marque el dominio como en disputa legal y proceda a informarlo en la web. Da la sensación que esto también se hace a mano.

<strong>No todo es manual</strong>
El 5 de marzo de 2014 el registro de dominios comenzó a ser pago. Desde algunas semanas antes muchos dominios que vencían después de esa fecha (o sea, tenían que pagar próximamente) misteriosamente <a href="http://andresvazquez.com.ar/data/Masiva-renovacion-de-dominios-en-NIC/" target="_blank">se dieron de baja y se volvieron a registrar</a>. Fueron miles, algunos perteneciente a registrantes masivos. ¿Se imaginan un administrador de 100 dominios dándolos de baja uno por uno y registrándolos de nuevo para prorrogar unos meses el pago de sus dominios?
Yo tampoco, algunas cosas, al parecer, se pueden automatizar.

<strong>Formas de esquivar los pagos</strong>
Hecha la ley siempre hay alguien que encuentra una trampa. La forma que han encontrado algunos usuarios de conservar acaparados los dominios sin pagar es simular un nuevo registro con métodos de pagos <em>off-line</em>, esto le da al usuario algunos días para realizar el pago. Deja al dominio en un estado de <em>reserva</em> que una vez finalizado puede volver a repetirse. <a href="http://andresvazquez.com.ar/data/Reservar-dominios-como-forma-de-apropiacion/" target="_blank">Hemos detectados dominios re-reservados hasta 15 veces</a>.

<strong>Indice de análisis de datos realizados</strong>
<a href="http://andresvazquez.com.ar/data/Reservar-dominios-como-forma-de-apropiacion/" target="_blank">La reserva de dominios como modo de apropiación</a>.
<a href="http://andresvazquez.com.ar/data/Masiva-renovacion-de-dominios-en-NIC/" target="_blank">Renovación masiva de dominios</a>.
<a href="http://andresvazquez.com.ar/data/Dominios-para-atras" target="_blank">Dominios que van hacia atras</a>.
<a href="http://andresvazquez.com.ar/data/Uso-de-DNSs-en-Argentina/" target="_blank">Uso de los DNSs en Argentina</a>.
<a href="http://andresvazquez.com.ar/data/Caida-de-dominios-en-NIC/" target="_blank">Cae el 67% de los dominios regsitrados</a>.
<a href="http://andresvazquez.com.ar/data/Servidores-en-Argentina/" target="_blank">Análisis de 250.000 servidores argentinos</a>.

<strong>Disclaimer</strong>
Durante la elaboración de estas tareas nos encontramos con muchas personas con una visión muy crítica de NIC, diría, exageradamente crítica. No compartimos esa posición, no hicimos esto para combatir a NIC, construimos <a href="http://nic.opendatacordoba.org/" target="_blank">una herramienta</a> para mirar lo que pasa, proponer mejoras y denunciar si hubiera situaciones irregulares.
Creo que el paso de gratuito a libre fue muy positivo, muchos dominios dejaron de ser posesión de especuladores. Por otro lado, dominios en poder de ONGs o personas con ganas de expresarse, cayeron.
La renovación del sitio web y la automatización de los pagos son cosas muy positivas aunque todavía falte.

<strong>Gracias</strong>
Muchas personas colaboraron para que esto sea posible, espero no olvidarme de ninguno:
a <a href="https://twitter.com/devpoderopedia" target="_blank">Juan Eduardo</a> por la magia de sus scripts y por convencer a <a href="https://twitter.com/miguelpaz" target="_blank">Miguel</a> de que <a href="http://www.poderopedia.org/poderopedia/index/chapters" target="_blank">Poderopedia</a> nos acompañe
a <a href="https://twitter.com/scannopolis" target="_blank">Evelin</a>, por los mates y el apoyo de <a href="https://twitter.com/fvialibre" target="_blank">Vía Libre</a>
a <a href="https://twitter.com/javierpallero" target="_blank">Javier Pallero</a>, por su asesoramiento legal
a <a href="http://www.estebanmagnani.com.ar/" target="_blank">Esteban</a>, <a href="https://twitter.com/rsametband" target="_blank">Ricardo</a> y <a href="https://twitter.com/unabuenarazon" target="_blank">Leandro</a> por la difusión en los medios
a Francuza y los chicos de <a href="http://opendatacordoba.org/" target="_blank">OpenDataCordoba</a> por todo, como siempre.</p></body></html>