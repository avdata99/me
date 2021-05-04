<html><body><p>¿Y que tal si los numerosos set de datos provinciales y nacionales disponibles pudieran analizarse por ciudad transversalmente?

Me pregunte esto porque en general trabajo con datos que son analizados individualmente. Me refiero a que los datos abiertos de censos o de elecciones en general son fuente de estudios de manera individual sobre el tema de los datos. Hacemos estudios sobre una elección o sobre un censo como conceptos más generales. Pero ¿que sucede si yo quiero <em>contar </em>la historia de una ciudad mirando solo los datos de ese gobierno local que han sidos publicados en sets de datos mas grandes a lo largo de la historia?

En general los análisis de datos son costosos y requieren de personal calificado. Los gobiernos locales no tienen acceso a esta valiosa información, son pocas las ciudades que realizan la inversión necesaria. Municipedia busca que los sets de datos que ya existen puedan ser cargados en una misma plataforma pero que se puedan visualizar por ciudad. De esta forma los esfuerzos por liberar información que ya se hacen podrán ser aprovechados de una forma simple y económica por gobiernos, periodistas e investigadores locales.

<img class="alignleft size-thumbnail wp-image-61" alt="Municipedia" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2014/04/Selection_010-150x150.png" width="150" height="150">

La idea del proyecto <a href="http://municipedia.com" target="_blank">municipedia</a> (<a href="http://twitter.com/municipedia" target="_blank">@municipedia</a>) es encargarse de presentar datos ya liberados en fichas individuales para cada ciudad permitiendo <strong>contar historias locales</strong>. Uno de los desafíos son los códigos de identificación con que las instituciones provinciales y nacionales etiquetan a cada ciudad. Por ejemplo para el ministerio de educación de San Luis el código de la ciudad de Merlo es distinto que para la Policía Federal.

La clave de M<em>unicipedia</em> es que cada set de datos agregado requiere poder <em>engancharse</em> a la base de datos pre-cargada en el sistema. Actualmente se resuelve con tablas accesorias que guardan los índices de las ciudades según las denominaciones que usa cada institución para poder reutilizar en el futuro.

Finalmente una aplicación de twitter permite un login para la carga de datos que ya esta abierta al público. Se usó la tecnología de google drive para distribuir plantillas con la lista de ciudades de Argentina y que los interesados puedan cargar nuevos datos.

<strong>Desafíos pendientes</strong>

Conseguir listas de ciudades de otros países para agregar al sistema, actualmente solo pueden incluirse datos de Argentina.
Permitir a los usuarios hacer visualizaciones con los datos existentes. Hoy solo se muestran listas de datos.
Incluir un sistema de control de los datos cargados al sistema por la comunidad como tiene Wikipedia.
Abrir un API para el consumo de datos desde otras aplicaciones.
Simplificar el proceso de carga de datos.
Liberar el código fuente (solo resta quitar datos privados de accesos a bases de datos, aplicaciones de twitter, etc)

<strong>Nota: </strong>El proyecto pudo ver su primera versión gracias a los datos que liberó <a href="http://twitter.com/manuelaristaran" target="_blank">Manuel Aristarán</a> y contó en un <a href="http://blog.jazzido.com/2013/09/08/base-de-datos-de-municipios-de-argentina/" target="_blank">post de su blog</a></p></body></html>