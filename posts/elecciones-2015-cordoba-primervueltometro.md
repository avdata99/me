> Proyecto del colectivo [OpenDataCordoba](https://opendatacordoba.org/). El sitio del proyecto vive en [opendatacordoba.org/elecciones2015/](https://opendatacordoba.org/elecciones2015/) — este post es un backup personal de mi participación.

Durante las elecciones nacionales 2015 (PASO, generales, balotaje) en OpenDataCordoba armamos una infraestructura para procesar y exponer los resultados oficiales en formatos abiertos. Yo fui uno más del equipo: trabajé sobre todo en el scraping de los datos de DINE+INDRA, la API en PHP y una visualización rápida llamada **PrimerVueltómetro**.

## Qué hicimos como equipo

- **Recolección de datos** desde el portal oficial DINE/INDRA cada vez que publicaba una nueva tanda. Los CSVs se descargaban y procesaban automáticamente.
- **API en PHP** que devolvía JSON listo para usar:
    - totales nacionales por alianza (con y sin lemas), PASO y definitivos
    - totales por provincia, departamento y elección (presidenciales, senadores, diputados, gobernador, etc.)
    - totales por lista en cada sección electoral
    - GeoJSON de departamentos de Córdoba
- **Visualizaciones** sobre esa API: el PrimerVueltómetro (proyección sobre el resultado de primera vuelta) y un dashboard del balotaje 2015.
- **Dataset abierto** del balotaje 2015 desagregado por mesa, en CSV, publicado para reutilización.

## Backup

El proyecto y el código vivieron en [github.com/OpenDataCordoba](https://github.com/OpenDataCordoba) y se publicaron desde el sitio de ODC. Si en algún momento ese sitio cae, este post es la nota mínima de qué se hizo y de mi rol concreto.
