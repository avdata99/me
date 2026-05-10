Análisis presentado durante el [NICathon](/blog/posts/nicathon-2015/) (marzo 2015).

# Caída de dominios en NIC.ar al comenzar el cobro

El pasado 5 de marzo de 2014 [NIC Argentina](https://nic.ar) comenzo a cobrar por el uso de los dominios en la zona *.AR*.

Descargando los datos del [#NICathon](https://opendatacordoba.org/NICathon/) de [OpenDataCordoba](https://opendatacordoba.org/) podemos ver que entre el 5 de marzo de 2014 y el 5 de marzo de 2015 hay listados 188.222 dominios que cambiaron su fecha de vencimiento. Esto se puede deber a:

- Llegada a la fecha de vencimiento del dominio (con caída, renovación o solicitud de prórroga).
- Cambio de titular o nuevo registro ([ver detalles](/blog/posts/masiva-renovacion-de-dominios-nic/)).

La base de datos muestra los cambios percibidos en cada dominio monitoreado. Si bien esto no es exacto ni sobre la totalidad de los dominios en NIC se puede ver una tendencia en los movimientos de los dominios de la zona *AR*.

Analizando la nueva fecha de vencimiento por la que cambio podemos decir:

- Si la nueva fecha es 365 días superior a la fecha previa de vencimiento entonces decimos que hubo una renovación *limpia*.
- Si la nueva fecha de vencimiento es vacía, entonces sabemos que el dominio se venció y no se renovó.
- Si la cantidad de dias es menor a 365 o superior suponemos que se pidio una prórroga, se cambio de titular y por lo tanto de fecha o el dominio cambio de fecha de vencimiento mediante una [baja y re-registración para evitar el pago](/blog/posts/masiva-renovacion-de-dominios-nic/).

De los más de 188.000 dominio, casi el 67% fue dado de baja. Los datos en el gráfico a continuación muestran la estimación del tamaño de la caída de dominio una vez que comenzo a ser pago.

Aunque no pudimos conocer la cantidad de dominios registrados en la actualidad (no recibimos respuesta) recordamos que NIC informó en algún momento que teníamos registrados alrededor de 2.5 millones de dominios.

Si la estimación no es mala (lo entendemos asi por el tamaño de la muestra, 650.000 dominios) entonces en la actualidad podemos tener un poco más de 800.000 dominios para toda la zona *AR*.

[![Gráfico de caída de dominios luego del cobro](/img/data/caida-de-dominios-en-nic/screenshot.png)](/data/Caida-de-dominios-en-NIC/)

**Visualización interactiva:** [/data/Caida-de-dominios-en-NIC/](/data/Caida-de-dominios-en-NIC/)
