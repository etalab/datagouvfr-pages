import re
import unidecode

from bs4 import BeautifulSoup
import mistune
from mistune.directives import DirectiveToc
from mistune.directives.toc import extract_toc_items

r = re.compile(r'^(\s*)', re.MULTILINE)

# Code borrowed and adapted from https://github.com/lepture/mistune/blob/master/mistune/directives/toc.py#L138
def render_toc_ul(toc):
    """Render a <ul> table of content HTML. The param "toc" should
    be formatted into this structure::
        [
          (toc_id, text, level),
        ]
    For example::
        [
          ('toc-intro', 'Introduction', 1),
          ('toc-install', 'Install', 2),
          ('toc-upgrade', 'Upgrade', 2),
          ('toc-license', 'License', 1),
        ]
    """
    if not toc:
        return ''

    s = '<ul class="fr-sidemenu__list">\n'
    levels = []
    for k, text, level in toc:
        item = '<a href="#{}" class="fr-sidemenu__link" target="_self">{}</a>'.format(k, text)
        if not levels:
            s += '<li class="fr-sidemenu__item">' + item
            levels.append(level)
        elif level == levels[-1]:
            s += '</li>\n<li class="fr-sidemenu__item">' + item
        elif level > levels[-1]:
            s += '\n<ul class="fr-sidemenu__list">\n<li class="fr-sidemenu__item">' + item
            levels.append(level)
        else:
            last_level = levels.pop()
            while levels:
                last_level = levels.pop()
                if level == last_level:
                    s += '</li>\n</ul>\n</li>\n<li class="fr-sidemenu__item">' + item
                    levels.append(level)
                    break
                elif level > last_level:
                    s += '</li>\n<li class="fr-sidemenu__item">' + item
                    levels.append(last_level)
                    levels.append(level)
                    break
                else:
                    s += '</li>\n</ul>\n'
            else:
                levels.append(level)
                s += '</li>\n<li class="fr-sidemenu__item">' + item

    while len(levels) > 1:
        s += '</li>\n</ul>\n'
        levels.pop()

    return s + '</li>\n</ul>\n'

dirToc = DirectiveToc()
markdown_renderer_with_toc_directive = mistune.create_markdown(escape=False,
        plugins=[DirectiveToc()])

with open('donnees-geo.md', 'r') as input_file:
    content = input_file.read()

html_tree = markdown_renderer_with_toc_directive(content)
content_resulting = []

directives_tags = """---
title: Données géographiques
keywords:
  - geo
  - adresses
  - SIG
  - geomatique
  - geographie
  - cartographie
description: Page inventaire des données géographiques essentielles.
content_type: html
---
"""

content_resulting.append(directives_tags)

title = "Les données à composante géographique"
illustration_url = "https://user-images.githubusercontent.com/72090652/201092205-31a8911c-844c-4f59-b652-8b27cda0c217.svg"
basic_description = """<p>
          Les données à composantes géographiques sont souvent indispensables pour réaliser des analyses. Sont référencées ici les principaux jeux de données disponibles sur <a href="http://data.gouv.fr/">data.gouv.fr</a>.
          Celle-ci n'est pas exhaustive et est
          <a href="https://github.com/datagouv/datagouvfr-pages/blob/master/pages/donnees-geo.md" target="_blank">
            ouverte aux contributions
          </a>
          .
        </p>
        <p>
          Un certains nombre de ces données font office de référentiel qui servent de pivot avec d'autres jeux de données. Elles font parties
          <a href="https://www.data.gouv.fr/fr/pages/spd/reference/">
            du SPD (Service Public de la Donnée)
          </a>
          . Voir aussi
          <a href="https://guides.etalab.gouv.fr/qualite/lier-les-donnees-a-un-referentiel/" target="_blank">
            cet article sur comment lier des données à un référentiel
          </a>
        </p>"""

levels_to_inf_3 = [i for i in extract_toc_items(markdown_renderer_with_toc_directive, content) if i[2] < 3]
left_menu = render_toc_ul(levels_to_inf_3)

main_content_template = """<section class="section-blue section-main">
  <div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
      <div class="fr-col">
        <h1>{}</h1>
      </div>
      <div class="fr-col-12">
        <div class="fr-highlight">
          <p>{}
          </p>
        </div>
      </div>
      <Sidemenu
        class="fr-col-12 fr-col-md-4 not-prose"
        button-text="Dans cette rubrique"
        :sticky-full-height="true"
      >
        <template #title>
          <img
            class="fr-responsive-img fr-hidden fr-displayed-lg fr-mb-4w"
            src="{}"
            alt=""
          >
          <p class="mb-0 fr-sr-only-lg">Menu</p>
        </template>
        {}
      </Sidemenu>
      <div class="fr-col-12 fr-col-md-8">{}</div>
    </div>
  </div>
</section>
""".format(title, basic_description, illustration_url, left_menu, html_tree)

'''
main_content_template = """<section class="section-blue section-main">
  <div class="fr-container">
    <div class="fr-grid-row fr-grid-row--gutters">
      <div class="fr-col">
        <h1>{}</h1>
      </div>
      <div class="fr-col-12">
        <div class="fr-highlight">
          <p>{}
          </p>
        </div>
      </div>
      <div class="fr-col-12 fr-col-md-4 not-prose">
      </div>
      <div class="fr-col-12 fr-col-md-8">{}</div>
    </div>
  </div>
</section>
""".format(title, basic_description, left_menu, html_tree)
'''

# <h1 class="fr-h1"> pour surcharger
main_content_template = main_content_template.replace("<h1 ", '<h1 class="fr-h1 fr-mt-4w"').replace('<h1 class="fr-h1 fr-mt-4w"id="toc_1">', '<h1 class="fr-h1" id="toc_1">')
soup = BeautifulSoup(main_content_template, 'html.parser')
main_content_template = r.sub(r'\1\1', soup.prettify())
content_resulting.append(main_content_template)

html = '\n'.join(content_resulting)
with open('donnees-geographiques.html', 'w') as input_file:
    input_file.write(html)
