<html><body><p>Vivo en Mendiolaza hace 30 años, desde joven recuerdo que había una sola empresa de colectivos, no recuerdo haber viajado muchas veces cómodo en mis viajes a la universidad a finales de los 90's. Si bien éramos pocos ya era un problema el transporte en aquella época.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>La realidad actual cambio mucho, <a href="http://blog.opendatacordoba.org/demografia-con-cartas-marinas/">la evolución de los padrones electorales</a> muestran la explosión de Mendiolaza (Córdoba) y toda la zona de Sierras Chicas (las localidades al noroeste de la capital provincial). La cantidad de electores en el padrón de Mendiolaza paso de 4.147 (2007) a   11.529 (2017), 178,01% en 10 años (la población argentina crece 1% anual aprox.)</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":473} -->
<figure class="wp-block-image"><img src="/blog/wp-content/uploads/2018/11/image.png" alt="" class="wp-image-473"><figcaption><br></figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Aunque ahora existen múltiples empresas de transporte que pasan por mi ciudad todavía es un problema poder contar con un servicio eficiente. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Vale aclarar que el departamento Colon (donde esta ubicado Mendiolaza) no cuenta con otra vía de transporte público. No hay trenes u otro sistema rápido de transporte ni parece haber un plan para ello. Para recorrer los 20 kilómetros que nos separan de la Capital se requieren entre 50 y 90 minutos.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":474,"align":"left","width":98,"height":90} -->
<div class="wp-block-image"><figure class="alignleft is-resized"><img src="/blog/wp-content/uploads/2018/11/image-1.png" alt="" class="wp-image-474" width="98" height="90"></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Trabajo en el Gobierno de la Ciudad de Córdoba donde también el transporte es un tema clave y de alta demanda social. Nos llevó un año pero conseguimos desarrollar la aplicación <em><strong><a href="https://play.google.com/store/apps/details?id=ar.gob.cordoba.gobiernoabierto.go" target="_blank" rel="noreferrer noopener" aria-label="Trabajo en el Gobierno de la Ciudad de Córdoba donde también el transporte es un tema clave y de alta demanda social. Nos llevó un año pero conseguimos desarrollar la aplicación Go basada exclusivamente en el GPS que toda unidad de transporte tiene. (abre en una nueva pestaña)">Go</a></strong></em> basada exclusivamente en el GPS que toda unidad de transporte tiene.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Este no es un tema menor, si bien la frecuencia es clave, la posibilidad de saber donde esta y cuanto falta para que venga el colectivo es importante para planificar mejor un viaje y perder menos tiempo en esperas. Además es posible saber si la unidad de transporte esta desviada de su recorrido habitual</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":475} -->
<figure class="wp-block-image"><img src="/blog/wp-content/uploads/2018/11/image-2.png" alt="" class="wp-image-475"></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":476,"align":"left","width":111,"height":79} -->
<div class="wp-block-image"><figure class="alignleft is-resized"><img src="/blog/wp-content/uploads/2018/11/image-3.png" alt="" class="wp-image-476" width="111" height="79"></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Para el transporte interurbano el Gobierno de la Provincia de Córdoba ha dispuesto la aplicación <em><a href="http://mibondiya.cba.gov.ar/" target="_blank" rel="noreferrer noopener" aria-label="Para el transporte interurbano el Gobierno de la Provincia de Córdoba ha dispuesto la aplicación MiBondiYa que permite saber los horarios de colectivos y en algunos casos la posición GPS en tiempo real en las unidades. Es interesante pero al tratar de usarla me doy con algunos problemas:
 (abre en una nueva pestaña)">MiBondiYa</a></em> que permite saber los horarios de colectivos y en algunos casos la posición GPS en tiempo real en las unidades. Es interesante pero al tratar de usarla me doy con algunos problemas:<br></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>No puedo ver a todas las unidades en un mismo mapa. Solo se ve el mapa para una unidad específica de una empresa particular. No hay un mapa integrado con todo.</li><li>No puedo consultar según la zona en la que estoy y obtener los resultados de todas las empresas que pasan por aquí, debo hacerlo una vez para cada una de las empresas.</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Resueltos estos inconvenientes sería una solución más interesante. En mi caso <strong>saber exactamente donde esta el colectivo que espero podría hacerme decidir si salir de mi casa en auto o no.</strong> Es por esto que decidí conectarme a los datos de este sistema y mostrarlos de otra forma. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Lamentablemente los datos no están expuestos de una forma amigable para que aplicaciones de terceros la reutilicen. De todas formas existen técnicas que se pueden aplicar en estos casos para <em>leer</em> los datos de un sitio web y transformarlos en información reutilizable.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Tomé el desafió de armar un mapa de colectivos que van desde Mendiolaza hasta Córdoba que muestre todas las unidades (sumando los horarios esperados en los casos donde el GPS no está disponible). Me llevó dos días, es una versión inicial pero entiendo que puede mejorarse.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":485} -->
<figure class="wp-block-image"><img src="/blog/wp-content/uploads/2018/11/image-5.png" alt="" class="wp-image-485"></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Como tomé los datos de <strong>TODO</strong> el sistema de transporte provincia <strong>puede reutilizarse para cualquier otro recorrido interurbano en Córdoba.</strong> Todo el código utilizado quedó <a href="https://github.com/avdata99/my-bondi-ia">abierto en un repositorio</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":478} -->
<figure class="wp-block-image"><img src="/blog/wp-content/uploads/2018/11/image-4-1024x599.png" alt="" class="wp-image-478"></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finalmente los colectivos Mendiolaza-Córdoba pueden consultarse en este primer beta desde <a href="https://bondi.mendiolaza.com.ar/bondis/mapa/">este sitio</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>El sistema guarda todos los datos que recoge por lo que podría eventualmente ser de utilidad para analizar datos de frecuencias (solo en los casos donde esta el GPS disponible).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph --></body></html>