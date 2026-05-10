# Migración de `/data/` y `/data/hackathons.html` al blog

Plan para mover los análisis y eventos publicados como HTML estáticos en
`custom-statics/data/` (servidos en `/data/...`) a posts del blog Nikola.

> **Etapa actual: planificación.** Esta etapa lista todo el contenido a migrar
> y deja un `- [ ]` por ítem. La **etapa 2** consiste en crear los posts uno
> por uno y marcar `- [x]`.

---

## Estrategia general

Cada bloque de los HTML legados cae en una de cuatro categorías:

- **A. Ya hay post.** El link en `index.html` apunta a `/blog/<slug>/`. Acción:
  ninguna sobre el contenido. Si el post no menciona la viz/data del `/data/`,
  agregar el link al final del post existente. No requiere redirección nueva.
- **B. Externo (OpenDataCordoba u otros).** Acción: ninguna.
- **C. Visualización JS interactiva** (D3, chart.js, Google Maps, DataTables).
  Mantenerla viva en `/data/<slug>/` (`FILES_FOLDERS` la sigue copiando tal
  cual) y crear un **post envoltorio** corto en `posts/` con: introducción
  (qué es, cuándo, por qué), captura, link a la viz interactiva, link a los
  datos crudos (CSV/JSON) si aplica. Post y viz quedan en URLs distintas.
- **D. HTML simple (texto + tabla pequeña).** Convertir el cuerpo a Markdown
  e ingresar como `posts/<slug>.md`. Borrar la copia bajo `custom-statics/data/`
  y agregar redirección 301 `data/<slug>/ → posts/<slug>/` en `conf.py`.

### Cómo crear un post (recordatorio)

Un post Nikola son dos archivos hermanos: `posts/<slug>.md` + `posts/<slug>.meta`.
El `.meta` lleva:

```
.. title: <Título legible>
.. slug: <slug>
.. date: <YYYY-MM-DD HH:MM:SS>
.. tags: OpenData, hackathon
.. description: <una frase>
```

El cuerpo del `.md` es Markdown plano. Mirar `posts/escuelas-docentes-y-matriculados-en-cordoba-entre-1998-y-2010.md`
como ejemplo corto y limpio.

### Redirecciones

Agregar al bloque `REDIRECTIONS` de `conf.py` cada par `["data/<slug>/", "/posts/<slug>/"]`.
Las redirecciones sólo aplican a la categoría **D** (cuando borramos el HTML
estático) y a las dos páginas índice:

- `data/` (`index.html`) → `/categories/datos/` o `/index.html`
- `data/hackathons.html` → `/categories/hackathons/` o `/index.html`

Para crear esas categorías basta con etiquetar los posts nuevos con `tags: datos`
o `tags: hackathons` y dejar que Nikola genere el índice.

### Indexado

Los posts nuevos quedan automáticamente en el feed RSS, en la home y en las
páginas de tag. Asegurar que **todos** los posts migrados lleven al menos una
de estas tags principales para que sean discoverables: `OpenData`, `datos`,
`hackathons`, `Cordoba`, `dominios-ar` (según corresponda).

---

## Items de `/data/index.html`

Orden cronológico inverso, igual que el original.

### Octubre 2015

