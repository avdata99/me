> Proyecto del colectivo [OpenDataCordoba](https://opendatacordoba.org/). El sitio de ayuda del proyecto vive en [opendatacordoba.org/funcionarios-cordoba/](https://opendatacordoba.org/funcionarios-cordoba/) y el código en [github.com/OpenDataCordoba/funcionarios-cordoba](https://github.com/OpenDataCordoba/funcionarios-cordoba). Este post es backup personal de mi participación.

**Funcionarios Córdoba** es un proyecto del grupo que se conecta a las listas oficiales de funcionarios públicos de Córdoba (provincia y ciudad) y detecta cambios, designaciones y renuncias. Lo detectado se publica automáticamente en la cuenta de Twitter [@funcionariosCBA](https://twitter.com/funcionariosCBA). Trabajé bastante en este proyecto.

## Qué hace

Un sistema chico que se conecta periódicamente a la lista de funcionarios de cada institución y detecta diffs:

- Poder Ejecutivo de la Provincia de Córdoba
- Poder Ejecutivo de la Municipalidad de Córdoba
- Tribunal de Cuentas (provincial y municipal)
- Poder Legislativo provincial
- Poder Judicial provincial
- Concejo Deliberante de la Municipalidad de Córdoba

Cada cambio se publica como tuit. La idea es bajísima fricción: no hay que armar una nota, el dato sale solo desde la fuente oficial.

## El problema más grande no es técnico

No todas estas instituciones publican y actualizan sus listas en formatos consumibles. Eso fue lo que más nos costó: convivir con páginas que cambian de URL, datos sin DNI (que es lo único que identifica unívocamente), HTMLs que rompen los parsers.

Por eso, en el sitio de ayuda del proyecto, lo que pedimos a los gobiernos no es "abran datos" en abstracto sino **lo mínimo concreto** para que el monitoreo no se rompa:

- una planilla simple con DNI + cargo, actualizada el mismo día del cambio
- URL estable (que no cambie)
- preferentemente un webservice (la Municipalidad de Córdoba tenía un [ejemplo](https://gobiernoabierto.cordoba.gob.ar/api/funciones/))

Ese pedido lo redacté yo en enero de 2019 cuando reescribí la página de ayuda.

## Cómo colaborar

Si sos parte de un gobierno y querés que tu institución entre al monitoreo, escribinos a [opendatacba@gmail.com](mailto:opendatacba@gmail.com).

Si sos desarrollador, el código está en [github.com/OpenDataCordoba/funcionarios-cordoba](https://github.com/OpenDataCordoba/funcionarios-cordoba) y aceptamos PRs.

## Relacionado

Más adelante hice algo parecido a nivel local: [Mapa de funcionarios de Villa María](/blog/posts/mapa-de-funcionarios-de-villa-maria/).
