
[Originalmente publicado como hilo en Twitter](https://x.com/dominiosAR/status/2052559441145323558).

Analizamos casi 600.000 dominios Argentinos. Intentamos hacer una peticion a la home page de cada uno. Conseguimos casi 400k respuestas (66%). Miramos tambien los encabezados de las respuestas y algunas partes del contenido HTML.

![Total de dominios .AR vigentes en abril de 2026: 697.130](/img/twitter/tecnologia-de-dominios-argentinos-2026/1.jpeg)

![Tablero de dominiosAR: 597.659 sitios analizados, 66,2% responden, 84,7% HTTPS, 23,1% HSTS, 25% CSP](/img/twitter/tecnologia-de-dominios-argentinos-2026/2.jpeg)

Analisis del header `server`. Si bien el servidor puede responder lo que quiera aquí, estos son nuestros resultados. 380k dominios devolvieron ese encabezado (casi todos). ¿Te sorprende ver a Apache todavía primero? En 2015 era 67% ([nuestro análisis anterior](/blog/posts/servidores-en-argentina/)).

![Distribución del header server en 2026: apache 34,2%, cloudflare 21,5%, nginx 12,8%, litespeed 11,8%](/img/twitter/tecnologia-de-dominios-argentinos-2026/3.jpeg)

![Distribución del header server en 2015: Apache 67%, Microsoft-IIS 14,6%, nginx 14,5%](/img/twitter/tecnologia-de-dominios-argentinos-2026/4.jpeg)

La novedad es Cloudflare. Para sorpresa de nadie Microsoft IIS cae bruscamente. Nginx se mantiene.

Vamos al header `X-Powered-By`. La principal novedad aqui es que se esta dejando de usar. Solo 84k de los casi 400k de sitios que respondieron lo usan. Para sorpresa de nadie Mumm-Ra sigue vivo. ASP se desploma.

![Stack tecnológico por X-Powered-By en 2026: php 72%, asp.net 10,9%, next.js 5,5%, hostingerwebsitebuilder 3,6%, express 2,6%](/img/twitter/tecnologia-de-dominios-argentinos-2026/5.jpeg)

![Mumm-Ra, el villano de ThunderCats, como metáfora de ASP.NET resucitando](/img/twitter/tecnologia-de-dominios-argentinos-2026/6.png)

![Distribución de X-Powered-By en 2015: PHP 66,4%, ASP.NET 28,6%, Plesk 3,6%](/img/twitter/tecnologia-de-dominios-argentinos-2026/7.jpeg)

Vamos al HTML. Analizamos el meta `generator`. Hay que decir que el 68% de los sitios no lo declara. Son otras cosas. Solo 126k sitios usa algun generador de contenido. Aqui WP y sus amigos lideran. Sorprende que el Wordpress a secas no es el 1°.

![Productos detectados via meta generator: elementor (WP) 31,6%, wordpress 20,3%, slider revolution (WP) 9,7%, site kit (WP) 5,4%, wix 4,5%](/img/twitter/tecnologia-de-dominios-argentinos-2026/8.jpeg)

Finalmente si los agrupamos podemos decir que el 82% de los sitios generados por algún CMS son Wordpress. Posiblemente PHP sigue vivo solo por esto. ¿Vos que pensas?

![CMS real (plataforma subyacente): wordpress 82%, wix 4,7%, hostinger 2,6%, joomla 1,8%, mobirise 1%](/img/twitter/tecnologia-de-dominios-argentinos-2026/9.jpeg)
