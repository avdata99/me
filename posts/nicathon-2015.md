> Proyecto del colectivo [OpenDataCordoba](https://opendatacordoba.org/). El sitio del evento vive en [opendatacordoba.org/NICathon/](https://opendatacordoba.org/NICathon/). Este es un proyecto que lideré, pero el evento se organizó desde ODC.

![NICathon](/img/odc/nicathon/banner.jpg)

**NICathon** fue un hackathon dedicado a los datos del registro de dominios `.com.ar`, del **5 al 20 de marzo de 2015**. Continuación natural de la [recolección de datos sobre dominios argentinos](http://blog.opendatacordoba.org/datos-abiertos-sobre-dominios-argentinos/) en la que veníamos trabajando: la idea fue exponer públicamente lo relevado y proponer que la comunidad construyera visualizaciones, historias o análisis sobre esos datos.

## La zona .AR

Cada país administra su zona de dominios. En Argentina lo hace NIC.ar. Durante unos 20 años el registro fue gratuito, lo que permitió mucho emprendimiento y también mucha especulación. Desde el 5 de marzo de 2014 el servicio pasó a ser pago, y eso provocó la caída masiva de dominios — cosa que se ve clara en los datos liberados para el evento.

## Modalidad

15 días, datos publicados en más de un formato, y compromiso de difundir cada trabajo enviado: visualizaciones, historias, análisis, cruces con otros sets. El evento incluyó además el código fuente del API y de la [aplicación web+móvil](http://nic.opendatacordoba.org/) que ya habíamos publicado antes.

## Análisis posibles que sugerimos

- Medir el abandono de dominios después de que el servicio se hizo pago.
- Geolocalización automática de dominios según quién los registra.
- ¿Por qué hay dominios vencidos o en proceso de alta hace años, sin resolverse?
- Lectura automática de los sitios listados → mapa de tecnologías usadas en Argentina.
- Especulación con dominios que cambian periódicamente de fecha de reserva.
- Análisis de los DNSs para entender el mercado de hosting.
- Dominios "abandonados" y renovados justo antes del cobro.

## Consideraciones sobre los datos

- Casi 700.000 dominios — no la totalidad, sólo la parte que relevamos.
- Las fechas son las de detección, no las del cambio real.
- Entre mediados de 2012 y enero de 2014 el motor de lectura no funcionó por cambios en NIC.ar.
- Desde el 25/12/2014, gracias a Poderopedia, agregamos lectura automática del Boletín Oficial. Desde esa fecha sí podríamos considerar la base como población total.
- No guardamos dominios con acentos, eñes u otros caracteres no estándar.
- Sólo zona `.com.ar` (no `.org.ar`, `.tur.ar`, etc.).

## El análisis técnico

Quedó en otro post: [Datos abiertos sobre dominios .com argentinos](/blog/posts/datos-abiertos-sobre-dominios-com-argentinos/).

## Apoyaron el evento

[Poderopedia](http://www.poderopedia.org/) (especialmente Juan Eduardo, [@devpoderopedia](https://twitter.com/devpoderopedia)) y [Vía Libre](http://vialibre.org.ar). Asesoramiento de [Javier Pallero](https://twitter.com/javierpallero) y [Derecho entre Líneas](http://www.derechoentrelineas.org/) en la cuestión de publicar datos personales de registrantes.

![Poderopedia](/img/odc/nicathon/poderopedia-logo.png) ![Vía Libre](/img/odc/nicathon/vialibre-logo.gif)

## En los medios

- [TV Pública](https://andresvazquez.com.ar/data/otros/NICathon.mp4)
- [La Nación](http://lanacion.com.ar/1745843-presentan-una-herramienta-para-analizar-los-dominios-argentinos-registrados)
- [Página/12](http://www.pagina12.com.ar/diario/suplementos/cash/17-8376-2015-03-22.html)
- [Radio Mitre Bahía Blanca](https://andresvazquez.com.ar/data/otros/Entrevista-Radio-Mitre-Bahia-Blanca-por-ArNicApp.mp3)
