# Données à composantes géographiques

Les données à composantes géographiques sont souvent indispensables pour réaliser des analyses. Sont référencées ici les principaux jeux de données disponibles sur [data.gouv.fr](http://data.gouv.fr/). Celle-ci n'est pas exhaustive et est [ouverte aux contributions](https://github.com/etalab/datagouvfr-pages/blob/master/pages/donnees-coronavirus.md).

Lien vers https://guides.etalab.gouv.fr/qualite/lier-les-donnees-a-un-referentiel/
pour parler du SPD

# Données limites administratives

## **Données communales** :

Le Code Officiel Géographique (COG). C’est une donnée pivot qui permet de rattacher les données à d’autres jeux de données, à des données géographiques ou de faire des calculs à des niveaux administratifs issus d’une combinaison de communes.

- [Code officiel géographique](https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/) avec les données sous forme JSON dans le cadre de l’API Découpage Administratif [https://github.com/etalab/decoupage-administratif#via-des-urls](https://github.com/etalab/decoupage-administratif#via-des-urls) (**SPD**)

### ***Données IGN***

- Admin Express: données communales à partir de 2017 jusqu’à nos jours [https://www.data.gouv.fr/fr/datasets/admin-express/](https://www.data.gouv.fr/fr/datasets/admin-express/) Les versions récentes intègrent les EPCI
- Geofla: données communales, cantonales et départementales en 1997, 2002 puis régulièrement de 2010 à 2016 régulièrement [http://www.data.gouv.fr/fr/datasets/geofla-r/](http://www.data.gouv.fr/fr/datasets/geofla-r/)

La précision géométrique de ces limites a changé au fil du temps. Lors du passage Geofla vers Admin Express puis avec le passage de Admin Express en version 3 [https://geoservices.ign.fr/admin-express-passe-la-grande-echelle](https://geoservices.ign.fr/admin-express-passe-la-grande-echelle)

Ces données font partie du SPD via le RGE (Référentiel à Grande Échelle)

*Il faut noter que les Collectivités d’Outre-Mer (COM) ne sont pas présentes. Si vous voulez une version avec les COM, Etalab produit une version avec AdminExpress pour métropole et DOM avec les géométries venant d’OpenStreetMap pour les COM. Voir les données générées [http://etalab-datasets.geo.data.gouv.fr/contours-administratifs/](http://etalab-datasets.geo.data.gouv.fr/contours-administratifs/) (le dépôt associé pour générer [https://github.com/etalab/contours-administratifs](https://github.com/etalab/contours-administratifs))*

Pour ne pas avoir à gérer les DOM/TOM du fait de l’éloignement, une version de données avec les Contours des communes de France simplifié, avec régions et département d'outre-mer rapprochés [http://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/](http://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-doutre-mer-rapproches/)

### ***Données OpenStreetMap***

Données communales tracées depuis un fond raster communal de la direction générale des Finances publiques (DGFiP)
[http://prev.openstreetmap.fr/36680-communes](http://prev.openstreetmap.fr/36680-communes)

- Extraction de OpenStreetMap France sur [data.gouv.fr](http://data.gouv.fr) [https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/)

## **Données postales**

Base officielle des codes postaux [https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/](https://www.data.gouv.fr/fr/datasets/base-officielle-des-codes-postaux/)

Fond de carte des codes postaux [http://www.data.gouv.fr/fr/datasets/fond-de-carte-des-codes-postaux/](http://www.data.gouv.fr/fr/datasets/fond-de-carte-des-codes-postaux/)

### **Dérivées ou dérivables des données communales générales :**

Généralement des zonages sont dérivés de zonage communaux

- Militaires: Zone de défense et de sécurité
- Écoles: académie et zone vacances
    - Contours géographiques des académies [http://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/](http://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/)
- Zonages liés à des actions, principalement ANCT (Agence Nationale de Cohésion des Territoires)
    - Zones de revitalisation rurale (ZRR) [http://www.data.gouv.fr/fr/datasets/zone-de-revitalisation-rurale-zrr-30382904/](http://www.data.gouv.fr/fr/datasets/zone-de-revitalisation-rurale-zrr-30382904/)
    - Aides à finalité régionale (AFR) (en cours de validation pour la période)
    - [Communes classées en zone de montagne](https://www.data.gouv.fr/fr/datasets/communes-de-la-loi-montagne-au-code-officiel-geographique-cog-2020-2022/)
    - [Communes classées en Périmètre de massif](https://www.observatoire-des-territoires.gouv.fr/kiosque/zonage-les-zones-de-perimetre-de-massifs)
    - [Programme Territoires d'industrie](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-territoires-dindustrie-0)
    - [communes bénéficiant du plan Action Cœur de Ville (ACV)](http://www.data.gouv.fr/fr/datasets/programme-action-coeur-de-ville/)
    - [communes classées en Loi Littoral](https://www.observatoire-des-territoires.gouv.fr/classement-des-communes-en-loi-littoral)
    - communes classées en Périmètres des parcs naturels régionaux (PNR): voir [les zonages des PNR](https://inpn.mnhn.fr/telechargement/cartes-et-information-geographique/ep/pnr)
    - communes classées en Parcs Nationaux: voir [les zonages des PN](https://inpn.mnhn.fr/telechargement/cartes-et-information-geographique/ep/pn)
    - [zones de revitalisation des commerces en milieu rural (*ZORCOMIR)*](https://www.observatoire-des-territoires.gouv.fr/classement-des-communes-en-zone-de-revitalisation-des-commerces-en-milieu-rural-zorcomir)
    - [Zones urbaines sensibles (ZUS)](http://www.data.gouv.fr/fr/datasets/zones-urbaines-sensibles-zus/)
    - Établissements Publics de Coopération Intercommunale (EPCI) Voir AdminExpress pour les données récentes. Pour reconstituer les données EPCI, utiliser les données DGCL qui donnent la [composition communale des EPCI depuis 1999](https://www.collectivites-locales.gouv.fr/institutions/liste-et-composition-des-epci-fiscalite-propre) ou bien [la BANATIC (Base nationale sur les intercommunalités)](https://www.data.gouv.fr/fr/datasets/base-nationale-sur-les-intercommunalites/)
    - Établissements publics territoriaux (EPT). Ils composent la Métropole du Grand Paris et sont disponibles sur [le portail de l'APUR](https://opendata.apur.org/datasets/Apur::etablissements-publics-territoriaux-metropole-du-grand-paris/explore?location=48.828504%2C2.379750%2C10.99)
    - Pays et Pôles d'Équilibre Territoriaux et Ruraux (PETR). Ils sont renseignés dans [la BANATIC (Base nationale sur les intercommunalités)](https://www.data.gouv.fr/fr/datasets/base-nationale-sur-les-intercommunalites/)
    - Départements: disponibles dans Admin Express
    - Régions: disponibles dans Admin Express
    - [Anciennes Régions](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-anciennes-regions-1972)
    - [Zone d'emploi (2020)](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-zones-demploi-2020)
    - [Bassin de vie (2012)](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-bassins-de-vie-2012)
    - [Canton-ou-ville (appelé pseudo-canton)](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-pseudo-cantons)
    - Arrondissement: disponibles dans Admin Express
    - [Unité urbaine (2020)](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-unites-urbaines-2020)
    - [Aire d'attraction des villes (2020)](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-aires-dattraction-des-villes-2020)
    - [Pôle / couronne des AAV (2020)](https://www.observatoire-des-territoires.gouv.fr/typologie-du-zonage-en-aires-dattraction-des-villes-aav-2020-0)
    - [Périmètre des cours d'appel](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-cours-dappel)
    - [Périmètre des tribunaux judiciaires](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-tribunaux-judiciaires)
    - [Périmètre des tribunaux de proximité](https://www.observatoire-des-territoires.gouv.fr/perimetre-des-ressorts-des-tribunaux-de-proximite-ou-poles-de-proximite-de-tribunaux-judiciaires)
    - [Programme Petites villes de demain](http://www.data.gouv.fr/fr/datasets/programme-petites-villes-de-demain/)
    - [CRTE](https://www.data.gouv.fr/fr/datasets/contrat-de-relance-et-de-transition-ecologique/)
    - [Quartiers prioritaires politique de la ville (QPV)](http://www.data.gouv.fr/fr/datasets/quartiers-prioritaires-de-la-politique-de-la-ville-qpv/)


**Données intracommunales et carroyées haute-résolution**

- IRIS: Il existe deux produits
  - [Contour IRIS](https://www.data.gouv.fr/fr/datasets/contours-iris/) adapté pour représenter sur une carte car simplifiée
  - [IRIS GE comme Grande Échelle](https://geoservices.ign.fr/irisge) adapté pour dénombrer dans quel IRIS un habitation est par exemple car la donnée a une plus grande précision
- Bureaux de vote: pas de renseignement national. Au cas par cas, mis à disposition par la commune. Repris dans OpenStreetMap
- Quartiers (cas par cas): soit disponible sur des portails OpenData soit sur OpenStreetMap
- Données carroyées 200m [https://www.insee.fr/fr/statistiques/6215138?sommaire=6215217](https://www.insee.fr/fr/statistiques/6215138?sommaire=6215217)

**Données statistiques à associer aux communes ou aux iris (ne contient pas de géographie)**

- Base du dossier complet [https://www.insee.fr/fr/statistiques/5359146](https://www.insee.fr/fr/statistiques/5359146) (INSEE, niveau communal, 1900 indicateurs)
- IRIS (source INSEE)
    - Activité des résidents en 2018 [https://www.insee.fr/fr/statistiques/5650708](https://www.insee.fr/fr/statistiques/5650708)
    - Diplômes - Formation en 2018 [https://www.insee.fr/fr/statistiques/5650712](https://www.insee.fr/fr/statistiques/5650712)
    - Couples - Familles - Ménages en 2018 [https://www.insee.fr/fr/statistiques/5650714](https://www.insee.fr/fr/statistiques/5650714)
    - Logement en 2018 [https://www.insee.fr/fr/statistiques/5650749](https://www.insee.fr/fr/statistiques/5650749)
    - Population en 2018 [https://www.insee.fr/fr/statistiques/5650720](https://www.insee.fr/fr/statistiques/5650720)
- 1526 variables regroupées en 19 classes sur les 49461 IRIS de France [https://www.data.gouv.fr/fr/datasets/1526-variables-regroupees-en-19-classes-sur-les-49461-iris-de-france/](https://www.data.gouv.fr/fr/datasets/1526-variables-regroupees-en-19-classes-sur-les-49461-iris-de-france/)

# **Transports/mobilités**

- Le Point d'Accès National (PAN) aux données ouvertes de transport [https://transport.data.gouv.fr](https://transport.data.gouv.fr/). Il concerne tous les types de transports ainsi que certains aspects de mobilité comme le covoiturage.

## Voiture

- Aires de covoiturage en France [https://transport.data.gouv.fr/datasets/base-nationale-des-lieux-de-covoiturage/](https://transport.data.gouv.fr/datasets/base-nationale-des-lieux-de-covoiturage/)
- Zones à faibles émissions [https://transport.data.gouv.fr/datasets?type=low-emission-zones](https://transport.data.gouv.fr/datasets?type=low-emission-zones)
- Base Nationale des Lieux de Stationnement [https://www.data.gouv.fr/fr/datasets/base-nationale-des-lieux-de-stationnement/](https://www.data.gouv.fr/fr/datasets/base-nationale-des-lieux-de-stationnement/)
- Bases de données annuelles des accidents corporels de la circulation routière - Années de 2005 à 2020 [http://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/](http://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/)
- Accidents de vélo [https://www.data.gouv.fr/fr/datasets/accidents-de-velo/](https://www.data.gouv.fr/fr/datasets/accidents-de-velo/) (dérivée des bases de données annuelles des accidents corporels de la circulation routière ci-dessus)
- Trafic moyen journalier annuel sur le réseau routier national [https://www.data.gouv.fr/fr/datasets/trafic-moyen-journalier-annuel-sur-le-reseau-routier-national/](https://www.data.gouv.fr/fr/datasets/trafic-moyen-journalier-annuel-sur-le-reseau-routier-national/)
- ROUTE 500, base de données des principales routes en France [http://www.data.gouv.fr/fr/datasets/route-500/](http://www.data.gouv.fr/fr/datasets/route-500/) Initialement, elle était gérée à part. Maintenant, il s’agit d’un produit dérivé de la BD TOPO
- Paris Respire - Secteurs [http://www.data.gouv.fr/fr/datasets/paris-respire-secteurs/](http://www.data.gouv.fr/fr/datasets/paris-respire-secteurs/)
- Prix des carburants en France [http://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france/](http://www.data.gouv.fr/fr/datasets/prix-des-carburants-en-france/)
- Prix des contrôles techniques [https://www.data.gouv.fr/fr/datasets/prix-des-controles-techniques/](https://www.data.gouv.fr/fr/datasets/prix-des-controles-techniques/)
- Fichier consolidé des Bornes de Recharge pour Véhicules Électriques [http://www.data.gouv.fr/fr/datasets/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/](http://www.data.gouv.fr/fr/datasets/fichier-consolide-des-bornes-de-recharge-pour-vehicules-electriques/)
- Radars automatiques [http://www.data.gouv.fr/fr/datasets/radars-automatiques/](http://www.data.gouv.fr/fr/datasets/radars-automatiques/)

## Transport ferroviaire

- Liste des gares [https://www.data.gouv.fr/fr/datasets/liste-des-gares/](https://www.data.gouv.fr/fr/datasets/liste-des-gares/)
- Gares ferroviaires de tous types, exploitées ou non [http://www.data.gouv.fr/fr/datasets/gares-ferroviaires-de-tous-types-exploitees-ou-non/](http://www.data.gouv.fr/fr/datasets/gares-ferroviaires-de-tous-types-exploitees-ou-non/)
- Positions géographiques des stations du réseau RATP [http://www.data.gouv.fr/fr/datasets/positions-geographiques-des-stations-du-reseau-ratp-ratp/](http://www.data.gouv.fr/fr/datasets/positions-geographiques-des-stations-du-reseau-ratp-ratp/) (voir aussi [https://data.iledefrance-mobilites.fr/explore/dataset/emplacement-des-gares-idf-data-generalisee/](https://data.iledefrance-mobilites.fr/explore/dataset/emplacement-des-gares-idf-data-generalisee/))

## Transport aérien

- Aéroports français [http://www.data.gouv.fr/fr/datasets/aeroports-francais-coordonnees-geographiques/](http://www.data.gouv.fr/fr/datasets/aeroports-francais-coordonnees-geographiques/)
- Données d'espace aérien de la base aéronautique du SIA [https://www.data.gouv.fr/fr/datasets/donnees-despace-aerien-de-la-base-aeronautique-du-sia/](https://www.data.gouv.fr/fr/datasets/donnees-despace-aerien-de-la-base-aeronautique-du-sia/)

## Mobilité

- INSEE Base des flux de mobilité [https://www.insee.fr/fr/information/2383370](https://www.insee.fr/fr/information/2383370)
    - [Mobilités professionnelles](https://www.insee.fr/fr/information/2383337) : déplacements domicile-travail
    - [Mobilités scolaires](https://www.insee.fr/fr/information/2383343) : déplacements domicile-études
    - [Migrations résidentielles](https://www.insee.fr/fr/information/2383331) : commune de résidence / commune de résidence antérieure

# **Annuaires/référentiels**

- Service-Public.fr [http://www.data.gouv.fr/fr/datasets/service-public-fr-annuaire-de-l-administration-base-de-donnees-locales/](http://www.data.gouv.fr/fr/datasets/service-public-fr-annuaire-de-l-administration-base-de-donnees-locales/)
- Base Sirene des entreprises et de leurs établissements (SIREN, SIRET) [http://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/](http://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/) dont versions géolocalisées ci-dessous
    - Sirene INSEE [https://www.data.gouv.fr/fr/datasets/geolocalisation-des-etablissements-du-repertoire-sirene-pour-les-etudes-statistiques/](https://www.data.gouv.fr/fr/datasets/geolocalisation-des-etablissements-du-repertoire-sirene-pour-les-etudes-statistiques/)
    - Sirene géolocalisée (Christian Quest) [https://data.cquest.org/geo_sirene/v2019/](https://data.cquest.org/geo_sirene/v2019/) (dans les ressources communautaires de [https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/](https://www.data.gouv.fr/fr/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/))
- Base Adresse Nationale (BAN) [http://www.data.gouv.fr/fr/datasets/base-adresse-nationale/](http://www.data.gouv.fr/fr/datasets/base-adresse-nationale/) (**SPD**)
- Adresses extraites du cadastre [http://www.data.gouv.fr/fr/datasets/adresses-extraites-du-cadastre/](http://www.data.gouv.fr/fr/datasets/adresses-extraites-du-cadastre/)
- Base d'Adresses Nationale Ouverte - BANO [http://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/](http://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/) (en complément de la BAN)
- Cadastre [http://www.data.gouv.fr/fr/datasets/cadastre/](http://www.data.gouv.fr/fr/datasets/cadastre/) (**SPD**)
- COG (Code officiel géographique) [https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/](https://www.data.gouv.fr/fr/datasets/code-officiel-geographique-cog/) (**SPD**)
- Référentiel à grande échelle (RGE) [http://www.data.gouv.fr/fr/datasets/referentiel-a-grande-echelle-rge/](http://www.data.gouv.fr/fr/datasets/referentiel-a-grande-echelle-rge/) (**SPD**) Le RGE est constitué des composantes orthophotographique, topographique et adresse, parcellaire et altimétrique.
- Services Publics Plus (référentiel structure) [https://www.data.gouv.fr/fr/datasets/referentiel-structure-de-la-plateforme-services-publics-plus-de-la-ditp/](https://www.data.gouv.fr/fr/datasets/referentiel-structure-de-la-plateforme-services-publics-plus-de-la-ditp/)

# Risques

- Connaître le potentiel radon de ma commune [http://www.data.gouv.fr/fr/datasets/connaitre-le-potentiel-radon-de-ma-commune/](http://www.data.gouv.fr/fr/datasets/connaitre-le-potentiel-radon-de-ma-commune/)
- Géorisques, en particulier [https://www.georisques.gouv.fr/donnees/bases-de-donnees](https://www.georisques.gouv.fr/donnees/bases-de-donnees) dont API
    - ICPE [https://www.georisques.gouv.fr/risques/installations/donnees](https://www.georisques.gouv.fr/risques/installations/donnees?page=1) (data.gouv.fr héberge cette donnée communautaire [https://www.data.gouv.fr/fr/datasets/base-des-installations-classees-icpe/](https://www.data.gouv.fr/fr/datasets/base-des-installations-classees-icpe/) obsolète)
- InfoTerre dont les flux OGC [https://infoterre.brgm.fr/page/geoservices-ogc](https://infoterre.brgm.fr/page/geoservices-ogc)
- Base nationale de Gestion ASsistée des Procédures Administratives relatives aux Risques (GASPAR) [https://www.data.gouv.fr/fr/datasets/base-nationale-de-gestion-assistee-des-procedures-administratives-relatives-aux-risques-gaspar/](https://www.data.gouv.fr/fr/datasets/base-nationale-de-gestion-assistee-des-procedures-administratives-relatives-aux-risques-gaspar/) (attention, CSV à joindre à des informations communales par le code INSEE, pas d’information géographique directe)

# Environnement (géologie, eau, autres)

- InfoTerre dont les flux OGC [https://infoterre.brgm.fr/page/geoservices-ogc](https://infoterre.brgm.fr/page/geoservices-ogc)
- Vigicrues
    - Hauteurs d’eau et débits des cours d’eau observés en temps réel aux stations du réseau Vigicrues [http://www.data.gouv.fr/fr/datasets/hauteurs-deau-et-debits-des-cours-deau-observes-en-temps-reel-aux-stations-du-reseau-vigicrues/](http://www.data.gouv.fr/fr/datasets/hauteurs-deau-et-debits-des-cours-deau-observes-en-temps-reel-aux-stations-du-reseau-vigicrues/)
    - Tronçons de cours d'eau Vigicrues, simplifiés avec niveau de vigilance crues [http://www.data.gouv.fr/fr/datasets/troncons-de-cours-deau-vigicrues-simplifies-avec-niveau-de-vigilance-crues-2/](http://www.data.gouv.fr/fr/datasets/troncons-de-cours-deau-vigicrues-simplifies-avec-niveau-de-vigilance-crues-2/)
- Sandre (Service d'administration nationale des données et référentiels sur l'eau) [https://www.sandre.eaufrance.fr/atlas/](https://www.sandre.eaufrance.fr/atlas/)
- Hubeau (API) [https://hubeau.eaufrance.fr](https://hubeau.eaufrance.fr/)
- Naiades [http://www.naiades.eaufrance.fr/acces-donnees](http://www.naiades.eaufrance.fr/acces-donnees)
- Corine Land Cover [http://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/](http://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/)
- Données d'observation des principales stations météorologiques [http://www.data.gouv.fr/fr/datasets/donnees-d-observation-des-principales-stations-meteorologiques/](http://www.data.gouv.fr/fr/datasets/donnees-d-observation-des-principales-stations-meteorologiques/)
- Température quotidienne régionale (depuis janvier 2016) [http://www.data.gouv.fr/fr/datasets/temperature-quotidienne-regionale-depuis-janvier-2016/](http://www.data.gouv.fr/fr/datasets/temperature-quotidienne-regionale-depuis-janvier-2016/)
- Données « temps réel » de mesure des concentrations de polluants atmosphériques réglementés [http://www.data.gouv.fr/fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1/](http://www.data.gouv.fr/fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1/)
- Pesticides dans les eaux souterraines [http://www.data.gouv.fr/fr/datasets/pesticides-dans-les-eaux-souterraines/](http://www.data.gouv.fr/fr/datasets/pesticides-dans-les-eaux-souterraines/)
- Carroyage DFCI (Défense des Forêts Contre les Incendies) 2 km [http://www.data.gouv.fr/fr/datasets/carroyage-dfci-2-km/](http://www.data.gouv.fr/fr/datasets/carroyage-dfci-2-km/)
- **TODO: rajouter BD Charm**

# Urbanisme (cadastre, données vente,  logement)

- Plan cadastral informatisé [http://www.data.gouv.fr/fr/datasets/plan-cadastral-informatise/](http://www.data.gouv.fr/fr/datasets/plan-cadastral-informatise/) (**SPD**)
- Base de donnée nationale des bâtiments [https://www.data.gouv.fr/fr/datasets/base-de-donnee-nationale-des-batiments-version-0-6/](https://www.data.gouv.fr/fr/datasets/base-de-donnee-nationale-des-batiments-version-0-6/)
- Géoportail de l’Urbanisme (PLU et SUP) [https://www.geoportail-urbanisme.gouv.fr](https://www.geoportail-urbanisme.gouv.fr/)
- Liste des PLU disponibles sur le Géoportail de l'Urbanisme [http://www.data.gouv.fr/fr/datasets/liste-des-plu-disponibles-sur-le-geoportail-de-lurbanisme-1/](http://www.data.gouv.fr/fr/datasets/liste-des-plu-disponibles-sur-le-geoportail-de-lurbanisme-1/)
- Demandes de valeurs foncières géolocalisées [http://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/](http://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres-geolocalisees/)
- DVF+ open-data (version géolocalisée produite par le Cerema) [https://www.data.gouv.fr/fr/datasets/dvf-open-data/](https://www.data.gouv.fr/fr/datasets/dvf-open-data/)
- "Carte des loyers" - Indicateurs de loyers d'annonce par commune en 2018 [https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2018/](https://www.data.gouv.fr/fr/datasets/carte-des-loyers-indicateurs-de-loyers-dannonce-par-commune-en-2018/)
- Sitadel [http://www.data.gouv.fr/fr/datasets/base-des-permis-de-construire-et-autres-autorisations-durbanisme-sitadel/](http://www.data.gouv.fr/fr/datasets/base-des-permis-de-construire-et-autres-autorisations-durbanisme-sitadel/)
- Logements vacants du parc privé par ancienneté de vacance, par commune et par EPCI    [http://www.data.gouv.fr/fr/datasets/logements-vacants-du-parc-prive-par-anciennete-de-vacance-par-commune-et-par-epci/](http://www.data.gouv.fr/fr/datasets/logements-vacants-du-parc-prive-par-anciennete-de-vacance-par-commune-et-par-epci/)
- Prix moyen au m² des ventes de maisons et d'appartements par commune en 2017 [http://www.data.gouv.fr/fr/datasets/prix-moyen-au-m2-des-ventes-de-maisons-et-dappartements-par-commune-en-2017/](http://www.data.gouv.fr/fr/datasets/prix-moyen-au-m2-des-ventes-de-maisons-et-dappartements-par-commune-en-2017/)
- Répertoire des logements locatifs des bailleurs sociaux [http://www.data.gouv.fr/fr/datasets/repertoire-des-logements-locatifs-des-bailleurs-sociaux/](http://www.data.gouv.fr/fr/datasets/repertoire-des-logements-locatifs-des-bailleurs-sociaux/) (rapportable à la commune)
- Annuaire des diagnostiqueurs immobiliers [http://www.data.gouv.fr/fr/datasets/annuaire-des-diagnostiqueurs-immobiliers/](http://www.data.gouv.fr/fr/datasets/annuaire-des-diagnostiqueurs-immobiliers/) (via géocodage)
- Zonage des Plan d'Exposition au Bruit (PEB) [http://www.data.gouv.fr/fr/datasets/zonage-des-plan-dexposition-au-bruit-peb/](http://www.data.gouv.fr/fr/datasets/zonage-des-plan-dexposition-au-bruit-peb/) Voir les services WFS de l’IGN pour une version à jour sur [https://geoservices.ign.fr/services-web-experts-transports#2314](https://geoservices.ign.fr/services-web-experts-transports#2314)
- Sites référencés dans Cartofriches [https://www.data.gouv.fr/fr/datasets/sites-references-dans-cartofriches/](https://www.data.gouv.fr/fr/datasets/sites-references-dans-cartofriches/)
- Corine Land Cover [http://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/](http://www.data.gouv.fr/fr/datasets/corine-land-cover-occupation-des-sols-en-france/)
- Fiches signalétiques des points géodésiques et des repères de nivellement [https://www.data.gouv.fr/fr/datasets/fiches-signaletiques-des-points-geodesiques-et-des-reperes-de-nivellement/](https://www.data.gouv.fr/fr/datasets/fiches-signaletiques-des-points-geodesiques-et-des-reperes-de-nivellement/). Voir aussi les services de l’IGN [https://geoservices.ign.fr/services-web-experts-geodesie#3390](https://geoservices.ign.fr/services-web-experts-geodesie#3390)

# Télécommunications (antennes, réseaux)

- [Arcep couverture mobile](http://www.data.gouv.fr/fr/datasets/mon-reseau-mobile/)
- [Données ADSL et fibre](https://www.data.gouv.fr/fr/datasets/ma-connexion-internet/)
- [Déploiement haut et très haut débit fixe](https://www.data.gouv.fr/fr/datasets/le-marche-du-haut-et-tres-haut-debit-fixe-deploiements/)
- [Données sur les réseaux mobiles](https://data.anfr.fr/anfr/visualisation/information/?id=dd11fac6-4531-4a27-9c8c-a3a9e4ec2107)
- [Données sur les installations radioélectriques de plus de 5 watts](http://www.data.gouv.fr/fr/datasets/donnees-sur-les-installations-radioelectriques-de-plus-de-5-watts-1/)

# Éducation

- Académies
    - Contours géographiques des académies [http://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/](http://www.data.gouv.fr/fr/datasets/contours-geographiques-des-academies/)
- Zones de vacances
- Emplacement écoles
    - Adresse et géolocalisation des établissements d'enseignement du premier et second degrés [https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/](https://www.data.gouv.fr/fr/datasets/adresse-et-geolocalisation-des-etablissements-denseignement-du-premier-et-second-degres-1/)

# Élections

- Contours des circonscriptions des législatives [http://www.data.gouv.fr/fr/datasets/countours-des-circonscriptions-des-legislatives-nd/](http://www.data.gouv.fr/fr/datasets/countours-des-circonscriptions-des-legislatives-nd/)
- Carte des circonscriptions législatives françaises (2012+) [http://www.data.gouv.fr/fr/datasets/carte-des-circonscriptions-legislatives-francaises-2012-nd/](http://www.data.gouv.fr/fr/datasets/carte-des-circonscriptions-legislatives-francaises-2012-nd/)
- Découpage des cantons pour les élections départementales de mars 2015 [http://www.data.gouv.fr/fr/datasets/decoupage-des-cantons-pour-les-elections-departementales-de-mars-2015/](http://www.data.gouv.fr/fr/datasets/decoupage-des-cantons-pour-les-elections-departementales-de-mars-2015/)
- Contours détaillés des circonscriptions des législatives [http://www.data.gouv.fr/fr/datasets/contours-detailles-des-circonscriptions-des-legislatives/](http://www.data.gouv.fr/fr/datasets/contours-detailles-des-circonscriptions-des-legislatives/)
- Panneaux d'affichage électoral [http://www.data.gouv.fr/fr/datasets/panneaux-daffichage-electoral/](http://www.data.gouv.fr/fr/datasets/panneaux-daffichage-electoral/)

# Police, sécurité publique, sécurité civile, justice

Dispatcher entre droits/justice et sécurité

- Opérations coordonnées par les CROSS (Centres régionaux opérationnels de surveillance et de sauvetage) [https://www.data.gouv.fr/fr/datasets/operations-coordonnees-par-les-cross/](https://www.data.gouv.fr/fr/datasets/operations-coordonnees-par-les-cross/)
- Liste et localisation des Secrétariats Généraux pour l'Administration du Ministère de l'Intérieur (SGAMI) en métropole [https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-sgami/](https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-sgami/)
- Liste des services de police accueillant du public avec géolocalisation [http://www.data.gouv.fr/fr/datasets/liste-des-services-de-police-accueillant-du-public-avec-geolocalisation/](http://www.data.gouv.fr/fr/datasets/liste-des-services-de-police-accueillant-du-public-avec-geolocalisation/)
- Liste des unités de gendarmerie accueillant du public, comprenant leur géolocalisation et leurs horaires d'ouverture [https://www.data.gouv.fr/fr/datasets/liste-des-unites-de-gendarmerie-accueillant-du-public-comprenant-leur-geolocalisation-et-leurs-horaires-douverture/](https://www.data.gouv.fr/fr/datasets/liste-des-unites-de-gendarmerie-accueillant-du-public-comprenant-leur-geolocalisation-et-leurs-horaires-douverture/)
- Compétence territoriale gendarmerie et police nationales [https://www.data.gouv.fr/fr/datasets/competence-territoriale-gendarmerie-et-police-nationales/](https://www.data.gouv.fr/fr/datasets/competence-territoriale-gendarmerie-et-police-nationales/)
- Découpage des zones de sécurité prioritaires (ZSP) [https://www.data.gouv.fr/fr/datasets/decoupage-des-zones-de-securite-prioritaires-zsp-1/](https://www.data.gouv.fr/fr/datasets/decoupage-des-zones-de-securite-prioritaires-zsp-1/)
- Base de données des barreaux d'avocats de France [https://www.data.gouv.fr/fr/datasets/base-de-donnees-des-barreaux-davocats-de-france/](https://www.data.gouv.fr/fr/datasets/base-de-donnees-des-barreaux-davocats-de-france/)
- 

# Santé

- Don du sang [http://www.data.gouv.fr/fr/datasets/dates-et-lieux-des-collectes-de-don-du-sang/](http://www.data.gouv.fr/fr/datasets/dates-et-lieux-des-collectes-de-don-du-sang/)
- FINESS Extraction du Fichier des établissements [http://www.data.gouv.fr/fr/datasets/finess-extraction-du-fichier-des-etablissements/](http://www.data.gouv.fr/fr/datasets/finess-extraction-du-fichier-des-etablissements/)
- Lieux de vaccination Covid-19 (pharmacies) - [Santé.fr](http://xn--sant-epa.fr/) [http://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-covid-19-pharmacies-sante-fr/](http://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-covid-19-pharmacies-sante-fr/)
- Lieux de vaccination contre la Covid-19 [http://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-contre-la-covid-19/](http://www.data.gouv.fr/fr/datasets/lieux-de-vaccination-contre-la-covid-19/)
- Géo'DAE - Base Nationale des Défibrillateurs [http://www.data.gouv.fr/fr/datasets/geodae-base-nationale-des-defibrillateurs/](http://www.data.gouv.fr/fr/datasets/geodae-base-nationale-des-defibrillateurs/)
- Résultats des contrôles officiels sanitaires : dispositif d'information « Alim’confiance » [https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/](https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/) (API sans archivage). Voir [https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/#resource-6c6484fe-7024-452a-a156-b2effbaad598-title](https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/#resource-6c6484fe-7024-452a-a156-b2effbaad598-title) pour une version avec historique et coordonnées

## Agriculture

- Registre parcellaire graphique (RPG) : contours des parcelles et îlots culturaux et leur groupe de cultures majoritaire [http://www.data.gouv.fr/fr/datasets/registre-parcellaire-graphique-rpg-contours-des-parcelles-et-ilots-culturaux-et-leur-groupe-de-cultures-majoritaire/](http://www.data.gouv.fr/fr/datasets/registre-parcellaire-graphique-rpg-contours-des-parcelles-et-ilots-culturaux-et-leur-groupe-de-cultures-majoritaire/) (**SPD**)
- Parcelles en Agriculture Biologique (AB) déclarées à la PAC [http://www.data.gouv.fr/fr/datasets/parcelles-en-agriculture-biologique-ab-declarees-a-la-pac/](http://www.data.gouv.fr/fr/datasets/parcelles-en-agriculture-biologique-ab-declarees-a-la-pac/)
- Agriculture biologique 2008-2011 - nombre d'opérateurs engagés en agriculture biologique [http://www.data.gouv.fr/fr/datasets/agriculture-biologique-2008-2011-nombre-d-operateurs-engages-en-agriculture-biologique-30378896/](http://www.data.gouv.fr/fr/datasets/agriculture-biologique-2008-2011-nombre-d-operateurs-engages-en-agriculture-biologique-30378896/) (information rapportable à une région ou un département)
- Délimitation Parcellaire des AOC Viticoles de l'INAO [http://www.data.gouv.fr/fr/datasets/delimitation-parcellaire-des-aoc-viticoles-de-linao/](http://www.data.gouv.fr/fr/datasets/delimitation-parcellaire-des-aoc-viticoles-de-linao/)

## Patrimoine/culture/tourisme/sports

- Immeubles protégés au titre des Monuments Historiques [https://www.data.gouv.fr/fr/datasets/immeubles-proteges-au-titre-des-monuments-historiques-2/](https://www.data.gouv.fr/fr/datasets/immeubles-proteges-au-titre-des-monuments-historiques-2/)
- Liste et localisation des Musées de France [https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/](https://www.data.gouv.fr/fr/datasets/liste-et-localisation-des-musees-de-france/)
- Liste des objets mobiliers propriété publique classés au titre des Monuments Historiques [https://www.data.gouv.fr/fr/datasets/liste-des-objets-mobiliers-propriete-publique-classes-au-titre-des-monuments-historiques/](https://www.data.gouv.fr/fr/datasets/liste-des-objets-mobiliers-propriete-publique-classes-au-titre-des-monuments-historiques/) (information rapportable à la commune via le code INSEE)
- Fréquentation des musées de France [http://www.data.gouv.fr/fr/datasets/frequentation-des-musees-de-france/](http://www.data.gouv.fr/fr/datasets/frequentation-des-musees-de-france/) (à lier géographiquement avec [https://data.culture.gouv.fr/explore/dataset/liste-et-localisation-des-musees-de-france/information/](https://data.culture.gouv.fr/explore/dataset/liste-et-localisation-des-musees-de-france/information/))
- Panorama des festivals [http://www.data.gouv.fr/fr/datasets/panorama-des-festivals/](http://www.data.gouv.fr/fr/datasets/panorama-des-festivals/)
- DATAtourisme, la base nationale des données du tourisme en Open Data [http://www.data.gouv.fr/fr/datasets/datatourisme-la-base-nationale-des-donnees-du-tourisme-en-open-data/](http://www.data.gouv.fr/fr/datasets/datatourisme-la-base-nationale-des-donnees-du-tourisme-en-open-data/)
- Données touristiques de la base DATAtourisme [http://www.data.gouv.fr/fr/datasets/donnees-touristiques-de-la-base-datatourisme/](http://www.data.gouv.fr/fr/datasets/donnees-touristiques-de-la-base-datatourisme/)
- Zones Touristiques Internationales [http://www.data.gouv.fr/fr/datasets/zones-touristiques-internationales/](http://www.data.gouv.fr/fr/datasets/zones-touristiques-internationales/)
- Localisation des sites de fouille archéologiques de l'Inrap [http://www.data.gouv.fr/fr/datasets/localisation-des-sites-de-fouille-archeologiques-de-l-inrap-576210/](http://www.data.gouv.fr/fr/datasets/localisation-des-sites-de-fouille-archeologiques-de-l-inrap-576210/)
- Données géocodées issues du recensement des licences et clubs auprès des fédérations sportives agréées par le ministère chargé des sports [http://www.data.gouv.fr/fr/datasets/donnees-geocodees-issues-du-recensement-des-licences-et-clubs-aupres-des-federations-sportives-agreees-par-le-ministere-charge-des-sports/](http://www.data.gouv.fr/fr/datasets/donnees-geocodees-issues-du-recensement-des-licences-et-clubs-aupres-des-federations-sportives-agreees-par-le-ministere-charge-des-sports/)

## POIs

- Recensement des équipements sportifs, espaces et sites de pratiques [http://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/](http://www.data.gouv.fr/fr/datasets/recensement-des-equipements-sportifs-espaces-et-sites-de-pratiques/) (soit à géocoder soit pour avoir les informations à la commune)
- Base permanente des équipements [https://www.data.gouv.fr/fr/datasets/base-permanente-des-equipements-1/](https://www.data.gouv.fr/fr/datasets/base-permanente-des-equipements-1/)
- Liste des boîtes aux lettres de rue France métropolitaine et DOM avec heure limite de dépôt [http://www.data.gouv.fr/fr/datasets/liste-des-boites-aux-lettres-de-rue-france-metropolitaine-et-dom-avec-heure-limite-de-depot-1/](http://www.data.gouv.fr/fr/datasets/liste-des-boites-aux-lettres-de-rue-france-metropolitaine-et-dom-avec-heure-limite-de-depot-1/)
- Adresses des débits de tabac [http://www.data.gouv.fr/fr/datasets/adresses-des-debits-de-tabac/](http://www.data.gouv.fr/fr/datasets/adresses-des-debits-de-tabac/)
- Liste des structures France services [https://www.data.gouv.fr/fr/datasets/62503e25bc0f6370f4a651ce/](https://www.data.gouv.fr/fr/datasets/62503e25bc0f6370f4a651ce/)

# Fonds de plan:

## Niveau France

- Données OpenStreetMap intégrales de France Métropolitaine [https://www.data.gouv.fr/fr/datasets/donnees-openstreetmap-integrales-de-france-metropolitaine/](https://www.data.gouv.fr/fr/datasets/donnees-openstreetmap-integrales-de-france-metropolitaine/)
- Fonds de carte IGN France et régions [https://www.data.gouv.fr/fr/datasets/fonds-de-carte-ign-france-et-regions-571459/](https://www.data.gouv.fr/fr/datasets/fonds-de-carte-ign-france-et-regions-571459/) (rare cas où la donnée est en fait des PDF à réutiliser sous forme papier)
- BD TOPO® (description vectorielle 3D des éléments du territoire et de ses infrastructures) [http://www.data.gouv.fr/fr/datasets/bd-topo-r/](http://www.data.gouv.fr/fr/datasets/bd-topo-r/)
- BD ORTHO® (images aériennes raster) [https://www.data.gouv.fr/fr/datasets/bd-ortho-r/](https://www.data.gouv.fr/fr/datasets/bd-ortho-r/)
- Métadonnée des photos aériennes anciennes de l'IGN [http://www.data.gouv.fr/fr/datasets/metadonnee-des-photos-aeriennes-anciennes-de-lign/](http://www.data.gouv.fr/fr/datasets/metadonnee-des-photos-aeriennes-anciennes-de-lign/)

## Niveau Europe

- EuroGlobalMap - données topographiques au 1/1 000 000 couvrant 45 pays et territoires en Europe [http://www.data.gouv.fr/fr/datasets/euroglobalmap-donnees-topographiques-au-1-1-000-000-couvrant-45-pays-et-territoires-en-europe/](http://www.data.gouv.fr/fr/datasets/euroglobalmap-donnees-topographiques-au-1-1-000-000-couvrant-45-pays-et-territoires-en-europe/)

## Niveau Monde

- COPERNICUS - Satellite Sentinel 1A [http://www.data.gouv.fr/fr/datasets/copernicus-satellite-sentinel-1a/](http://www.data.gouv.fr/fr/datasets/copernicus-satellite-sentinel-1a/)

## Données Monde génériques (hors data.gouv.fr)

- Natural Earth Data [https://www.naturalearthdata.com/downloads/](https://www.naturalearthdata.com/downloads/) (pays, principales villes, rivières, lacs, fond de plan raster altimétrie/bathymétrie)
- Données bathymétriques [https://www.gebco.net/data_and_products/gridded_bathymetry_data/](https://www.gebco.net/data_and_products/gridded_bathymetry_data/)
- Speedtest by Ookla Global Fixed and Mobile Network Performance Maps [https://registry.opendata.aws/speedtest-global-performance/](https://registry.opendata.aws/speedtest-global-performance/)
