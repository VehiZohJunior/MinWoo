# Guide de contribution au corpus MinWoo

Ce guide explique comment remplir les fichiers de vocabulaire pour le Yacouba (`content/yacouba/vocabulaire.csv`) et le Toura (`content/toura/vocabulaire.csv`). Chaque langue a son propre fichier avec les mêmes colonnes.

Les fichiers sont au format CSV : ils s'ouvrent directement avec **Excel** ou **Google Sheets**. Ouvrez le fichier, ajoutez une ligne par mot, puis enregistrez.

## Colonnes à remplir

| Colonne | Que mettre | Obligatoire ? |
|---|---|---|
| `id` | Un numéro unique (1, 2, 3...) | Oui |
| `categorie` | Voir liste des catégories ci-dessous | Oui |
| `mot_yacouba` / `mot_toura` | Le mot ou l'expression dans la langue | Oui |
| `traduction_francais` | Traduction en français | Oui |
| `traduction_anglais` | Traduction en anglais | Non (peut être ajoutée plus tard) |
| `prononciation_simplifiee` | Comment le prononcer, écrit simplement (ex: "bo-lo") | Oui |
| `transcription_api` | Transcription phonétique API/IPA (souvent ajoutée plus tard par un linguiste) | Non |
| `exemple_phrase_yacouba` / `exemple_phrase_toura` | Une phrase d'exemple utilisant le mot | Non, mais très utile |
| `exemple_phrase_francais` | Traduction française de la phrase d'exemple | Si exemple rempli |
| `contributeur` | Nom du locuteur natif qui a fourni ce mot | Oui |
| `date_contribution` | Date au format AAAA-MM-JJ | Oui |
| `statut_validation` | `à valider`, `validé`, ou `rejeté` | Oui (commencer par "à valider") |
| `notes` | Toute remarque (variante régionale, nuance, etc.) | Non |

## Catégories suggérées pour commencer (par ordre de priorité)

1. **Salutations et politesse** (bonjour, merci, s'il vous plaît...)
2. **Nombres** (1 à 20 au minimum)
3. **Famille** (père, mère, frère, sœur, enfant...)
4. **Corps humain** (tête, main, pied, œil...)
5. **Nourriture et boissons**
6. **Verbes courants** (manger, boire, dormir, aller, venir, parler...)
7. **Temps et calendrier** (jours, aujourd'hui, hier, demain...)
8. **Nature et environnement**
9. **Phrases de la vie quotidienne** (comment ça va, je m'appelle...)

Commencez par les catégories 1 à 4 : ce sont les bases qui permettent de construire les premières leçons de l'application.

## Processus de validation

- Chaque mot commence avec le statut `à valider` dès qu'un contributeur l'ajoute.
- Un deuxième locuteur natif ou un chercheur relit et passe le statut à `validé` (ou `rejeté` avec une note expliquant pourquoi).
- Seuls les mots `validé` seront utilisés dans l'application pour les apprenants — cela garantit la fiabilité du contenu, un point essentiel pour la crédibilité scientifique du projet.

## Une fois rempli

Enregistrez le fichier CSV et prévenez-moi (dites-moi combien de mots ont été ajoutés). J'intégrerai ensuite ce contenu dans la structure de l'application.
