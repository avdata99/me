Análisis presentado durante el [NICathon](/blog/posts/nicathon-2015/) (marzo 2015).

# Tecnología de los sitios webs en Argentina

Según [informe de NetCraft](http://news.netcraft.com/archives/2015/02/24/february-2015-web-server-survey.html) el uso de los servidores webs en sitios activos en el mundo esta liderado por los servidores **Apache**.

La mitad de los casi 200 millones de sitios webs analizados usan Apache, lo siguen -lejos- los sitios alojados con Nginx, IIS y GSE (Google).

Analizando 250.000 sitios webs argentinos con datos que libera [OpenDataCordoba](https://opendatacordoba.org/) en su [#NICathon](https://opendatacordoba.org/NICathon/) podemos analizar la realidad Argentina.

En este caso la ventaja de [Apache](https://es.wikipedia.org/wiki/Servidor_HTTP_Apache) sobre los demás es mayor. Se puede ver además una paridad entre el uso de servidores [IIS (de Microsoft)](https://es.wikipedia.org/wiki/Internet_Information_Services) y [Nginx](https://es.wikipedia.org/wiki/Nginx).

El uso de servidores de aplicaciones Google (por ejemplo BlogSpot) es diez veces menor (8% vs 0.8%) en Argentina en comparación con lo informado por NetCraft.

Puede notarse (viendo la lista completa) que es frecuente el uso de servidores con versiones consideradas inseguras y que ya no deberían estar en uso. Hasta se han encontrado sitios web administrados por Microsift IIS 4.0 o Nginx 0.6.

Otras curiosidades son los 57 sitios alojados en Amazon S3 y los 23 en gitHub.com.

La información para Argentina fue extraida leyendo los *headers* que informan los servidores al ser consultado por herramientas simples (CURL se uso en este caso). Si bien es posible que los servidores voluntariamente puedan modificar u omitir esta información no creemos que esta sea una costumbre habitual.

[![Servidores en el mundo según NetCraft y en Argentina según NICathon](/img/data/servidores-en-argentina/servidores-top.png)](/data/Servidores-en-Argentina/)

Ingresando un poco más en los detalles podemos ver las versiones usadas de los tres servidores web mas populares:

[![Versiones de Apache, Microsoft IIS y Nginx en sitios argentinos](/img/data/servidores-en-argentina/versiones-servidores.png)](/data/Servidores-en-Argentina/)

## Lenguajes de programación usados

Algo que NetCraft no informa es la tecnología detras del servidor web. Nos referimos a el lenguaje de programación usado para construir los sitio web.

En este caso si es más común que los datos no se informen (menos de la mitad no lo hace) el siguiente gráfico muestra las tecnologíaas utilizadas en los casos en los que es informado.

Es una lástima que esta forma de deteccíon de sitios no sea capaz de relevar correctamente el uso de tecnologías Python o Java (usamos para el caso el *header **X-Powered-By***). Seguramente un análisis más detallado del contenido HTML de los sitios permitiría saber un poco mejor las tecnologías y los frameworks utilizados. Quedará para otro estudio.

[![Tecnología detrás del webserver — PHP vs ASP.NET](/img/data/servidores-en-argentina/lenguajes.png)](/data/Servidores-en-Argentina/)

**Visualización interactiva:** [/data/Servidores-en-Argentina/](/data/Servidores-en-Argentina/)

**Todos los datos de este estudio pueden descargarse:**

- [JSON — Todos los servidores revisados (headers completos, 85MB)](/data/Servidores-en-Argentina/data/servers-headers-final.json)
- [Resumen solo con Servidores, X-Powered-By (23.4MB)](/data/Servidores-en-Argentina/data/servers.csv)
- [Acumulado por tipo de servidor (CSV)](/data/Servidores-en-Argentina/data/servers_resumen.csv)
- [Acumulado por servidor y versión (CSV)](/data/Servidores-en-Argentina/data/servers_version_resumen.csv)
- [Acumulado por tecnología usada (CSV)](/data/Servidores-en-Argentina/data/powered_resumen.csv)
- [Acumulado por tecnología Y versión usada (CSV)](/data/Servidores-en-Argentina/data/powered_version_resumen.csv)
