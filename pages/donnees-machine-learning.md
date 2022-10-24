---
title: Les données ouvertes pour l’apprentissage automatique (Machine Learning)
keywords:
  - machine-learning
  - IA
  - AI
  - apprentissage-automatique
description: Les jeux de données qui se prêtent bien à l’apprentissage automatique (Machine Learning) disponibles sur data.gouv.fr.
menu:
  - footer
datasets:
- emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france
- liste-des-logements-proposes-en-airbnb-sur-bordeaux
- agribalyse-r-synthese-1
- donnees-carroyees-issues-du-dispositif-sur-les-revenus-localises-fiscaux-et-sociaux-filosofi
- demandes-de-valeurs-foncieres
- inventaire-de-gaz-a-effet-de-serre-territorialise
- insertion-professionnelle-des-diplomes-de-master-en-universites-et-etablissements-assimil-0
- bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019
- arbres-urbains
- resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance
- concentration-horaire-des-polluants-air-ambiant-ligair-orleans-metropole
- donnees-brutes-de-contribution-anonymisees
- donnees-hospitalieres-relatives-a-lepidemie-de-covid-19
- donnees-des-urgences-hospitalieres-et-de-sos-medecins-relatives-a-lepidemie-de-covid-19
- indicateurs-de-suivi-de-lepidemie-de-covid-19
- eclairage-public-de-la-ville-de-bethune-2017-2019-1
- parcoursup-2020-voeux-de-poursuite-detudes-et-de-reorientation-dans-lenseignement-superieur-et-reponses-des-etablissements

---
# Catalogue des datasets de *data.gouv.fr* pour le Machine Learning

Cette page a pour vocation de référencer les principaux jeux de données qui se prêtent bien à l’apprentissage automatique (*Machine Learning*) disponibles sur data.gouv.fr. Elle n’est pas exhaustive et est ouverte aux contributions.

