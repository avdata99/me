<html><body><p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":525,"align":"left","width":116,"height":201,"linkDestination":"custom"} -->
<div class="wp-block-image"><figure class="alignleft is-resized"><a href="https://play.google.com/store/apps/details?id=ar.gob.cordoba.gobiernoabierto.go"><img src="/blog/wp-content/uploads/2019/02/image-3.png" alt="" class="wp-image-525" width="116" height="201"></a></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>En octubre de 2018 la Municipalidad de Córdoba lanzó la <a href="https://play.google.com/store/apps/details?id=ar.gob.cordoba.gobiernoabierto.go">aplicación móvil llamada </a><em><a href="https://play.google.com/store/apps/details?id=ar.gob.cordoba.gobiernoabierto.go">Go.</a></em> Su finalidad es proveer información precisa de cada unidad del transporte público de pasajeros con la finalidad de mejorar la experiencia de los usuarios de este servicio.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Al momento de su salida había aplicaciones similares en Argentina pero ninguna (que yo conozca) que permita <em>seguir</em> al colectivo por su GPS en tiempo real. Incluso cuando el colectivo se desvía por cortes de tránsito los usuarios pueden notarlo y re-ubicarse para alcanzarlo.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":526,"linkDestination":"custom"} -->
<figure class="wp-block-image"><a href="https://twitter.com/JMGonzalez30/status/1070334451186585601" target="_blank" rel="noreferrer noopener"><img src="/blog/wp-content/uploads/2019/02/image-4.png" alt="" class="wp-image-526"></a><figcaption><strong>Nota: Ese día había protestas en la vía pública </strong></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Tan difícil de creer que estos datos era reales que este usuario grabó mientras esperaba el colectivo esperando ser defraudado.</p>
<!-- /wp:paragraph -->

<!-- wp:core-embed/youtube {"url":"https://www.youtube.com/watch?v=beszgsTij4k","type":"video","providerNameSlug":"youtube","className":"wp-embed-aspect-4-3 wp-has-aspect-ratio"} -->
<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-4-3 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://www.youtube.com/watch?v=beszgsTij4k
</div></figure>
<!-- /wp:core-embed/youtube -->

