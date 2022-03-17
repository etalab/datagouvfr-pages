<h4> Vous avez une question sur une procédure administrative ? </h4>
<p>Notre support n'est pas en mesure de vous aider sur ces sujets.
Vous pouvez vous référer au site <a href="https://doc.data.gouv.fr/" target="_blank"> Service-Public.fr</a>.</p>

<h4> Vous avez une question sur un jeu de données en particulier ? </h4>
<p>Notre équipe n'est pas en charge de la production des données publiées sur la plateforme.<br/>
Adressez vous directement au producteur dans l'espace de discussion en bas de page du jeu de donnée.
<a href="https://www.data.gouv.fr/fr/datasets/fichier-des-personnes-decedees/#discussion-604e44bcf9fac775bbc0aeca" target="_blank"> Voir un exemple </a>.</p>

<p><strong> Questions les plus fréquentes : </p></strong>
<ul class="fr-accordions-group">
   <li>
       <section class="fr-accordion">
           <h3 class="fr-accordion__title">
               <button class="fr-accordion__btn" aria-expanded="false" aria-controls="accordion-1">Vous avez une question sur la base SIRENE ?</button>
           </h3>
           <div class="fr-collapse" id="accordion-1">
               <br/>
               <p>Si vous rechercher votre numéro SIRET ou SIREN vous pouvez vous rendre sur le site <a href="https://annuaire-entreprises.data.gouv.fr/" target="_blank"> Annuaire des Entreprises</a>.
               <br/>Si vous souhaitez rendre privées les données de votre entreprise,
                vous devez en <a href="https://statut-diffusion-sirene.insee.fr/" target="_blank"> faire la demande auprès de l'INSEE </a> qui publie ces données dans le répertoire SIRENE.</p>
           </div>
       </section>
   </li>

   <div class="fr-col-12 fr-col-md-3">
  <div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
      <h2 class="fr-card__title">
        <a class="fr-card__link" href="{{ startup.url }}" >{{ startup.title | strip_html }}</a>
      </h2>
      {%- if startup.sponsors -%}
      <p class="fr-card__detail" style="z-index: 10;position: relative;">
      {%- for sponsorId in startup.sponsors -%}
        {% assign sponsor = site.organisations | where: 'id', sponsorId | first %}
        {% if forloop.index > 1 %} / {% endif %}<abbr title="{{sponsor.name}}">{{sponsor.acronym}}</abbr>
      {%- endfor -%}
      </p>
      {%- endif -%}
      <p class="fr-card__desc">{{ startup.mission | strip_html }}</p>
    </div>
    <div class="fr-card__img">
      {% include screenshot.html startup=startup force=true %}
    </div>
  </div>
</div>