> Pour en savoir plus sur le contexte dans lequel s’inscrit ce catalogue et sur sa construction vous pouvez lire [l’article dédié](https://www.data.gouv.fr/fr/posts/les-donnees-ouvertes-pour-lapprentissage-automatique-machine-learning). 

Nous proposons ici un **catalogue des jeux de données identifiés comme exploitables par des algorithmes d’apprentissage automatique regroupés par tâche.**
Chaque jeu est accompagné : 
- d’un **profiling** qui vous permettra d’explorer le jeu de données et d’obtenir un résumé de ses statistiques descriptives ; 
- des **résultats de l’entraînement et du test automatique d’algorithmes classiques de Machine Learning** : métriques, matrices de confusion, graphiques, etc. ([voir le guide pour mieux comprendre ces résultats](https://github.com/etalab-ia/open_ML/blob/main/docs/explain_automodels/Guide%20au%20AutoML%20Leaderboard%20report.md)).

> Pour davantage de lisibilité, l’inventaire présenté ici est également [disponible sous la forme d’une application.](https://datascience.etalab.studio/dgml/)

*N.b.: Cette page est en cours de construction et est [ouvertes à la contribution](https://github.com/etalab/datagouvfr-pages/tree/master/pages) plus de jeux de données sont à venir. Le profiling a été effectué avec [Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/) et les modèles ont été entrainés à l’aide de [mljar-supervised](https://supervised.mljar.com/)*.

## Régression


[**Émissions de CO2 et de polluants des véhicules commercialisés en France**](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/)
*Ce jeu de données présente l’ensemble des caractéristiques techniques des véhicules commercialisés en France en 2013, ainsi que les consommations de carburant, les émissions de CO2 et de polluants de l’air.*  
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/6ff09b59-84ca-4346-a8d1-3587ed94da15.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/6ff09b59-84ca-4346-a8d1-3587ed94da15/README.html) (target variable: *CO2*)
  - [Réutilisation data.gouv](https://www.data.gouv.fr/fr/reuses/predict-co2-emissions-of-different-cars/)

[**Liste des logements proposés en Airbnb sur Bordeaux**](https://www.data.gouv.fr/en/datasets/liste-des-logements-proposes-en-airbnb-sur-bordeaux/)
C*e jeu de données contient un recensement des caractéristiques des logements (prix par nuit, nombre de pièces, services disponibles, etc.) proposés par Airbnb à Bordeaux.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/123e1c18-37e0-4147-ad65-768320387800.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/123e1c18-37e0-4147-ad65-768320387800/README.html) (target variable: *PrixNuitee*)

[**AGRIBALYSE® - Synthèse**](https://www.data.gouv.fr/fr/datasets/agribalyse-r-synthese-1/)
*AGRIBALYSE® est une base de données de référence des indicateurs d’impacts environnementaux des produits agricoles et des produits alimentaires consommés en France. Vous trouverez le recensement des caractéristiques de plusieurs aliments ainsi que les émissions de polluants qui leur sont associés.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/c763b24a-a0fe-4e77-9586-3d5453c631cd.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/c763b24a-a0fe-4e77-9586-3d5453c631cd/README.html) (target variable: *DQR — Note de qualité de la donnée (1 excellente ; 5 très faible)*)

[**Données carroyées issues du dispositif sur les revenus localisés fiscaux et sociaux**](https://www.data.gouv.fr/fr/datasets/donnees-carroyees-issues-du-dispositif-sur-les-revenus-localises-fiscaux-et-sociaux-filosofi/)
*Ces données proviennent du dispositif sur les revenus localisés sociaux et fiscaux (FiLoSoFi) et contiennent des variables sur la structure par âge des individus, sur les caractéristiques des ménages et des logements et sur les revenus de l’année 2015. On se restreint ici au jeu de données correspondant à la France métropolitaine.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/aa50b408-49f4-4608-97fd-dd8fb21ef239.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/aa50b408-49f4-4608-97fd-dd8fb21ef239/README.html) (target variable: *Log_soc*)
  - [Réutilisation data.gouv.fr](https://www.data.gouv.fr/fr/reuses/deep-learning-pour-la-prediction-de-la-densite/)

[**Demande de valeurs foncières**](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/) 
*Publié et produit par la direction générale des finances publiques, ce jeu de données permet de connaître les transactions immobilières intervenues au cours des cinq dernières années sur le territoire métropolitain et les DOM-TOM. On se restreint ici aux données du premier trimestre de 2020.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/90a98de0-f562-4328-aa16-fe0dd1dca60f.html)
  - [Modèle](https://github.com/etalab-ia/DGML/blob/main/docs/automodels/90a98de0-f562-4328-aa16-fe0dd1dca60f/README.md) (target variable: *valeur foncière*)

[**Concentration horaire des polluants —Air ambiant —Lig'Air - Orléans Métropole**](https://www.data.gouv.fr/fr/datasets/concentration-horaire-des-polluants-air-ambiant-ligair-orleans-metropole/)
*Ce jeu de données contient les concentrations moyennes horaires des principaux polluants de l’air réglementés dans la région Centre-Val de Loire : monoxyde d’azote NO et dioxyde d’azote NO2, particules en suspension PM10, particules en suspension PM2.5, ozone O3, monoxyde de carbone CO. Les données sont souvent mises à jour et peuvent donc évoluer.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/ce203343-6ed9-4fd3-b310-e553ae437f6d.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/AutoML_conc_poll_reg/README.html) (target variable: *valeur*)

[**Inventaire de gaz à effet de serre territorialisé**](https://www.data.gouv.fr/fr/datasets/inventaire-de-gaz-a-effet-de-serre-territorialise/#_)
*Ce jeu de données recense les effets de l’ensemble des gaz à effet de serre, en détaillant les émissions par commune et par secteur en 2016.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/4072eb84-5093-4490-96e6-bcec87f51ea8.html)

[**Insertion professionnelle des diplômés de Master en universités et établissements assimilés**](https://www.data.gouv.fr/fr/datasets/insertion-professionnelle-des-diplomes-de-master-en-universites-et-etablissements-assimil-0/#_)
*Ce jeu contient les données issues de l’opération nationale de collecte de données sur l’insertion professionnelle (taux d’insertion, salaire, etc.) des diplômés de Master.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/a27a4212-6732-408e-85e4-819ce897046b.html)

## Classification

[**Bases de données annuelles des accidents corporels de la circulation routière - Années de 2005 à 2019**](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2019/#_)
*Ces jeux de données répertorient l’intégralité des accidents corporels de la circulation intervenus durant une année précise en France métropolitaine et dans les DOM-TOM. Ils comprennent des informations de localisation de l’accident ainsi que des informations concernant les caractéristiques de l’accident et son lieu, les véhicules impliqués et leurs victimes.
Ici nous avons choisi les données de 2019 et nous avons concaténé les jeux disponibles (caractéristique, lieux, véhicule, usager) dans un unique jeu de données.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/6af37c98-0933-4ae4-8380-5f63212fb52a.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/6af37c98-0933-4ae4-8380-5f63212fb52a/README.html) (target variable: *grav*)
  - [Réutilisation data.gouv.fr](https://www.data.gouv.fr/fr/reuses/machine-learning-pour-predire-la-gravite-des-accidents/)

[**Arbres urbains**](https://www.data.gouv.fr/fr/datasets/arbres-urbains/)
*Ce jeu de données comprend des informations sur la localisation, l’espèce, les dimensions, les spécificités et l’état de santé du patrimoine arboré de la commune de Saint-Germain-en-Laye.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/96f4164d-956d-4c1c-b161-68724eb0ccdc.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/96f4164d-956d-4c1c-b161-68724eb0ccdc/README.html) (target variable: *classification_diagnostic*)

[**Résultats des contrôles officiels sanitaires : dispositif d’information « Alim’confiance »**](https://www.data.gouv.fr/fr/datasets/resultats-des-controles-officiels-sanitaires-dispositif-dinformation-alimconfiance/) 
*Ce jeu de données contient le résultat des contrôles officiels en sécurité sanitaire des aliments réalisés dans tous les établissements de la chaîne alimentaire : abattoirs, commerces de détail (métiers de bouche, restaurants, supermarchés, marchés, vente à la ferme, etc.), restaurants collectifs et établissements agroalimentaires.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/fff0cc27-977b-40d5-9c11-f7e4e79a0b72.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/fff0cc27-977b-40d5-9c11-f7e4e79a0b72/README.html) (target variable : *Synthese_eval_sanit*)
  - [Réutilisation data.gouv.fr](https://www.data.gouv.fr/fr/reuses/predire-la-qualite-sanitaire-dun-etablissement-alimentaire/)

[**Concentration horaire des polluants —Air ambiant —Lig'Air - Orléans Métropole**](https://www.data.gouv.fr/fr/datasets/concentration-horaire-des-polluants-air-ambiant-ligair-orleans-metropole/)
*Ce jeu de données contient les concentrations moyennes horaires des principaux polluants réglementés dans l’air sur la région Centre-Val de Loire : monoxyde d’azote NO et dioxyde d’azote NO2, particules en suspension PM10, particules en suspension PM2.5, ozone O3, monoxyde de carbone CO. Les données sont souvent mises à jour et peuvent donc évoluer.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/ce203343-6ed9-4fd3-b310-e553ae437f6d.html)
  - [Modèle](https://etalab-ia.github.io/DGML/automodels/AutoML_conc_poll_class/README.html) (target variable: *nom_poll*)

[**Données sur l’orientation des toits en France**](https://www.data.gouv.fr/fr/datasets/donnees-brutes-de-contribution-anonymisees/#resource-849fa6c2-7d0b-46b8-9814-29bf18b35bfa)
*Ces jeux de données, réutilisés dans le projet [*OpenSolar*]( https://github.com/opensolarmap/solml), se composent d’un datasses *contributions* (id OpenStreetMap du bâtiment ainsi que l’orientation du toit) et *bâtiments* (id, géométrie, surface du bâtiment et orientation du toit).*
  - [Profiling du dataset bâtiments](https://etalab-ia.github.io/DGML/profilings/849fa6c2-7d0b-46b8-9814-29bf18b35bfa.html), 
  - [Profiling du dataset contributions](https://etalab-ia.github.io/DGML/profilings/aef0f017-ba25-4772-b0e7-8693308d4404.html)

## Séries temporelles

[Données hospitalières relatives à l’épidémie de COVID-19](https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/) 
*Cinq jeux de données différents sont proposés contenant des données sur les hospitalisations, les réanimations et les décès, regroupés par région, puis par département et par sexe, par classe d’âge et par établissements.*
  - [Profiling du jeu de données par région et classe d’âge du patient](https://etalab-ia.github.io/DGML/profilings/08c18e08-6780-452d-9b8c-ae244ad529b3.html) 
  - [Profiling du jeu de données par département](https://etalab-ia.github.io/DGML/profilings/41b9bd2a-b5b6-4271-8878-e45a8902ef00.html),
  - [Profiling du jeu de données par département et sexe du patient](https://etalab-ia.github.io/DGML/profilings/63352e38-d353-4b54-bfd1-f1b3ee1cabd7.html) ;
  - [Profiling du jeu de données établissements hospitaliers par département](https://etalab-ia.github.io/DGML/profilings/6fadff46-9efd-4c53-942a-54aca783c30c.html) ;
  - [Profiling du jeu de données des nouvelles admissions en réanimation par région](https://etalab-ia.github.io/DGML/profilings/a1466f7f-4ece-4158-a373-f5d4db167eb0.html).

[Données des urgences hospitalières et de SOS Médecins relatives à l’épidémie de COVID-19](https://www.data.gouv.fr/en/datasets/donnees-des-urgences-hospitalieres-et-de-sos-medecins-relatives-a-lepidemie-de-covid-19/)
*Quatre jeux de données qui contiennent les données quotidiennes de SOS Médecins et des urgences hospitalières en relation à l’épidémie de Covid-19. On s’intéresse ici au jeu de données des passages quotidiens par département et par tranche d’âge.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/eceb9fb4-3ebc-4da3-828d-f5939712600a.html)

[Indicateurs de suivi de l’épidémie de COVID-19 ](https://www.data.gouv.fr/fr/datasets/indicateurs-de-suivi-de-lepidemie-de-covid-19/#_)
*Les données mises à disposition présentent la valeur quotidienne de 4 indicateurs (activité épidémique, taux de positivité des tests virologiques, évolution du R0, tension hospitalière sur la capacité en réanimation) au niveau national et départemental depuis le 15 mars 2020. On s’intéresse ici aux données par département.*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/4acad602-d8b1-4516-bc71-7d5574d5f33e.html)

[Éclairage public de la ville de Béthune 2017-2019 ](https://www.data.gouv.fr/fr/datasets/eclairage-public-de-la-ville-de-bethune-2017-2019-1/#_)
*Ce jeu de données contient des données sur l’éclairage public de la ville de Béthune (62400) sur la période de janvier 2017 à décembre 2019. En particulier : la consommation en kWhEN, la dépense en euros TTC, l’émission GES (KgCO2).*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/fd34262e-355d-4ac6-bac2-06c1b52fa42a.html)

## Apprentissage non supervisé

[Parcoursup 2020](https://www.data.gouv.fr/fr/datasets/parcoursup-2020-voeux-de-poursuite-detudes-et-de-reorientation-dans-lenseignement-superieur-et-reponses-des-etablissements/#resource-1d916b7c-bd4c-4951-845a-70f7ad7c17db)
*Ce jeu de données présente les voeux de poursuite d’études et de réorientation dans l’enseignement supérieur ainsi que les propositions des établissements pour chaque formation — hors apprentissage — à la fin du processus d’affectation de la plateforme Parcoursup pour la session 2020*
  - [Profiling](https://etalab-ia.github.io/DGML/profilings/1d916b7c-bd4c-4951-845a-70f7ad7c17db.html)
  - [Réutilisation data.gouv.fr](https://www.data.gouv.fr/fr/reuses/classifions-parcoursup/)

## Traitement automatique du langage

[PIAF](https://www.data.gouv.fr/fr/datasets/piaf-le-dataset-francophone-de-questions-reponses/) un jeu de données de questions réponses francophones
  - [Réutilisation data.gouv.fr](https://www.data.gouv.fr/fr/reuses/modele-de-questions-reponses-francophone/)
