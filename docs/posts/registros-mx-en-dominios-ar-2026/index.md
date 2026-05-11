[Originalmente publicado como hilo en Twitter](https://x.com/dominiosAR/status/2049662721180774532).

¿A quién le delegan el correo los dominios argentinos? Para responderlo miramos los registros MX de DNS sobre nuestra base de [dominiosAR](/blog/posts/tecnologia-de-dominios-argentinos-2026/).

De los ~585.000 dominios que tenemos relevados, 421.000 están delegados a algún DNS y 322.000 tienen al menos un registro MX. A marzo de 2026 NIC declara 692.000 dominios totales, así que la muestra es bastante representativa.

![Total de dominios relevados y delegados a DNS](/img/twitter/registros-mx-en-dominios-ar-2026/1.png)

![Dominios con registro MX detectado: 322.000 sobre 421.000 delegados](/img/twitter/registros-mx-en-dominios-ar-2026/2.jpeg)

Casi el 60% de esos dominios con MX apunta a su **propio dominio**\*. Cerca del 1% (unos 2.500) son inválidos: apuntan a `localhost`. Y a un 4,5% nuestra expresión regular no logró clasificarlo.

![Distribución de destinos MX: ~60% dominio propio, ~1% localhost, 4,5% sin clasificar](/img/twitter/registros-mx-en-dominios-ar-2026/3.jpeg)

De los 115.000 dominios que apuntan **explícitamente** a proveedores externos, Google y Hostinger comparten el primer lugar con cerca del 70% del mercado entre los dos. ¿Se imaginaban a [@Hostinger](https://x.com/Hostinger) ahí, por encima de [@Microsoft](https://x.com/Microsoft)?

![Ranking de proveedores externos de MX: Google y Hostinger lideran con ~70% combinado](/img/twitter/registros-mx-en-dominios-ar-2026/4.jpeg)

¿Y los sitios de gobierno (`gov.ar` + `gob.ar`)? El 64% apunta a dominio propio\*.

![Dominios .gov.ar y .gob.ar: 64% apunta a dominio propio](/img/twitter/registros-mx-en-dominios-ar-2026/5.jpeg)

De los 328 dominios de gobierno que sí declaran un proveedor externo, el principal —como suponíamos— es Microsoft.

![Proveedores externos de MX en dominios de gobierno: Microsoft lidera](/img/twitter/registros-mx-en-dominios-ar-2026/6.jpeg)

---

\* Con seguridad no existen tantos sitios que gestionen sus propios mails. Ese 60% seguramente esconde cosas por detrás. ¿Cuál te parece que sería la mejor estrategia para descubrir el proveedor real?

**Nota extra.** El uso de `localhost` como MX no es un descuido: es política de uno de los proveedores de hosting.

¿Qué más le preguntarían a estos datos?
