<html><body><p>Hace algunos días hice un <a href="http://blog.opendatacordoba.org/cuantas-personas-votan-por-cada-domicilio/" target="_blank">análisis sobre el padrón electoral de Villa Allende</a> (Córdoba, AR). Luego de esto algunas personas de la ciudad vecina de Mendiolaza (mi ciudad, limítrofe con Villa Allende) me enviaron copia del padrón para hacer un proceso similar.

Este segundo padrón me permitió además hacer la siguiente prueba
</p><blockquote>¿Hay electores repetidos?</blockquote>
<img class="aligncenter size-medium wp-image-207" src="http://andresvazquez.com.ar/blog/wp-content/uploads/2015/08/Selecci%C3%B3n_009-300x158.png" alt="Selección_009" width="300" height="158">

Uno podría intuir que no. Las elecciones fueron muy cercanas.
El padrón de Villa Allende corresponde a las elecciones para intendente del 26/7/2015, el de Mendiolaza fue el usado 21 días antes en las elecciones a Gobernador (aún no esta listo el que se usará para las elecciones a intendente el próximo 6/9/2015).

Sin embargo hay ocho electores repetidos en ambos padrones. Algunos incluso tienen la misma dirección en ambos. <a href="https://github.com/avdata99/padrones-electorales/blob/master/comparativa-padrones-Mendiolaza-y-Villa-Allende-2015.csv" target="_blank">Ver</a>.
<table border="1" cellspacing="0"><colgroup width="75"></colgroup> <colgroup span="2" width="78"></colgroup> <colgroup width="966"></colgroup> <colgroup width="901"></colgroup>
<tbody>
<tr>
<th align="left" height="17">DNI</th>
<th align="left">Padron 1</th>
<th align="left">Padron 2</th>
<th align="left">Datos en Padron 1</th>
<th align="left">Datos en Padron 2</th>
</tr>
<tr>
<td align="right" height="17">16833139</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">AMUCHASTEGUI, MARIA IRIS DEL VALLE.
<strong>QUITO 407</strong></td>
<td align="left">AMUCHASTEGUI MARIA IRIS DEL VALLE.
<strong>MZA 24 L 1</strong></td>
</tr>
<tr>
<td align="right" height="17">20528421</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">CONTRERAS, PATRICIA DEL CARMEN.
<strong>BIALET MASSE 54</strong></td>
<td align="left">CONTRERAS PATRICIA DEL CARMEN.
<strong>MZA 10 L 17</strong></td>
</tr>
<tr>
<td align="right" height="17">28268614</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">DE MARCO, FLORENCIA.
<strong>GERONA 1205</strong></td>
<td align="left">DE MARCO FLORENCIA.
<strong>MZ.65LT.3-ECIA.Q2</strong></td>
</tr>
<tr>
<td align="right" height="17">26313446</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">JUAREZ, RICARDO OSCAR.
<strong>LONDRES 540</strong></td>
<td align="left">JUAREZ RICARDO OSCAR.
<strong>LONDRES 540</strong></td>
</tr>
<tr>
<td align="right" height="17">29605760</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">JULIA, MARIA GUADALUPE.
<strong>PJE VERGOGCANE 83</strong></td>
<td align="left">JULIA MARIA GUADALUPE.
<strong>LOS TILOS 1520</strong></td>
</tr>
<tr>
<td align="right" height="17">30189179</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">MONJE, VALERIA EDITH.
<strong>LOS ANDES 1184</strong></td>
<td align="left">MONJE VALERIA EDITH.
<strong>MALVINAS 130</strong></td>
</tr>
<tr>
<td align="right" height="17">23513076</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">OCANTO, HECTOR GUILLERMO.
<strong>NUEVA GRANADA 268</strong></td>
<td align="left">OCANTO HECTOR G.
<strong>DEL TALAR-LAVANDA M291L 7 399</strong></td>
</tr>
<tr>
<td align="right" height="17">35612915</td>
<td align="left">Villa Allende</td>
<td align="left">Mendiolaza</td>
<td align="left">SOSA HEREDIA, MARCELO ERNESTO.
<strong>NUEVA ZELANDIA 778</strong></td>
<td align="left">SOSA HEREDIA MARCELO ERNESTO.
<strong>DE LA LUNA 585</strong></td>
</tr>
</tbody>
</table>
¿Podemos saber si estas personas efectivamente votaron en ambas elecciones?

No, no es información pública quienes votaron y quienes no. Tampoco lo son los padrones de una forma orgánica. No se distribuyen (en formatos útiles) por internet.

Esto no supone un caso grave de corrupción, mas bien parece una desprolijidad preocupante. Revisando el padrón de Mendiolaza se puede ver también como muchos votantes no tienen un domicilio claro. Domicilios como <em>Calle pública s/n</em> o con nombres de calles sin número o direcciones descritas como la intersección entre dos calles.
<blockquote><strong>Los padrones electorales necesitan pasar procesos de aprobación mas elaborados. La justicia electoral tiene mucho trabajo interesante para hacer (y para mostrar). </strong></blockquote>
Los datos usado y el código fuente del análisis están disponibles aquí:
<a href="https://github.com/avdata99/padrones-electorales" target="_blank">github.com/avdata99/padrones-electorales</a></body></html>