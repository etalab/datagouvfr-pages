---
title: Les API FranceConnectées
keywords:
  - api
  - franceconnect
  - identite
  - pivot
  - bouton
description: Guide pour comprendre ce qu'est une API FranceConnectée, quel est leur intérêt et leur fonction
---

# Les API FranceConnectées

[🔎 En savoir plus sur les API](https://www.data.gouv.fr/fr/pages/api-definition)
[➡️ Accéder à l’API Géorisques](TODO)

[FranceConnect](https://franceconnect.gouv.fr/) permet au citoyen de s'authentifier à de nombreux services de l'administration. Ce dispositif permet d'utiliser un compte existant sur impots.fr ou ameli.fr par exemple, afin d'accéder à tous les services de l'administration.


Les API FranceConnectées sont des API, **en accès restreint et souvent accessibles uniquement aux administrations**, qui permettent d'accéder aux données administratives d'un particulier. **Leur particularité est de proposer une modalité d'appel via FranceConnect**. Elles permettent alors de transmettre - _en plus des données d'identité pivot de FranceConnect_ - d'**autres données personnelles du citoyen**.

**Concrêtement, prenons un usager effectuant une démarche en ligne :** L'usager commence sa démarche, il a besoin de renseigner des justificatifs administratifs. Le service en ligne lui propose de s'authentifier, et met à disposition le bouton "Se connecter via FranceConnect". En cliquant et en confirmant suite au parcours FranceConnect, il permet à FranceConnect de transmettre ses données d'identité directement à une API FranceConnectée qui retourne alors les données qu'elle détient. 

## Qui peut accéder à ces API FranceConnectées ?

Globalement, seules les administrations peuvent utiliser les API FranceConnectées. 

Dans le détail, en tant qu'organisation proposant une démarche en ligne, il faut être éligible et effectuer une demande d'habilitation auprès de : 
- **FranceConnect pour implémenter le bouton FranceConnect**. Toute administation ou collectivité est éligible, et dans des cas spécifiques, certaines entreprises et associations le sont aussi. Pour en savoir plus, consulter la [documentation de FranceConnect](https://franceconnect.gouv.fr/partenaires) ; 
- **Administration en charge de l'API FranceConnectée**, et pouvoir expliquer en quoi le cas d'usage de la démarche justifie d'accéder aux données personnelles de cette API.


## À quoi servent-elles ?

Les API FranceConnectées simplifient les démarches en ligne d'un usager, car elles lui évitent la saisie de données personnelles utilisées comme paramètres d'appel aux API (par exemple : le _numéro fiscal_ sert de paramètre d'appel pour les API fiscales et doit être saisi par l'utilisateur si la démarche n'utilise pas d'API FranceConnectée). C'est l'identité pivot fournie par FranceConnect qui fait office de modalité d'appel pour une API FranceConnectée, le usager n'a donc rien à saisir.

**Le parcours d'un usager dans une démarche avec API en modalité d'appel classique :**

- 👤 Connexion par son compte associé à la démarche
- 🔍 Recherche du paramètre demandé dans ses documents personnels (par exemple _le numéro fiscal_ ou _nom, prénom, date et lieu de naissance_)
- 🗝 Saisie de ce ou ces paramètre(s)
- 👩‍💻 Récupération de données par API

**Le parcours grâce aux API FranceConnectées :**

- 🇫🇷 Connexion par FranceConnect
- ✅ Récupération de données grâce aux API FranceConnectées

**Les API FranceConnectées simplifient :**

| La démarche du usager                      | Le traitement de l'agent                                        |
| ------------------------------------------- | --------------------------------------------------------------- |
| Des démarches simplifiées et accélérées     | Les délais de traitement sont instantanés                       |
| Plus aucune pièces justificatives à fournir | Plus de pièces justificatives à traiter et à stocker            |
| Plus d'erreur de saisie possible            | Plus de fraude possible car la donnée est certifiée à la source |

## Un cas pratique : la demande d'Aide Juridictionnelle

_Témoignage du Ministère de la Justice :_

> L'aide juridictionnelle est une prise en charge par l'État des frais judiciaires, réservée aux revenus les plus modestes. Grâce à la vérification des revenus avec l'API Impot Particulier FranceConnectée, ce sont 1,2 millions de formulaires CERFA qui seront soumis en ligne en lieu et place d'un dossier papier !

## Comment fonctionnent-elles techniquement ?

_Schéma de fonctionnement des API FranceConnectées :_
![Fonctionnement des API FranceConnectées](https://franceconnect.gouv.fr/images/how-it-works-data.svg)

## Comment accéder aux API FranceConnectées ?

Les API FranceConnectées ne sont accessibles qu’aux administrations publiques, collectivités territoriales ou entreprises privées en situation de mission de service public. Elles nécessitent de :

1. Avoir FranceConnect [sur son téléservice](https://franceconnect.gouv.fr/partenaires)
2. Faire une demande d'habilitation à l’API FranceConnectée en question
3. Brancher l’API
4. 🎉 Commencer à dématérialiser 🥳
