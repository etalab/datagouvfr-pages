---
title: Données limites administratives
---

# Données limites administratives

## **Données communales**

Le Code Officiel Géographique (COG). C’est une donnée pivot qui permet de rattacher les données à d’autres jeux de données, à des données géographiques ou de faire des calculs à des niveaux administratifs issus d’une combinaison de communes.

- [Code officiel géographique](https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/) avec les données sous forme JSON dans le cadre de <a href="https://github.com/etalab/decoupage-administratif#via-des-urls" target="_blank">l’API Découpage Administratif</a> (**SPD**)

### Données IGN

- [Admin Express](https://www.data.gouv.fr/fr/datasets/admin-express/): données communales à partir de 2017 jusqu’à nos jours. Les versions récentes intègrent les EPCI
- [Geofla](https://www.data.gouv.fr/fr/datasets/geofla-r/): données communales, cantonales et départementales en 1997, 2002 puis régulièrement de 2010 à 2016 régulièrement 

La précision géométrique de ces limites a changé au fil du temps. Lors du passage Geofla vers Admin Express puis avec le passage de Admin Express en version 3. Voir <a href="https://geoservices.ign.fr/admin-express-passe-la-grande-echelle" target="_blank">cet article pour faire la distinction</a>

Ces données font partie du SPD via le RGE (Référentiel à Grande Échelle)

*Il faut noter que les Collectivités d’Outre-Mer (COM) ne sont pas présentes. Si vous voulez une version avec les COM, Etalab produit une version avec Admin Express pour métropole et DOM avec les géométries venant d’OpenStreetMap pour les COM. Voir les <a href="http://etalab-datasets.geo.data.gouv.fr/contours-administratifs/" target="_blank">données générées par Etalab</a> (avec le <a href="https://github.com/etalab/contours-administratifs" target="_blank">dépôt associé pour générer</a>)*

Pour ne pas avoir à gérer les DOM/TOM du fait de l’éloignement, lorsqu'on produit des cartes France entière, il existe une [version de données avec les Contours des communes de France simplifié, avec régions et département d'outre-mer rapprochés](https://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/)

### Données OpenStreetMap

Pour les données communales, celle-ci ont tracées depuis un fond raster communal de la direction générale des Finances publiques (DGFiP) comme cet article <a href="http://prev.openstreetmap.fr/36680-communes" target="_blank">"Achèvement du tracé collaboratif des limites communales françaises dans OpenStreetMap"</a> le retrace.

- [Extractions de OpenStreetMap France](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/) sur [data.gouv.fr](http://data.gouv.fr)

## **Données postales**

- [Base officielle des codes postaux](https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/) de La Poste. Comme la donnée n'est qu'à date courante, il est possible d'avoir <a href="http://files.opendatarchives.fr/datanova.laposte.fr/archives/laposte_hexasmal/" target="_blank">les mêmes données archivées plus anciennes sur OpenDatarchives</a>
- Fond de carte des codes postaux [https://www.data.gouv.fr/fr/datasets/fond-de-carte-des-codes-postaux/](https://www.data.gouv.fr/fr/datasets/fond-de-carte-des-codes-postaux/)

## **Données dérivées ou dérivables des données communales générales**

Généralement des zonages sont dérivés de zonage communaux. Voici une liste ci-dessous. Vous pouvez pour certains zonages passer par la <a href="https://www.insee.fr/fr/information/2028028" target="_blank">"Table d’appartenance géographique des communes et tables de passage" de l'INSEE</a>

- Militaires:
  - [zone de défense et de sécurité](https://www.data.gouv.fr/fr/datasets/zones-de-defense-et-de-securite-2016/)
- Écoles: académie et zones de vacances
    - [Contours géographiques des académies](https://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/)
- Zonages liés à des actions, principalement ANCT (Agence Nationale de Cohésion des Territoires)
    - [Zones de revitalisation rurale (ZRR)](https://www.data.gouv.fr/fr/datasets/zone-de-revitalisation-rurale-zrr-30382904/)
    - [Aides à finalité régionale (AFR)](https://www.data.gouv.fr/fr/datasets/zones-daide-a-finalite-regionale-afr/)
    - [Communes classées en zone de montagne](https://www.data.gouv.fr/fr/datasets/communes-de-la-loi-montagne-au-code-officiel-geographique-cog-2020-2022/)
    - <a href="https://www.observatoire-des-territoires.gouv.fr/kiosque/zonage-les-zones-de-perimetre-de-massifs" target="_blank">Communes classées en Périmètre de massif</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-territoires-dindustrie-0" target="_blank">Programme Territoires d'industrie</a>
    - [Communes bénéficiant du plan Action Cœur de Ville (ACV)](https://www.data.gouv.fr/fr/datasets/programme-action-coeur-de-ville/)
    - <a href="https://www.observatoire-des-territoires.gouv.fr/classement-des-communes-en-loi-littoral" target="_blank">Communes classées en Loi Littoral</a>
    - Communes classées en Périmètres des parcs naturels régionaux (PNR): voir <a href="https://inpn.mnhn.fr/telechargement/cartes-et-information-geographique/ep/pnr" target="_blank">les zonages des PNR</a>
    - Communes classées en Parcs Nationaux: voir <a href="https://inpn.mnhn.fr/telechargement/cartes-et-information-geographique/ep/pn" target="_blank">les zonages des PN</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/classement-des-communes-en-zone-de-revitalisation-des-commerces-en-milieu-rural-zorcomir" target="_blank">zones de revitalisation des commerces en milieu rural (ZORCOMIR)</a>
    - [Zones urbaines sensibles (ZUS)](https://www.data.gouv.fr/fr/datasets/zones-urbaines-sensibles-zus/)
    - Établissements Publics de Coopération Intercommunale (EPCI) Voir [Admin Express](https://www.data.gouv.fr/fr/datasets/admin-express/) pour les données récentes. Pour reconstituer les données EPCI, utiliser les données DGCL qui donnent la <a href="https://www.collectivites-locales.gouv.fr/institutions/liste-et-composition-des-epci-fiscalite-propre" target="_blank">composition communale des EPCI depuis 1999</a> ou bien [la BANATIC (Base nationale sur les intercommunalités)](https://www.data.gouv.fr/fr/datasets/base-nationale-sur-les-intercommunalites/)
    - Établissements publics territoriaux (EPT). Ils composent la Métropole du Grand Paris et sont disponibles sur <a href="https://opendata.apur.org/datasets/Apur::etablissements-publics-territoriaux-metropole-du-grand-paris/explore?location=48.828504%2C2.379750%2C10.99" target="_blank">le portail de l'APUR</a>
    - Pays et Pôles d'Équilibre Territoriaux et Ruraux (PETR). Ils sont renseignés dans [la BANATIC (Base nationale sur les intercommunalités)](https://www.data.gouv.fr/fr/datasets/base-nationale-sur-les-intercommunalites/)
    - Départements: disponibles dans [Admin Express](https://www.data.gouv.fr/fr/datasets/admin-express/)
    - Régions: disponibles dans [Admin Express](https://www.data.gouv.fr/fr/datasets/admin-express/)
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-anciennes-regions-1972" target="_blank">Anciennes Régions</a>
    - <a href="https://www.insee.fr/fr/information/4652957" target="_blank">Zone d'emploi (2020)</a>
    - <a href="https://www.insee.fr/fr/information/2115016" target="_blank">Bassin de vie (2012)</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-pseudo-cantons" target="_blank">Canton-ou-ville (appelé pseudo-canton)</a>
    - Arrondissement: disponibles dans [Admin Express](https://www.data.gouv.fr/fr/datasets/admin-express/)
    - <a href="https://www.insee.fr/fr/information/4802589" target="_blank">Unité urbaine (2020)</a>
    - <a href="https://www.insee.fr/fr/information/4803954" target="_blank">Aire d'attraction des villes (2020)</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/typologie-du-zonage-en-aires-dattraction-des-villes-aav-2020-0" target="_blank">Pôle / couronne des AAV (2020)</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-cours-dappel" target="_blank">Périmètre des cours d'appel</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-tribunaux-judiciaires" target="_blank">Périmètre des tribunaux judiciaires</a>
    - <a href="https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-tribunaux-de-proximite-ou-poles-de-proximite-de-tribunaux-judiciaires" target="_blank">Périmètre des tribunaux de proximité</a>
    - [Programme Petites villes de demain](https://www.data.gouv.fr/fr/datasets/programme-petites-villes-de-demain/)
    - [CRTE (Contrat de Relance et de Transition Ecologique)](https://www.data.gouv.fr/fr/datasets/contrat-de-relance-et-de-transition-ecologique/)
    - [Quartiers prioritaires politique de la ville (QPV)](https://www.data.gouv.fr/fr/datasets/quartiers-prioritaires-de-la-politique-de-la-ville-qpv/)


**Données intracommunales et carroyées haute-résolution**

- IRIS: Il existe deux produits
  - [Contour IRIS](https://www.data.gouv.fr/fr/datasets/contours-iris/) adapté pour représenter sur une carte car simplifiée
  - <a href="https://geoservices.ign.fr/irisge" target="_blank">IRIS GE comme Grande Échelle</a> adapté pour dénombrer dans quel IRIS un habitation est par exemple car la donnée a une plus grande précision
- Bureaux de vote: pas de renseignement national. Au cas par cas, mis à disposition par la commune. Repris dans OpenStreetMap
- Quartiers (cas par cas): soit disponible sur des portails OpenData soit sur OpenStreetMap
- <a href="https://www.insee.fr/fr/statistiques/6215138?sommaire=6215217" target="_blank">Données carroyées 200m</a>

**Données statistiques à associer aux communes ou aux iris (ne contient pas de géographie)**

- <a href="https://www.insee.fr/fr/statistiques/5359146" target="_blank">Base du dossier complet</a> (INSEE, niveau communal, 1900 indicateurs)
- IRIS (source INSEE)
    - <a href="https://www.insee.fr/fr/statistiques/5650708" target="_blank">Activité des résidents en 2018</a>
    - <a href="https://www.insee.fr/fr/statistiques/5650712" target="_blank">Diplômes - Formation en 2018</a>
    - <a href="https://www.insee.fr/fr/statistiques/5650714" target="_blank">Couples - Familles - Ménages en 2018</a>
    - <a href="https://www.insee.fr/fr/statistiques/5650749" target="_blank">Logement en 2018</a>
    - <a href="https://www.insee.fr/fr/statistiques/5650720" target="_blank">Population en 2018</a>
- [1526 variables regroupées en 19 classes sur les 49461 IRIS de France](https://www.data.gouv.fr/fr/datasets/1526-variables-regroupees-en-19-classes-sur-les-49461-iris-de-france/)

# **Transports/mobilités**

- Le Point d'Accès National (PAN) aux données ouvertes de transport <a href="https://transport.data.gouv.fr/" target="_blank">transport.data.gouv.fr</a>. Il concerne tous les types de transports ainsi que certains aspects de mobilité comme le covoiturage.

## Voiture/transport routier

- <a href="https://transport.data.gouv.fr/datasets/base-nationale-des-lieux-de-covoiturage/" target="_blank">Aires de covoiturage en France</a>
- <a href="https://transport.data.gouv.fr/datasets?type=low-emission-zones" target="_blank">Zones à faibles émissions</a>
- [Base Nationale des Lieux de Stationnement](https://www.data.gouv.fr/fr/datasets/base-nationale-des-lieux-de-stationnement/)
- [Bases de données annuelles des accidents corporels de la circulation routière - Années de 2005 à 2020](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/)
- [Accidents de vélo](https://www.data.gouv.fr/fr/datasets/accidents-de-velo/) (dérivée des bases de données annuelles des accidents corporels de la circulation routière ci-dessus)
- [Trafic moyen journalier annuel sur le réseau routier national](https://www.data.gouv.fr/fr/datasets/trafic-moyen-journalier-annuel-sur-le-reseau-routier-national/)
- [ROUTE 500, base de données des principales routes en France](https://www.data.gouv.fr/fr/datasets/route-500/). Initialement, elle était gérée à part. Maintenant, il s’agit d’un produit dérivé de la BD TOPO
- [Paris Respire - Secteurs](https://www.data.gouv.fr/fr/datasets/paris-respire-secteurs/)
- [Prix des carburants en France](https://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france/)
- [Prix des contrôles techniques](https://www.data.gouv.fr/fr/datasets/prix-des-controles-techniques/)
- [Fichier consolidé des Bornes de Recharge pour Véhicules Électriques](https://www.data.gouv.fr/fr/datasets/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/)
- [Radars automatiques](https://www.data.gouv.fr/fr/datasets/radars-automatiques/)
- [Gestionnaires du réseau routier national](https://www.data.gouv.fr/fr/datasets/gestionnaires-du-reseau-routier-national/)
- [Registre public des gares routières et des aménagements routiers](https://www.data.gouv.fr/fr/datasets/registre-public-des-gares-routieres/) Il contient des coordonnées géographiques</a>

## Transport ferroviaire

- [Liste des gares](https://www.data.gouv.fr/fr/datasets/liste-des-gares/)
- [Gares ferroviaires de tous types, exploitées ou non](https://www.data.gouv.fr/fr/datasets/gares-ferroviaires-de-tous-types-exploitees-ou-non/)
- [Positions géographiques des stations du réseau RATP](https://www.data.gouv.fr/fr/datasets/positions-geographiques-des-stations-du-reseau-ratp-ratp/) (voir aussi <a href="https://data.iledefrance-mobilites.fr/explore/dataset/emplacement-des-gares-idf-data-generalisee/" target="_blank">ce jeu de données</a>).

## Transport aérien

- [Aéroports français](https://www.data.gouv.fr/fr/datasets/aeroports-francais-coordonnees-geographiques/)
- [Données d'espace aérien de la base aéronautique du SIA](https://www.data.gouv.fr/fr/datasets/donnees-despace-aerien-de-la-base-aeronautique-du-sia/)

## Mobilité

- <a href="https://www.insee.fr/fr/information/2383370" target="_blank">INSEE Base des flux de mobilité</a>
    - <a href="https://www.insee.fr/fr/information/2383337" target="_blank">Mobilités professionnelles</a> : déplacements domicile-travail
    - <a href="https://www.insee.fr/fr/information/2383343" target="_blank">Mobilités scolaires</a> : déplacements domicile-études
    - <a href="https://www.insee.fr/fr/information/2383331" target="_blank">Migrations résidentielles</a> : commune de résidence / commune de résidence antérieure

# **Annuaires/référentiels**

- [Service-Public.fr](https://www.data.gouv.fr/fr/datasets/service-public-fr-annuaire-de-l-administration-base-de-donnees-locales/)
- [Base Sirene des entreprises et de leurs établissements (SIREN, SIRET)](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) dont versions géolocalisées ci-dessous
    - [Sirene INSEE](https://www.data.gouv.fr/fr/datasets/geolocalisation-des-etablissements-du-repertoire-sirene-pour-les-etudes-statistiques/)
    - <a href="https://data.cquest.org/geo_sirene/v2019/" target="_blank">Sirene géolocalisée (Christian Quest)</a> (dans les ressources communautaires de [ce jeu de données](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/))
- [Base Adresse Nationale (BAN)](https://www.data.gouv.fr/fr/datasets/base-adresse-nationale/) (**SPD**)
- [Adresses extraites du cadastre](https://www.data.gouv.fr/fr/datasets/adresses-extraites-du-cadastre/)
- [Base d'Adresses Nationale Ouverte - BANO](https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/) (en complément de la BAN)
- [Cadastre](https://www.data.gouv.fr/fr/datasets/cadastre/) (**SPD**)
- [COG (Code officiel géographique)](https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/) (**SPD**)
- [Référentiel à grande échelle (RGE)](https://www.data.gouv.fr/fr/datasets/referentiel-a-grande-echelle-rge/) (**SPD**) Le RGE est constitué des composantes orthophotographique, topographique et adresse, parcellaire et altimétrique.
- [Services Publics Plus](https://www.data.gouv.fr/fr/datasets/referentiel-structure-de-la-plateforme-services-publics-plus-de-la-ditp/) (référentiel structure)

# Risques

- [Connaître le potentiel radon de ma commune](https://www.data.gouv.fr/fr/datasets/connaitre-le-potentiel-radon-de-ma-commune/)
- <a href="https://www.georisques.gouv.fr/donnees/bases-de-donnees" target="_blank">Géorisques</a>,
    - <a href="https://www.georisques.gouv.fr/risques/installations/donnees" target="_blank">ICPE</a>
- InfoTerre dont les <a href="https://infoterre.brgm.fr/page/geoservices-ogc" target="_blank">flux OGC</a>
- [Base nationale de Gestion Assistée des Procédures Administratives relatives aux Risques (GASPAR)](https://www.data.gouv.fr/fr/datasets/base-nationale-de-gestion-assistee-des-procedures-administratives-relatives-aux-risques-gaspar/) (attention, CSV à joindre à des informations communales par le code INSEE, pas d’information géographique directe).

# Environnement (géologie, eau, autres)

- [Cartes géologiques départementales à 1/50 000 (BD Charm)](https://www.data.gouv.fr/fr/datasets/cartes-geologiques-departementales-a-1-50-000-bd-charm-50/)
- InfoTerre dont les <a href="https://infoterre.brgm.fr/page/geoservices-ogc" target="_blank">flux OGC</a>
- Vigicrues
    - [Hauteurs d’eau et débits des cours d’eau observés en temps réel aux stations du réseau Vigicrues](https://www.data.gouv.fr/fr/datasets/hauteurs-deau-et-debits-des-cours-deau-observes-en-temps-reel-aux-stations-du-reseau-vigicrues/)
    - [Tronçons de cours d'eau Vigicrues, simplifiés avec niveau de vigilance crues](https://www.data.gouv.fr/fr/datasets/troncons-de-cours-deau-vigicrues-simplifies-avec-niveau-de-vigilance-crues-2/)
- <a href="https://www.sandre.eaufrance.fr/atlas/" target="_blank">Sandre (Service d'administration nationale des données et référentiels sur l'eau)</a>
- <a href="https://hubeau.eaufrance.fr" target="_blank">Hubeau (API)</a>
- <a href="http://www.naiades.eaufrance.fr/acces-donnees" target="_blank">Naiades</a>
- [Corine Land Cover](https://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/)
- [Données d'observation des principales stations météorologiques](https://www.data.gouv.fr/fr/datasets/donnees-d-observation-des-principales-stations-meteorologiques/)
- [Température quotidienne régionale (depuis janvier 2016)](https://www.data.gouv.fr/fr/datasets/temperature-quotidienne-regionale-depuis-janvier-2016/)
- [Données « temps réel » de mesure des concentrations de polluants atmosphériques réglementés](https://www.data.gouv.fr/fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1/)
- [Pesticides dans les eaux souterraines](https://www.data.gouv.fr/fr/datasets/pesticides-dans-les-eaux-souterraines/)
- [Carroyage DFCI](https://www.data.gouv.fr/fr/datasets/carroyage-dfci-2-km/) (Défense des Forêts Contre les Incendies) 2 km

# Urbanisme (cadastre, données vente, logement)

- [Plan cadastral informatisé](https://www.data.gouv.fr/fr/datasets/plan-cadastral-informatise/) (**SPD**)
- [Base de donnée nationale des bâtiments](https://www.data.gouv.fr/fr/datasets/base-de-donnee-nationale-des-batiments-version-0-6/)
- <a href="https://www.geoportail-urbanisme.gouv.fr" target="_blank">Géoportail de l’Urbanisme (PLU et SUP)</a>
- [Liste des PLU disponibles sur le Géoportail de l'Urbanisme](https://www.data.gouv.fr/fr/datasets/liste-des-plu-disponibles-sur-le-geoportail-de-lurbanisme-1/)
- [Demandes de valeurs foncières géolocalisées](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/)
- [DVF+ open-data (version géolocalisée produite par le Cerema)](https://www.data.gouv.fr/fr/datasets/dvf-open-data/)
- ["Carte des loyers" - Indicateurs de loyers d'annonce par commune en 2018](https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2018/)
- [Sitadel](https://www.data.gouv.fr/fr/datasets/base-des-permis-de-construire-et-autres-autorisations-durbanisme-sitadel/)
- [Logements vacants du parc privé par ancienneté de vacance, par commune et par EPCI](https://www.data.gouv.fr/fr/datasets/logements-vacants-du-parc-prive-par-anciennete-de-vacance-par-commune-et-par-epci/)
- [Prix moyen au m² des ventes de maisons et d'appartements par commune en 2017](https://www.data.gouv.fr/fr/datasets/prix-moyen-au-m2-des-ventes-de-maisons-et-dappartements-par-commune-en-2017/)
- [Répertoire des logements locatifs des bailleurs sociaux](https://www.data.gouv.fr/fr/datasets/repertoire-des-logements-locatifs-des-bailleurs-sociaux/) (rapportable à la commune)
- [Annuaire des diagnostiqueurs immobiliers](https://www.data.gouv.fr/fr/datasets/annuaire-des-diagnostiqueurs-immobiliers/) (via géocodage)
- [Zonage des Plan d'Exposition au Bruit](https://www.data.gouv.fr/fr/datasets/zonage-des-plan-dexposition-au-bruit-peb/) (PEB) Voir les <a href="https://geoservices.ign.fr/services-web-experts-transports#2314" target="_blank">services WFS de l’IGN</a> pour une version à jour.
- [Sites référencés dans Cartofriches](https://www.data.gouv.fr/fr/datasets/sites-references-dans-cartofriches/)
- [Corine Land Cover](https://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/)
- [Fiches signalétiques des points géodésiques et des repères de nivellement](https://www.data.gouv.fr/fr/datasets/fiches-signaletiques-des-points-geodesiques-et-des-reperes-de-nivellement/). Voir aussi <a href="https://geoservices.ign.fr/services-web-experts-geodesie#3390" target="_blank">les services de l’IGN</a>.

# Télécommunications (antennes, réseaux)

- [Arcep couverture mobile](https://www.data.gouv.fr/fr/datasets/mon-reseau-mobile/)
- [Données ADSL et fibre](https://www.data.gouv.fr/fr/datasets/ma-connexion-internet/)
- [Déploiement haut et très haut débit fixe](https://www.data.gouv.fr/fr/datasets/le-marche-du-haut-et-tres-haut-debit-fixe-deploiements/)
- <a href="https://data.anfr.fr/anfr/visualisation/information/?id=dd11fac6-4531-4a27-9c8c-a3a9e4ec2107" target="_blank">Données sur les réseaux mobiles</a>
- [Données sur les installations radioélectriques de plus de 5 watts](https://www.data.gouv.fr/fr/datasets/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/)

# Éducation

- Académies
    - [Contours géographiques des académies](https://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/)
- Zones de vacances
- Emplacement écoles
    - [Adresse et géolocalisation des établissements d'enseignement du premier et second degrés](https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/)

# Élections

- [Contours des circonscriptions des législatives](https://www.data.gouv.fr/fr/datasets/countours-des-circonscriptions-des-legislatives-nd/)
- [Carte des circonscriptions législatives françaises (2012+)](https://www.data.gouv.fr/fr/datasets/carte-des-circonscriptions-legislatives-francaises-2012-nd/)
- [Découpage des cantons pour les élections départementales de mars 2015](https://www.data.gouv.fr/fr/datasets/decoupage-des-cantons-pour-les-elections-departementales-de-mars-2015/)
- [Contours détaillés des circonscriptions des législatives](https://www.data.gouv.fr/fr/datasets/contours-detailles-des-circonscriptions-des-legislatives/)
- [Panneaux d'affichage électoral](https://www.data.gouv.fr/fr/datasets/panneaux-daffichage-electoral/)

# Police, sécurité publique, sécurité civile, justice

Dispatcher entre droits/justice et sécurité

- [Opérations coordonnées par les CROSS](https://www.data.gouv.fr/fr/datasets/operations-coordonnees-par-les-cross/) (Centres régionaux opérationnels de surveillance et de sauvetage)
- [Liste et localisation des Secrétariats Généraux pour l'Administration du Ministère de l'Intérieur (SGAMI) en métropole](https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-sgami/)
- [Liste des services de police accueillant du public avec géolocalisation](https://www.data.gouv.fr/fr/datasets/liste-des-services-de-police-accueillant-du-public-avec-geolocalisation/)
- [Liste des unités de gendarmerie accueillant du public, comprenant leur géolocalisation et leurs horaires d'ouverture](https://www.data.gouv.fr/fr/datasets/liste-des-unites-de-gendarmerie-accueillant-du-public-comprenant-leur-geolocalisation-et-leurs-horaires-douverture/)
- [Compétence territoriale gendarmerie et police nationales](https://www.data.gouv.fr/fr/datasets/competence-territoriale-gendarmerie-et-police-nationales/)
- [Découpage des zones de sécurité prioritaires (ZSP)](https://www.data.gouv.fr/fr/datasets/decoupage-des-zones-de-securite-prioritaires-zsp-1/)
- [Base de données des barreaux d'avocats de France](https://www.data.gouv.fr/fr/datasets/base-de-donnees-des-barreaux-davocats-de-france/)

# Santé

- [Don du sang](https://www.data.gouv.fr/fr/datasets/dates-et-lieux-des-collectes-de-don-du-sang/)
- [FINESS Extraction du Fichier des établissements](https://www.data.gouv.fr/fr/datasets/finess-extraction-du-fichier-des-etablissements/)
- [Lieux de vaccination Covid-19 (pharmacies)](https://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-covid-19-pharmacies-sante-fr/)
- [Lieux de vaccination contre la Covid-19](https://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-contre-la-covid-19/)
- [Géo'DAE - Base Nationale des Défibrillateurs](https://www.data.gouv.fr/fr/datasets/geodae-base-nationale-des-defibrillateurs/)
- [Résultats des contrôles officiels sanitaires : dispositif d'information « Alim’confiance »](https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/) (API sans archivage). Voir [ce jeu de données](https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/#resource-6c6484fe-7024-452a-a156-b2effbaad598-title) pour une version avec historique et coordonnées.

# Agriculture

- [Registre parcellaire graphique (RPG)](https://www.data.gouv.fr/fr/datasets/registre-parcellaire-graphique-rpg-contours-des-parcelles-et-ilots-culturaux-et-leur-groupe-de-cultures-majoritaire/) : contours des parcelles et îlots culturaux et leur groupe de cultures majoritaire (**SPD**)
- [Parcelles en Agriculture Biologique (AB) déclarées à la PAC](https://www.data.gouv.fr/fr/datasets/parcelles-en-agriculture-biologique-ab-declarees-a-la-pac/)
- [Agriculture biologique 2008-2011 - nombre d'opérateurs engagés en agriculture biologique](https://www.data.gouv.fr/fr/datasets/agriculture-biologique-2008-2011-nombre-d-operateurs-engages-en-agriculture-biologique-30378896/) (information rapportable à une région ou un département)
- [Délimitation Parcellaire des AOC Viticoles de l'INAO](https://www.data.gouv.fr/fr/datasets/delimitation-parcellaire-des-aoc-viticoles-de-linao/)

# Patrimoine/culture/tourisme/sports

- [Immeubles protégés au titre des Monuments Historiques](https://www.data.gouv.fr/fr/datasets/immeubles-proteges-au-titre-des-monuments-historiques-2/)
- [Liste et localisation des Musées de France](https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/)
- [Liste des objets mobiliers propriété publique classés au titre des Monuments Historiques](https://www.data.gouv.fr/fr/datasets/liste-des-objets-mobiliers-propriete-publique-classes-au-titre-des-monuments-historiques/)  (information rapportable à la commune via le code INSEE)
- [Fréquentation des musées de France](https://www.data.gouv.fr/fr/datasets/frequentation-des-musees-de-france/) (à lier géographiquement avec <a href="https://data.culture.gouv.fr/explore/dataset/liste-et-localisation-des-musees-de-france/information/" target="_blank">ce jeu de données</a>)
- [Liste des festivals en France](https://www.data.gouv.fr/fr/datasets/liste-des-festivals-en-france/)
- [DATAtourisme, la base nationale des données du tourisme en Open Data](https://www.data.gouv.fr/fr/datasets/datatourisme-la-base-nationale-des-donnees-du-tourisme-en-open-data/)
- [Données touristiques de la base DATAtourisme](https://www.data.gouv.fr/fr/datasets/donnees-touristiques-de-la-base-datatourisme/)
- [Zones Touristiques Internationales](https://www.data.gouv.fr/fr/datasets/zones-touristiques-internationales/)
- [Localisation des sites de fouille archéologiques de l'Inrap](https://www.data.gouv.fr/fr/datasets/localisation-des-sites-de-fouille-archeologiques-de-l-inrap-576210/)
- [Données géocodées issues du recensement des licences et clubs auprès des fédérations sportives agréées par le ministère chargé des sports](https://www.data.gouv.fr/fr/datasets/donnees-geocodees-issues-du-recensement-des-licences-et-clubs-aupres-des-federations-sportives-agreees-par-le-ministere-charge-des-sports/)
- [Base des lieux et équipements culturels (Basilic)](https://www.data.gouv.fr/fr/datasets/base-des-lieux-et-equipements-culturels-basilic/)

# POIs

- [Recensement des équipements sportifs, espaces et sites de pratiques](https://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/) (soit à géocoder soit pour avoir les informations à la commune)
- [Base permanente des équipements](https://www.data.gouv.fr/fr/datasets/base-permanente-des-equipements-1/)
- [Liste des boîtes aux lettres de rue France métropolitaine et DOM avec heure limite de dépôt](https://www.data.gouv.fr/fr/datasets/liste-des-boites-aux-lettres-de-rue-france-metropolitaine-et-dom-avec-heure-limite-de-depot-1/)
- [Adresses des débits de tabac](https://www.data.gouv.fr/fr/datasets/adresses-des-debits-de-tabac/)
- [Liste des structures France services](https://www.data.gouv.fr/fr/datasets/62503e25bc0f6370f4a651ce/)

# Fonds de plan

## Niveau France

- [Données OpenStreetMap intégrales de France Métropolitaine](https://www.data.gouv.fr/fr/datasets/donnees-openstreetmap-integrales-de-france-metropolitaine/)
- [Fonds de carte IGN France et régions](https://www.data.gouv.fr/fr/datasets/fonds-de-carte-ign-france-et-regions-571459/) (rare cas où la donnée est en fait des PDF à réutiliser sous forme papier)
- [BD TOPO®](https://www.data.gouv.fr/fr/datasets/bd-topo-r/) (description vectorielle 3D des éléments du territoire et de ses infrastructures)
- [BD ORTHO®](https://www.data.gouv.fr/fr/datasets/bd-ortho-r/) (images aériennes raster)
- [Métadonnée des photos aériennes anciennes de l'IGN](https://www.data.gouv.fr/fr/datasets/metadonnee-des-photos-aeriennes-anciennes-de-lign/)

## Niveau Europe

- [EuroGlobalMap - données topographiques au 1/1 000 000 couvrant 45 pays et territoires en Europe](https://www.data.gouv.fr/fr/datasets/euroglobalmap-donnees-topographiques-au-1-1-000-000-couvrant-45-pays-et-territoires-en-europe/)

## Niveau Monde

- [COPERNICUS - Satellite Sentinel 1A](https://www.data.gouv.fr/fr/datasets/copernicus-satellite-sentinel-1a/)

## Données Monde génériques (hors [data.gouv.fr](http://data.gouv.fr/))

- <a href="https://www.naturalearthdata.com/downloads/" target="_blank">Natural Earth Data</a>(pays, principales villes, rivières, lacs, fond de plan raster altimétrie/bathymétrie)
- <a href="https://www.gebco.net/data_and_products/gridded_bathymetry_data/" target="_blank">Données bathymétriques</a>
- <a href="https://registry.opendata.aws/speedtest-global-performance/" target="_blank">Speedtest by Ookla Global Fixed and Mobile Network Performance Maps</a>
