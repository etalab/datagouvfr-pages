---
title: Les API dédiées à l'authentification des personnes et des organisations
keywords:
  - api
  - franceconnect
  - identite
  - sante
  - proconnect
  - santeconnect
  - pro
  - openid
  - siret
  - siren
  - acces
  - securite
  - authentification
  - bouton
description: API permettant d'authentifier les particuliers et les organisations
---

# Les API dédiées à l'authentification des personnes et des organisations

## Dans quel cas l'authentification des personnes ou des organisations est nécessaire ?

### 🙋🏽‍♀️ Démarches administratives des particuliers

Lors d'une démarche administrative, les administrations doivent s'assurer que la personne qui saisit ses informations en ligne est authentifiée.
Le couple identifiant / mot de passe est une solution, mais elle comporte des limites (multiplication des mots de passe), et la gestion de la sécurité des comptes nécessite un investissement humain et technologique conséquent.

**Le bouton France Connect vise à simplifier l'authentification des particuliers**, qui sont de plus en plus nombreux à disposer d'un compte France Connect.

Une fois implémenté par l'administration, il permet non seulement de garantir une authentification sécurisée pour les usagers, mais également de **récupérer les données nécessaires à la démarche** (données fiscales, statut étudiant ou boursier, statut demandeur d'emploi, attestation de droits de la CNAM, etc...)

[🔎 En savoir plus sur FranceConnect les API FranceConnectées](https://www.data.gouv.fr/fr/pages/api_franceconnectees)

### 🏛️ Connecter des professionnels

Certaines applications veulent pouvoir identifier des professionnels, que ce soit par exemple pour des démarches, du logiciel bureautique, des accès à des données.

Plutôt que de demander des justificatifs et de les vérifier manuellement, ProConnect permet d'**obtenir l'identité de la structure** : Numéro SIRET, code Commune (COG), Code d'activité (NAF), etc... et de **vérifier automatiquement l'adresse e-mail** (correspondance du nom de domaine et vérification de la réception des e-mails).

- [ProConnect](https://www.proconnect.gouv.fr/) pour les professionnels,
- [Pro Santé Connect](https://esante.gouv.fr/produits-services/pro-sante-connect) pour les professionnels de la sphère sanitaire et sociale.


## Quelles API utiliser pour authentifier des personnes ou des organisations ?

| Population                             | FranceConnect | ProConnect   | ProSantéConnect |
|----------------------------------------|---------------|--------------|-----------------|
| Particuliers                           | ✅             | ❌           | ❌               |
| Professionnels                         | ❌             | ✅           | ✅               |
| Professionnels de la santé             | ❌             | ✅           | ✅               |
| Entreprises                            | ❌             | ✅           | ❌               |
| Agents de l'administration centrale    | ❌             | ✅           | ❌               |
| Agents des collectivités territoriales | ❌             | ✅           | ❌               |


## Comment accéder aux API ?

Les API d’authentification sont réservées aux administrations et à leurs éditeurs.

#### [🇫🇷 API FranceConnect](TODO)

#### [🏛️ API ProConnect](TODO)

#### [🏥 API Pro Santé Connect](TODO)

