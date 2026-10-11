# Personal site

Static site for andresvaqzquez.com.ar  
Also available at https://avdata99.github.io/me/  

## Build

Built with [Nikola](https://getnikola.com/) + [Pagefind](https://pagefind.app/) (buscador estatico). Versiones fijadas en `requirements.txt`. Use [`uv`](https://github.com/astral-sh/uv) to manage the Python env so we don't pollute the system.

**Siempre buildear con `./build.sh`**, no con `nikola build` solo: el script corre `nikola build` y despues `pagefind --site docs`, que regenera el indice del buscador en `docs/pagefind/`. Si se saltea Pagefind, el buscador (`/pages/buscar/`) queda desactualizado.

```bash
./build.sh                                        # crea .venv si hace falta, instala requirements.txt, nikola build + pagefind
uv run python -m http.server 8000 -d docs        # preview local en http://localhost:8000 (buscador incluido)
```

`uv run nikola serve -b` tambien sirve para previsualizar (bajo `/blog/`).

Output goes to `docs/` (committed - GitHub Pages serves from there). After a build, commit both the source changes and the regenerated `docs/` (incluido `docs/pagefind/`).

### Buscador

- Solo se indexan posts y paginas: `themes/hack/templates/base.tmpl` marca su `<main>` con `data-pagefind-body` (los listados, tags y archivo no entran).
- Para excluir una pagina o post puntual, agregar la metadata `.. pagefind: no` (asi esta `pages/buscar.html`).
- La UI esta en `pages/buscar.html`; acepta `?q=termino` en la URL.

## CV

El CV vive en `cv/` (fuentes Markdown) y se compila a HTML + PDF con un script propio. Los outputs van a `custom-statics/cv/`, que Nikola copia al root del sitio en `/cv/...`.

> **Importante:** `nikola build` **no** compila el CV — sólo copia los HTML/PDF ya generados. Si editás un `cv/cv-andres-*.md`, **primero** corré `./cv/build/build.py` y **después** `nikola build`. Si te olvidás, los archivos en `docs/cv/` quedan desactualizados.

```bash
cd cv/build && ./build.py     # 1) regenera HTML + PDF en custom-statics/cv/
cd ../.. && uv run nikola build  # 2) los publica a docs/
```

Detalles y prerequisitos en [`cv/build/README.md`](cv/build/README.md).

## Convertir un `.md` "falso" (HTML del import de WordPress) a Markdown real

Muchos `posts/*.md` y `pages/*.md` son en realidad HTML con extensión `.md` (legado del import de WordPress). Para pasar uno a Markdown plano:

```bash
sudo apt install pandoc       # una sola vez
pandoc -f html -t gfm posts/<slug>.md -o /tmp/<slug>.md
# revisá /tmp/<slug>.md, limpiá basura de WP (clases wp-*, atributos style=, etc.)
mv /tmp/<slug>.md posts/<slug>.md
uv run nikola build           # verificá el render
```

Conviene ir migrando archivo por archivo, no en bulk: el HTML que dejó WordPress suele traer cosas raras (`<br/>` sueltos, `class="wp-image-NNN"`, `style="..."`) que pandoc transcribe literalmente y queda mejor borrar a mano que dejar.