<!-- wp:paragraph -->
<p><a href="https://andresvazquez.com.ar/blog/una-app-mas/">Conté hace un tiempo</a> (con motivo del lanzamiento de otra aplicación) la gran cantidad de trabajo que significa llegar a esto y las oportunidades que se abren luego de estas publicaciones.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>La aplicación <em>Go</em> representa un esfuerzo particularmente complejo en cuanto a la organización de los datos preexistente: </p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Las ubicación y especificaciones (lineas que la usan) de las paradas</li><li>Los recorridos geolocalizados de cada línea.</li><li>La flota activa de colectivos.</li><li>El geoposicionamiento en tiempo real de las unidades</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Estos datos se encontraban algunos en poder de la municipalidad en formatos variados, otros como parte del sistema de gestión de flota de las empresas de transporte. Comenzar a trabajarlos y procesarlos deja ver la parte del <em>iceberg</em> que una aplicación simple no permite percibir. <strong>Detrás de </strong><em><strong>Go</strong></em><strong> hay miles de horas de trabajo y sobre todo muchos datos. </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Esta reorganización de los datos nos permitiría además (todavía no está listo) tener un servicio de datos en formato <a href="https://developers.google.com/transit/gtfs/?hl=es">GTFS.</a>* Este formato es el estándar usado en otras ciudades del mundo para compartir datos de transporte y el que usan las aplicaciones más usadas (Google Maps, Apple, etc). <strong>Una ciudad sin GTFS no puede decir que ha terminado de abrir sus datos de transporte.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Todos estos datos en control municipal, organizados y antes de lanzar <em>Go</em> nos permitieron <strong>desarrollar tableros de control interno</strong> que permitían a personal de transporte ver en tiempo real donde estaban las unidades y cuantas de ellas se encontraban prestando servicio. Esto permite mejorar sensiblemente el control de la calidad del servicio subiendo el nivel de datos en poder del municipio en su dialogo con los prestadores del servicio.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Sin embargo la cantidad de datos recibidos ** nos permitían hacer análisis más detallados y complejos que requerían más y mejor equipo del que teníamos.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size">Mano en la data</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><em><a rel="noreferrer noopener" aria-label='"CAF financiará proyectos que usan la ciencia de datos para el diseño de políticas públicas en la Argentina" (abre en una nueva pestaña)' href="https://www.caf.com/es/actualidad/noticias/2018/10/caf-financiara-proyectos-que-usan-la-ciencia-de-datos-para-el-diseno-de-politicas-publicas-en-argentina/?parent=14258&amp;social=twitter" target="_blank">"CAF financiará proyectos que usan la ciencia de datos para el diseño de políticas públicas en la Argentina"</a></em> Por suerte encontramos que <a rel="noreferrer noopener" aria-label="CAF (abre en una nueva pestaña)" href="https://www.caf.com/" target="_blank">CAF</a> estaba buscando conectar científicos de datos y políticas públicas.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>CAF financiaba con hasta <strong>US$ 10.000</strong> a 5 equipos que presentaran propuestas. Se presentaron 10 equipos (Ministerios de Nación Argentina y otras ciudades de nuestro país). Luego de mostrar <a rel="noreferrer noopener" aria-label="en un workshop junto a científicos que escucharon nuestros problemas (abre en una nueva pestaña)" href="https://www.lanacion.com.ar/2183447-danza-con-datos-cuando-varias-disciplinas-hablan-un-idioma-141x-118-cm" target="_blank">en un workshop junto a científicos que escucharon nuestros problemas</a> (<a rel="noreferrer noopener" aria-label="acompañados por un equipo de la Fundación Sadosky (abre en una nueva pestaña)" href="http://www.fundacionsadosky.org.ar/se-financiaran-proyectos-que-usan-la-ciencia-de-datos-para-el-diseno-de-politicas-publicas-en-la-argentina/" target="_blank">acompañados por un equipo de la Fundación Sadosky</a>) el trabajo que estábamos realizando <strong>la Municipalidad de Córdoba fue seleccionada</strong>. <br>Con esta financiación un equipo de UBA/CONICET trabajó junto a nuestro equipo para sacar mejor provecho de toda la nueva información de transporte que estábamos procesando.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Actualmente estamos integrando todo el trabajo conjunto a nuestras herramientas preexistentes y esperamos publicar (y liberar como software libre para otras ciudades) los resultados finales.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Es muy importante destacar que la totalidad de los fondos se invirtieron en tecnología que es propiedad de la Municipalidad y que incrementará las capacidades propias instaladas en los equipos internos.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size">Conclusiones</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>La gestión del sistema de transporte de cualquier ciudad mediana o grande sin datos y análisis es seguramente pobre o incompleta. Mirar todo este cúmulo de datos detenidamente deja ver mucho mejor y a un nivel mucho mas detallado que pasa con este servicio que usan cientos de miles de personas cada día.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"customFontSize":12} -->
<p style="font-size:12px">*Córdoba tuvo el primer GTFS de Argentina que lamentablemente se discontinuó. Impulsado por un activista de la ciudad, <a rel="noreferrer noopener" aria-label="Gastón Ávila (abre en una nueva pestaña)" href="https://twitter.com/AvilaGas" target="_blank">Gastón Ávila</a> (<a rel="noreferrer noopener" aria-label="contó un poco del tema (abre en una nueva pestaña)" href="http://blog.opendatacordoba.org/transporte-publico-y-datos-publicos/" target="_blank">acá cuenta un poco del tema</a>).<br>** Por ejemplo la posición GPS cada ~20 segundos de las 900 unidades de transporte</p>
<!-- /wp:paragraph --></body></html>