- [ ] **Elecciones y padrones** — Categoría **A**.  
  Post existente: [`elecciones-y-padron`](/blog/elecciones-y-padron/).  
  Datos extra en [Fusion Tables](https://www.google.com/fusiontables/DataSource?docid=1GZOQlWYwolkr2FnfdbBOqF1gTZHI77hgN4Pgd9XY).  
  Acción: verificar que el post mencione el link a Fusion Tables; si no, agregarlo al final.

### Septiembre 2015

- [ ] **Cuántas personas votan por cada domicilio (Villa Allende)** — Categoría **A**.  
  Post local existente: [`cuantas-personas-votan-en-cada-domicilio`](/blog/cuantas-personas-votan-en-cada-domicilio/).  
  El bloque original dice "en el blog de OpenDataCordoba" pero el post local
  cubre el mismo análisis. Verificar y, si hace falta, citar también el de OpenDataCordoba.

- [ ] **Comparando padrones electorales** — Categoría **A**.  
  Post existente: [`comparando-padrones-electorales`](/blog/comparando-padrones-electorales/).

- [ ] **Padrones por localidad — análisis interactivo** — Categoría **C** (6 vizs estáticas).  
  Páginas en `/data/padrones/`:
  - `Pilar-2015.html`, `Mendiolaza-Gobernador-2015.html`, `Unquillo-Paso-2015.html`,
    `Saldan-Paso-2015.html`, `Rio-Ceballos-Gobernador-2015.html`,
    `Villa-Allende-Municipales-2015.html`
  
  Hay además páginas extra en la carpeta (`Colonia-Caroya`, `Concepcion`,
  `Corral-de-Bustos`, `Hernando`, `La-Puerta`, `Sacanta`) que no aparecen
  linkeadas desde `index.html` — incluirlas igual.  
  Acción: un único post envoltorio `posts/padrones-por-localidad-2015.md`
  con tabla de localidades y links a cada HTML.  
  Cobertura mediática a citar: [CBA24N](http://www.cba24n.com.ar/content/villa-allende-hallan-domicilios-con-decenas-de-empadronados),
  [La Voz del Interior](http://www.lavoz.com.ar/politica/un-hogar-con-169-votantes-en-villa-allende).

### Marzo 2015 — NICathon (paquete de 6 análisis)

Estos 6 análisis salieron del NICathon. Son visualizaciones JS pesadas (chart.js,
DataTables, Google Charts). Categoría **C** para todos: post envoltorio + viz
intacta. Tag común: `dominios-ar`.

- [ ] **La reserva de dominios como modo de apropiación**  
  Viz: [`/data/Reservar-dominios-como-forma-de-apropiacion/`](/data/Reservar-dominios-como-forma-de-apropiacion/) (DataTable).  
  Datos: `cambios-en-reservas.csv`, `cambios-en-reservas.json`.  
  Slug propuesto: `reservar-dominios-como-apropiacion`.

- [ ] **Renovación masiva de dominios en NIC**  
  Viz: [`/data/Masiva-renovacion-de-dominios-en-NIC/`](/data/Masiva-renovacion-de-dominios-en-NIC/) (chart + DataTable).  
  Datos: `dominios-actualizados.csv`, `Registrantes-que-renovaron-dominios.csv/.json`.  
  Slug: `masiva-renovacion-de-dominios-nic`.

- [ ] **Dominios que van hacia atrás**  
  Viz: [`/data/Dominios-para-atras/`](/data/Dominios-para-atras/) (chart).  
  Slug: `dominios-para-atras`.

- [ ] **Uso de DNSs en Argentina**  
  Viz: [`/data/Uso-de-DNSs-en-Argentina/`](/data/Uso-de-DNSs-en-Argentina/) (chart + tabla).  
  Slug: `uso-de-dns-en-argentina`.

- [ ] **Cae el 67% de los dominios registrados**  
  Viz: [`/data/Caida-de-dominios-en-NIC/`](/data/Caida-de-dominios-en-NIC/) (chart).  
  Slug: `caida-de-dominios-en-nic`.

- [ ] **Análisis de 250.000 servidores argentinos**  
  Viz: [`/data/Servidores-en-Argentina/`](/data/Servidores-en-Argentina/) (6 charts Google).  
  Slug: `servidores-en-argentina`.

> Alternativa más liviana: un sólo post **"NICathon: 6 análisis sobre dominios .com.ar"**
> que liste los 6 con un párrafo cada uno. Tomar esta opción si Andrés prefiere
> menos posts por encima de granularidad. Recomiendo la versión granular: cada
> análisis tiene cobertura mediática propia y rinde como post individual.

### Agosto 2014

- [ ] **Educación en Córdoba por fracción 2010 (CEPyD)** — Categoría **C**.  
  Viz: [`/data/CEPyD-Cordoba-Capital-2010/`](/data/CEPyD-Cordoba-Capital-2010/) (Google Maps).  
  Colaboración con [CEPyD](http://www.cepyd.org.ar/).  
  Slug: `educacion-cordoba-capital-cepyd-2010`.  
  Texto base: "Gráfico basado en datos del Centro de Estudios de Población y Desarrollo. Desarrollo en colaboración con la institución."

### Junio 2014

- [ ] **Coparticipación en Córdoba (ruta del dinero cordobés)** — Categoría **A**.  
  Post existente: [`la-coparticipacion-provincial-de-recursos-en-cordoba`](/blog/la-coparticipacion-provincial-de-recursos-en-cordoba/).  
  Mapa interactivo en [`/data/ruta-del-dinero-cordobes/?dato=coparticipacion`](/data/ruta-del-dinero-cordobes/?dato=coparticipacion).  
  Acción: confirmar que el post linkea al mapa.

### Mayo 2014

- [ ] **Escuelas de Córdoba 1998/2010** — Categoría **A**.  
  Post existente: [`escuelas-docentes-y-matriculados-en-cordoba-entre-1998-y-2010`](/blog/escuelas-docentes-y-matriculados-en-cordoba-entre-1998-y-2010/).  
  Datos crudos en `/data/Evolucion-de-la-educacion-en-Cordoba-entre-1998-y-2010/`
  (CSVs, notebook Jupyter, PNGs).  
  Acción: confirmar que el post linkea a esa carpeta de datos.

- [ ] **Radios municipales en Córdoba** — Categoría **C** sin viz local.  
  El bloque enlaza a `cordoba-argentina-segun-censo-2010/mapa/...` que **no
  está** en `custom-statics/data/`. Verificar si la app vive en otro lado;
  si no, escribir un post breve sólo descriptivo (Categoría **D** simplificada).  
  Slug: `radios-municipales-cordoba-2014`.

### Marzo 2014

- [ ] **Córdoba según censo 2010** — Categoría **A**.  
  Post existente: [`cordoba-a-nivel-de-radio-censal`](/blog/cordoba-a-nivel-de-radio-censal/).  
  Mapa interactivo `cordoba-argentina-segun-censo-2010/` no está local; si
  reaparece, linkear desde el post.  
  Código en [GitHub HackathonFOPEA/CensoCordoba2010](https://github.com/HackathonFOPEA/CensoCordoba2010).

### Septiembre 2013

- [ ] **Comercio y Justicia (scrape de tapas)** — Categoría **A**.  
  Post existente: [`las-tapas-del-diario-comercio-y-justicia`](/blog/las-tapas-del-diario-comercio-y-justicia/).  
  Carpeta `comercio-y-justicia/` no está local — si aparece, linkear.

- [ ] **Siglos de fundación de ciudades argentinas** — Categoría **A**.  
  Post existente: [`siglos-de-fundacion-de-las-ciudades-argentinas`](/blog/siglos-de-fundacion-de-las-ciudades-argentinas/).  
  Carpeta `municipios-argentinos-siglo-de-fundacion/` no está local.

- [ ] **Incendios en Córdoba (mapa septiembre 2013)** — Categoría **D** sin viz local.  
  Carpeta `incendio-en-cordoba/` no está local. Escribir post breve descriptivo.  
  Slug: `incendio-en-cordoba-septiembre-2013`.

- [ ] **Análisis de combustibles Argentina 2010-2013** — Categoría **D** sin viz local.  
  Carpeta `combustibles-en-Argentina/` no está local. Probablemente solapada
  con el post existente sobre tasa vial; revisar si hace falta nuevo post o
  basta con extender el existente.  
  Slug tentativo: `combustibles-argentina-2010-2013`.

- [ ] **Consumo de combustibles en Córdoba (D3.js, semestral)** — Categoría **A** parcial.  
  Post existente: [`consumo-de-combustibles-en-cordoba-a-un-ano-de-la-implementacion-de-la-tasa-vial`](/blog/consumo-de-combustibles-en-cordoba-a-un-ano-de-la-implementacion-de-la-tasa-vial/).  
  Carpeta `tasa-vial/` no está local. Si aparece, sería envoltorio **C**.

### Diciembre 2013

- [ ] **API de dominios argentinos (375.000 .com.ar)** — Categoría **A**.  
  Post existente: [`api-de-dominios-argentinos`](/blog/api-de-dominios-argentinos/).  
  Carpeta `nic-argentina/` no está local.

### Noviembre 2012

- [ ] **Designación de funcionarios** — Categoría **D**.  
  Carpeta: `/data/designacion-de-funcionarios/` (HTML simple + 1 CSV).  
  Texto base: "Datos extraídos del boletín oficial que me compartieron en un
  hackathon y re-comparto por aquí. Designación de funcionarios en Argentina
  entre 2011 y 2012."  
  Slug: `designacion-de-funcionarios-2011-2012`.  
  Acción: convertir el HTML a markdown, mover el CSV a `files/` o dejarlo
  como descarga adjunta, agregar redirección.

---

## Items de `/data/hackathons.html`

Cada bloque es una nota corta sobre un evento. Categoría **D** universalmente:
posts breves de 5-15 líneas con texto, fechas, links a sitios del evento,
cobertura mediática y, si existe, link a viz/aplicación construida.

Tag común sugerida: `hackathons`. Tags secundarias por evento (`Cordoba`,
`OpenData`, `Datafest`, etc.).

- [x] **Octubre 2015 — Jornadas GoberNET**  
  Sitio: [opendatacordoba.org/jornadas/GoberNET](http://opendatacordoba.org/jornadas/GoberNET).  
  Texto base: "Colaboración general en la organización y armado del sitio web
  de invitación del evento."  
  Slug: `jornadas-gobernet-2015`.

- [x] **Junio 2015 — HackatONG 2015**  
  Sitio: [opendatacordoba.org/HackatONG/2015](http://opendatacordoba.org/HackatONG/2015/),
  cobertura: [semanatic.com](http://www.semanatic.com/hackatong/).  
  Slug: `hackatong-2015`.

- [x] **Mayo 2015 — III Encuentro de Data Science Córdoba**  
  Sitio: [datasciencecordoba.github.io/encuentros/mayo-2015](http://datasciencecordoba.github.io/encuentros/mayo-2015.html).
  Video: [YouTube](https://www.youtube.com/watch?v=NxysD0OicLs).
  Meetup: [meetup.com/.../220559752](http://www.meetup.com/Encuentros-Data-Science-Cordoba/events/220559752/).  
  Slug: `iii-encuentro-data-science-cordoba`.

- [x] **Abril 2015 — II Encuentro de Data Science Córdoba**  
  Sitio: [datasciencecordoba.github.io/encuentros/abril-2015](http://datasciencecordoba.github.io/encuentros/abril-2015.html).
  Video: [YouTube](https://www.youtube.com/watch?v=Ha8SkqUlsmA).  
  Slug: `ii-encuentro-data-science-cordoba`.

- [x] **Marzo 2015 — NICathon**  
  Sitio: [opendatacordoba.org/NICathon](http://opendatacordoba.org/NICathon/),
  app: [nic.opendatacordoba.org](http://nic.opendatacordoba.org).
  Cobertura: [TV Pública](https://andresvazquez.com.ar/data/otros/NICathon.mp4),
  [La Nación](http://lanacion.com.ar/1745843-presentan-una-herramienta-para-analizar-los-dominios-argentinos-registrados),
  [Página/12](http://www.pagina12.com.ar/diario/suplementos/cash/17-8376-2015-03-22.html),
  [Radio Mitre Bahía Blanca](https://andresvazquez.com.ar/data/otros/Entrevista-Radio-Mitre-Bahia-Blanca-por-ArNicApp.mp3).  
  Existe ya el post [`datos-abiertos-sobre-dominios-com-argentinos`](/blog/datos-abiertos-sobre-dominios-com-argentinos/)
  con contexto. Decidir: ¿extender ese post con la sección "el evento" o crear
  un post nuevo `nicathon-2015`? Recomiendo nuevo post enfocado en el evento
  (organización, equipo, prensa) y que linkee al post técnico existente.  
  Slug: `nicathon-2015`.

- [x] **Marzo 2015 — Encuentro de Data Science Córdoba (I)**  
  Sitio: [datasciencecordoba.github.io/encuentros/marzo-2015](http://datasciencecordoba.github.io/encuentros/marzo-2015.html).
  Cobertura en [blog OpenDataCordoba](http://opendatacordoba.org/blog/encuentro-de-data-science-cordoba/),
  [SRT UNC](https://www.youtube.com/watch?v=3XZ_z7qUaeo&feature=youtu.be&t=1m26s).  
  Slug: `i-encuentro-data-science-cordoba`.

- [x] **Septiembre 2014 — Hack(at)ONG + Program.AR**  
  Hackdash: [hackatong.hackdash.org](http://hackatong.hackdash.org/),
  repos: [github.com/HackatONG-ProgramAR](https://github.com/HackatONG-ProgramAR),
  sitio: [hackatong-programar.github.io](http://hackatong-programar.github.io).
  Cobertura: [Día a Día](http://www.diaadia.com.ar/cordoba/el-hackatong-dejo-17-aplicaciones-punto),
  [Cadena 3](http://www.cadena3.com/contenido/2014/09/08/134336.asp).  
  Existe post [`hackatong-programar`](/blog/hackatong-programar/). Confirmar si
  cubre todo o si conviene un post separado. Probable: **A**, sin migración nueva.

- [x] **Junio 2014 — La ruta del dinero**  
  Solapa con el post existente [`la-coparticipacion-provincial-de-recursos-en-cordoba`](/blog/la-coparticipacion-provincial-de-recursos-en-cordoba/)
  y el mapa en [`/data/ruta-del-dinero-cordobes/`](/data/ruta-del-dinero-cordobes/).
  Cobertura: [La Nación](http://blogs.lanacion.com.ar/data/argentina/hackaton-regional-larutadeldinero/),
  [Telam](http://larutadeldinero.info/).  
  **A**, sin migración nueva. Si el post no menciona el evento como hackathon
  regional, agregarlo.

- [x] **Mayo 2014 — Hackathon FOPEA**  
  Repos: [github.com/HackathonFOPEA](https://github.com/HackathonFOPEA),
  sitio: [hackathonfopea.github.io](http://hackathonfopea.github.io/).
  Cobertura: [La Voz](http://www.lavoz.com.ar/ciudadanos/cuatro-proyectos-de-programadores-y-periodistas-en-el-congreso-de-fopea),
  [La Nación](http://blogs.lanacion.com.ar/data/datos-abiertos/hackaton-y-talleres-en-congresofopea/).  
  Slug: `hackathon-fopea-2014`.

- [x] **Noviembre 2013 — Democracia con Códigos**  
  Mapa: [democraciaconcodigos.github.io/election-2013](http://democraciaconcodigos.github.io/election-2013/),
  grupo: [OpenDataCordoba (Google Group)](https://groups.google.com/forum/#!forum/open-data-cordoba).  
  Slug: `democracia-con-codigos-2013`.

- [x] **Agosto 2013 — Hackathon Program.AR**  
  Lanzamiento Portal Datos Públicos. Equipo de [Represión Financiera en la dictadura](http://cnv.hhba.info/).
  Cobertura: [MinCyT](http://www.mincyt.gob.ar/noticias/se-realizo-el-primer-hackaton-de-datos-publicos-9113),
  [Educ.AR](http://www.educ.ar/sitios/educar/noticias/ver?id=119004),
  [OKFN AR](http://ar.okfn.org/2013/08/05/hotelviz-visualizacion-con-las-ciudades-de-mayor-turismo-en-argentina/),
  [La Nación](http://www.lanacion.com.ar/1605789-el-gobierno-anuncio-programar-su-primera-hackaton),
  [Telam](http://www.telam.com.ar/notas/201308/27485-masiva-concurrencia-al-hackaton-de-datos-publicos.html).  
  Slug: `hackathon-programar-2013`.

- [x] **Noviembre 2012 — Datafest La Nación**  
  "Cruce de datos entre integrantes de sociedades anónimas y funcionarios
  públicos. Premio compartido del evento."
  Cobertura: [La Nación](http://blogs.lanacion.com.ar/data/argentina/el-datafest-desde-adentro/),
  [iLab](http://blog.ilabamericalatina.org/2012/11/datafest-como-lograr-que-los-datos.html).  
  Slug: `datafest-la-nacion-2012`.

---

## Otros

- [ ] **Carpeta `censo-2010-familia/`** — no está enlazada desde `index.html`.
  Es un trabajo final académico ("Familia y provincias argentinas.pdf",
  notebook + ALL-RESULTS.csv). Decidir: dejar como recurso suelto o post envoltorio.
  No bloquea la migración; revisar al final.

---

## Cierre de la migración (después de marcar todo)

Cuando todos los `- [ ]` estén `- [x]`:

1. **Reemplazar `custom-statics/data/index.html`** por una página que
   directamente redirija al tag `datos` o al índice del blog.
   Alternativa: un `index.html` mínimo que liste los posts nuevos como
   `archive` (mantiene la URL pero sin contenido legacy).
2. **Reemplazar `custom-statics/data/hackathons.html`** análogamente con
   redirección al tag `hackathons`.
3. **Borrar las carpetas `custom-statics/data/<slug>/`** que pertenezcan a
   ítems de categoría **D** (su contenido ya quedó migrado al post).
   Mantener las de categoría **C** (las viz interactivas siguen vivas).
4. **Confirmar `REDIRECTIONS`** en `conf.py`: cada D-redirect agregado, más
   los dos índices (`data/`, `data/hackathons.html`).
5. **`uv run nikola build`** y revisar que ningún link interno quedó roto
   (`uv run nikola check -l` para chequear links).
6. Borrar este archivo.
