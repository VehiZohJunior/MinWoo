# MinWoo — Référentiel pédagogique et linguistique

Version 1.0 — 21 novembre 2026. Document de travail soumis au comité scientifique.

Ce document fixe l'architecture d'apprentissage de MinWoo : comment un débutant complet progresse jusqu'à pouvoir lui-même transmettre la langue. Il ne contient **aucune donnée de langue inventée** : les mots, phrases, proverbes et enregistrements viendront exclusivement du comité scientifique, après double validation. Les seules formes citées ici proviennent de publications scientifiques, avec leur source.

La version lisible par l'application est `content/curriculum/programme.json` ; le format des données attendues du comité est `content/schema/modele-de-donnees.schema.json`.

---

## 1. Dix principes

1. **L'apprenant agit dans une situation réelle.** Chaque unité aboutit à une tâche de communication (saluer un aîné, acheter au marché, raconter un conte), conformément à l'approche actionnelle du CECR (Conseil de l'Europe 2001, 2020).
2. **Quatre volets équilibrés.** Chaque unité combine, en proportions voisines, l'écoute centrée sur le sens, la production centrée sur le sens, l'étude explicite de la langue et l'entraînement à la fluidité (Nation 2007). L'étude explicite ne dépasse pas environ un quart du temps.
3. **L'oreille d'abord.** On entend avant de parler, et on entend plusieurs voix. L'entraînement perceptif à voix multiples améliore la perception des tons chez l'adulte et se transfère en partie à la production (Wang et al. 1999 ; Sakai & Moorman 2018). D'où l'exigence de trois enregistrements par mot, par des locuteurs différents.
4. **Le ton fait partie du mot dès le premier jour.** En dan, le ton distingue les mots et porte une partie de la grammaire (Vydrin 2021). Il n'est jamais présenté comme un détail optionnel ou réservé aux avancés.
5. **La grammaire se découvre avant de s'expliquer.** L'apprenant observe des exemples, remarque la régularité, puis reçoit l'explication en français simple.
6. **On se souvient de ce qu'on rappelle.** Révision espacée et rappel actif plutôt que relecture : l'effet de test et l'espacement sont parmi les résultats les plus solides de la psychologie de l'apprentissage (Pimsleur 1967 ; Roediger & Karpicke 2006 ; Cepeda et al. 2006).
7. **La langue vit dans une société.** Variation dialectale, registres, âge et statut des interlocuteurs, contact avec le français et le dioula sont enseignés, pas gommés.
8. **La langue est la mémoire d'un milieu.** Parenté, calendrier agricole, plantes, animaux, lieux et savoir-faire sont des contenus à part entière : c'est le point de vue de l'écologie des langues (Haugen 1972).
9. **Rien sans source ni validation.** Chaque donnée porte sa source, son locuteur, son consentement, et la validation d'un second membre du comité. Les exemples sont présentés selon les règles de glose de Leipzig (Comrie, Haspelmath & Bickel 2008).
10. **La plateforme est un outil d'aménagement linguistique.** Elle contribue à la planification de l'acquisition (Cooper 1989), au renforcement de la transmission intergénérationnelle et à la production de matériel d'enseignement, deux des facteurs de vitalité retenus par l'UNESCO (2003). Elle s'inscrit dans la continuité des travaux de l'ILA et du Projet École Intégrée en Côte d'Ivoire.

---

## 2. Ce que la recherche établit sur les langues pilotes

### 2.1 Dan (yacouba)

Source principale : Vydrin (2021), esquisse de grammaire du dan de l'Est, dialecte de Gouèta ; dictionnaire de Vydrin & Mongnan (2008).

| Domaine | Données publiées | Conséquence pour l'enseignement |
|---|---|---|
| Locuteurs | Environ 1 300 000 en Côte d'Ivoire ; départements de Biankouma, Sipilou et Man | Public potentiel large, diaspora importante |
| Normes | Gouèta (Santa) pour le nord-est ; Blo pour le sud-ouest | Le comité choisit une norme de référence par cours et signale les variantes |
| Voyelles | 12 orales, 9 nasales ; nasalité écrite par *-n* | Unité dédiée aux voyelles dès la bande 0 |
| Consonnes | Labio-vélaires *kp*, *gb* ; labialisées *kw*, *gw* ; implosives écrites *bh*, *dh* | Unité dédiée aux consonnes de la région |
| Tons | 5 tons ponctuels (extra-haut, haut, moyen, bas, extra-bas) et 3 tons modulés ; Vydrin illustre l'échelle par *ka̋a, káa, kāa, kàa, kȁa* | Entraînement perceptif progressif : deux tons très éloignés d'abord, puis les tons voisins |
| Ton grammatical | Le ton extra-bas marque l'aspect neutre du verbe et la tête d'une construction génitivale ; le pluriel et l'intensité des adjectifs passent par le ton | La piste « Sons et tons » rejoint la grammaire dès la bande 2 |
| Ordre des mots | Sujet – marque prédicative pronominale – objet – verbe – oblique | Exercices « Remets dans l'ordre » systématiques en bandes 1 et 2 |
| Pronoms | 10 séries de pronoms personnels ; marques prédicatives qui fusionnent la personne du sujet avec l'aspect, le mode et la polarité | Les marques prédicatives sont enseignées par paradigmes, en contexte |
| Possession | Noms relationnels (parenté, corps) sans connecteur ; noms libres avec le connecteur *bhȁ* ou *ȁ* | Deux unités séparées en bande 1 : famille/corps, puis objets possédés |
| Lieux | Noms locatifs avec déclinaison ; postpositions | Unité « Dans, sur, devant » en bande 2 |
| Formation des mots | Dérivation nominale (diminutif, agent, abstrait…), composition, préverbes, redoublement | Unités « Fabriquer des mots » et « Redoubler » |

### 2.2 Toura (wan)

Sources : Bearth (1968, 1971, 1983), Idiatov (2008, et son étude de l'orthographe toura dans *Mandenkan* 41).

- Environ 50 000 à 67 000 locuteurs selon les sources ; département de Biankouma, au nord-est de Man ; forte présence à Abidjan et Yamoussoukro.
- Dialectes : naò, boo, yiligele, gwéò, wáádú, guse.
- Quatre tons ponctuels (Bearth 1968). Orthographe pratique due à Thomas Bearth : haut ‹á›, mi-haut ‹â›, mi-bas non marqué, bas ‹à› ; enclitiques tonals notés après le mot ; nasalité par *-n*.
- La séparation ou la liaison des mots composés est une vraie difficulté orthographique ; Idiatov propose des critères explicites, à adopter ou adapter par le comité.
- Le toura partage l'architecture mandé-sud (ordre S–Aux–O–V–X, possession aliénable/inaliénable, postpositions) ; les détails propres au toura doivent être établis à partir de Bearth et Idiatov avant la rédaction des unités de grammaire.

### 2.3 Ce que les deux langues ont en commun

Le mandé-sud partage un ordre des constituants rigide S–Aux–O–V–X, des pronoms qui fusionnent la personne et l'aspect, une distinction aliénable/inaliénable, des postpositions, des idéophones, des constructions en chaîne et des marques de focalisation (Khachaturyan 2021 sur le mano ; Idiatov 2017). **Le même squelette de programme sert donc au dan et au toura**, et servira au gouro ; seul le contenu de chaque unité change.

---

## 3. Architecture : le pagne de la langue

Un pagne est fait de bandes étroites tissées puis cousues ensemble. Le programme suit cette image.

### 3.1 Six bandes, alignées sur le CECR

| Bande | Nom | Niveau | Intention |
|---|---|---|---|
| 0 | Ouvrir l'oreille | Pré-A1 | Entendre les tons, les voyelles, les consonnes ; lire l'alphabet ; saluer |
| 1 | Premiers pas | A1 | Famille, corps, nombres, possession, lieux, première phrase verbale, négation, questions |
| 2 | Dans la cour | A2 | Aspects (habitude, accompli, futur), postpositions, pluriel, dérivation, milieu, premiers proverbes |
| 3 | Raconter | B1 | Enchaînement, focalisation, subordination, discours rapporté, conte, idéophones, variation |
| 4 | La parole des anciens | B2 | Argumentation, proverbes en situation, paroles de cérémonie, métaphores, chants, contact de langues |
| 5 | Transmettre | C1 | Médiation, néologie, écriture suivie, enseignement aux enfants, documentation, contribution au comité |

La bande 5 referme la boucle : l'apprenant devenu compétent devient contributeur et alimente le comité. C'est le cœur du projet d'aménagement linguistique.

Le détail des 54 unités, avec objectif, pistes et tâche finale, est dans `content/curriculum/programme.json` et s'affiche dans l'application (écran « Programme »).

### 3.2 Huit pistes qui traversent toutes les bandes

| Piste | Disciplines | Ce qu'on y apprend |
|---|---|---|
| Sons et tons | Phonétique, phonologie, prosodie | Voyelles, consonnes, tons, mélodie de la phrase |
| Écriture | Orthographe, lecture | Alphabet officiel, notation des tons, découpage des mots |
| Mots | Lexicologie, morphologie | Vocabulaire par champs et fréquence, dérivation, composition, emprunts |
| Grammaire | Morphosyntaxe, syntaxe | Ordre des mots, marques prédicatives, pronoms, possession, phrase complexe |
| Sens | Sémantique | Polysémie, champs sémantiques, sens figuré, idéophones |
| Usage | Pragmatique, sociolinguistique | Politesse, adresse, registres, variation, contact de langues |
| Parole et récit | Analyse du discours, ethnopoétique | Dialogue, récit, conte, proverbe, chant |
| Culture et milieu | Anthropolinguistique, écolinguistique | Parenté, noms, agriculture, plantes, animaux, lieux, savoir-faire |

Chaque piste progresse en spirale : on revient aux mêmes domaines à chaque bande, avec plus de profondeur. Un tableau de bord permet de vérifier qu'aucune piste n'est délaissée.

---

## 4. L'unité type (15 à 20 minutes sur téléphone)

| Étape | Volet (Nation) | Contenu |
|---|---|---|
| 1. Écouter | Input centré sur le sens | Une courte situation, plusieurs voix |
| 2. Remarquer | Étude de la langue | Isoler un ton, une forme, une structure ; dégager la règle |
| 3. S'exercer | Étude de la langue | Exercices guidés, correction immédiate |
| 4. Dire | Production centrée sur le sens | S'enregistrer, se comparer à la référence |
| 5. Agir | Production centrée sur le sens | La tâche de communication de l'unité |
| 6. Fluidité | Fluidité | Rappel rapide de ce qui est déjà su, rien de nouveau |
| 7. Bilan | Consolidation | Le cauris se remplit ; les éléments entrent en révision espacée |

Règles de dosage : au moins 95 % de mots déjà connus dans les écoutes de l'étape 1, 100 % dans l'étape 6 (Nation 2007). Au plus 8 à 10 éléments nouveaux par unité.

---

## 5. Les 22 types d'exercices

La liste complète figure dans `programme.json` (champ `typesExercices`). Ils sont choisis pour couvrir chaque piste :

- **Sons et tons** : « Même ou différent ? » (paires minimales), « Quel ton ? », « Trois voix, un mot », « Répète et compare ».
- **Écriture** : « Dictée », « Lis à voix haute ».
- **Mots et sens** : « Écoute et choisis », « Quel sens ? », « Fabrique le mot », « Range les mots », « Au propre ou au figuré ? ».
- **Grammaire** : « Remets dans l'ordre », « Transforme », « Complète le tableau », « Démonte la phrase » (glose de Leipzig, bande 3 et plus).
- **Usage et parole** : « Que dirais-tu ? », « À toi de parler », « Écoute l'histoire », « Le bon proverbe », « Explique-le ».
- **Transversaux** : « Rappel éclair » (fluidité), « Propose au comité » (bande 5).

Aucun exercice ne repose sur la seule traduction mot à mot. La bonne réponse est signalée par le cauris qui se remplit, jamais par une coche verte (voir `CLAUDE.md`).

---

## 6. Évaluation et progression

- **Test de positionnement** à l'entrée, pour les apprenants qui ne partent pas de zéro (enfants de la diaspora, locuteurs passifs).
- **Contrôle d'unité** : la tâche finale de l'unité.
- **Examen de bande** : un parcours mêlant les huit pistes ; sa réussite ouvre la bande suivante et donne une parure.
- **Auto-évaluation « Je peux… »** à chaque bande, sur le modèle des descripteurs du CECR, y compris l'échelle de maîtrise phonologique du volume complémentaire.
- **Portfolio sonore** : l'apprenant garde ses enregistrements et entend ses progrès.
- **Révision espacée** : chaque élément appris revient à intervalles croissants, ajustés selon les erreurs.

---

## 7. Le circuit de la donnée

Six types de contenus, définis dans `content/schema/modele-de-donnees.schema.json` :

1. **Entrée lexicale** : forme écrite avec tons, transcription API, schéma tonal, catégorie (dont nom relationnel et nom locatif), pluriel, formes liées, sens, champ sémantique, registre, exemples glosés, enregistrements, note culturelle.
2. **Point de grammaire** : explication en français simple, règle, au moins deux exemples glosés, prérequis.
3. **Situation pragmatique** : qui parle à qui, ce qui se dit, ce qu'il faut éviter.
4. **Texte oral** : conte, proverbe, devinette, chant, récit, parole de cérémonie, avec contexte d'emploi et restrictions éventuelles.
5. **Fiche phonologique** : un son ou un ton, ses réalisations, ses paires minimales.
6. **Unité** : déjà décrite dans `programme.json`.

Règles du circuit :

- Statuts : brouillon → proposé → validé (ou rejeté, ou à revoir).
- **La validation est faite par un membre différent de celui qui a saisi.** C'est vérifié par la base de données elle-même, pas seulement par l'interface.
- Chaque enregistrement porte le consentement éclairé du locuteur, son pseudonyme, sa variété, et la façon dont il souhaite être crédité.
- Un texte réservé (savoir initiatique, parole qui ne se dit pas en public) est marqué et n'est jamais publié.
- Seuls les contenus validés sont copiés vers le site public, avec une copie sur l'ordinateur du projet.

---

## 8. Décisions qui reviennent au comité

1. **Norme de référence** pour le dan (gouèta, blo, ou deux cours parallèles) et pour le toura (dialecte de référence).
2. **Orthographe** : adoption formelle de l'alphabet officiel et des règles de découpage des mots (en s'appuyant sur Idiatov pour le toura).
3. **Corpus de fréquence** : il n'existe pas encore de liste de fréquence publiée pour le dan ou le toura ; le comité constituera une première liste pour ordonner le vocabulaire des bandes 1 et 2.
4. **Calibrage des niveaux** : les correspondances avec le CECR sont des objectifs ; elles seront ajustées après les premiers apprenants.
5. **Contenus culturels** : ce qui peut être enseigné publiquement, et ce qui ne le peut pas.
6. **Gouro** : même architecture, à ouvrir quand le comité dispose de contributeurs gouro.

---

## 9. Ce que MinWoo emprunte aux méthodes existantes, et ce qu'il fait autrement

| Modèle | Ce qu'on retient | Ce qu'on fait autrement |
|---|---|---|
| Méthodes audio à rappel espacé (Pimsleur 1967) | Audio d'abord, rappel à intervalles croissants | Plusieurs voix, et l'écrit arrive tôt car l'orthographe est un enjeu d'aménagement |
| Applications à micro-leçons | Séances courtes, progression visible, régularité | Pas de traduction mot à mot comme exercice principal ; contenus validés par des linguistes |
| Méthodes à phase passive puis active | Longue exposition avant la production | Production enregistrée dès la bande 0, pour les tons |
| Revitalisation par la transmission maître-apprenti (Hinton 2002) | La langue se transmet d'une personne à une autre, en situation | La bande 5 transforme l'apprenant en passeur et en contributeur |
| Documentation des langues (Himmelmann 1998) | Données primaires enregistrées, métadonnées, consentement | Ces données servent aussi directement l'enseignement |

---

## 10. Bibliographie

- Bearth, Thomas. 1968. *Étude instrumentale des tons du toura (Côte d'Ivoire)*.
- Bearth, Thomas. 1971. *L'énoncé toura (Côte d'Ivoire)*. Norman : Summer Institute of Linguistics.
- Bearth, Thomas. 1983. *Le toura : esquisse grammaticale*. Abidjan : SIL.
- Cepeda, N. J., et al. 2006. Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin* 132(3).
- Comrie, B., Haspelmath, M. & Bickel, B. 2008. *The Leipzig Glossing Rules*. Max Planck Institute for Evolutionary Anthropology.
- Conseil de l'Europe. 2001. *Cadre européen commun de référence pour les langues*.
- Conseil de l'Europe. 2020. *CECR — Volume complémentaire*.
- Cooper, Robert L. 1989. *Language Planning and Social Change*. Cambridge University Press.
- Halaoui, N., et al. 1983. *Atlas des langues mandé-sud de Côte d'Ivoire*. Abidjan : ILA / ACCT.
- Haugen, Einar. 1972. *The Ecology of Language*. Stanford University Press.
- Himmelmann, Nikolaus P. 1998. Documentary and descriptive linguistics. *Linguistics* 36.
- Hinton, Leanne. 2002. *How to Keep Your Language Alive: A Commonsense Approach to One-on-One Language Learning*. Heyday.
- Idiatov, Dmitry. 2008. *Dictionnaire toura-français*.
- Idiatov, Dmitry. La détermination des limites des mots : l'exemple de l'orthographe toura. *Mandenkan* 41.
- Idiatov, Dmitry. 2017. Mande languages. Introduction (prépublication HAL halshs-01481642).
- Khachaturyan, Maria. 2021. A typological portrait of Mano, Southern Mande. *Linguistic Typology*.
- Nation, Paul. 2007. The Four Strands. *Innovation in Language Learning and Teaching* 1(1), 2-13.
- Pimsleur, Paul. 1967. A memory schedule. *The Modern Language Journal* 51(2).
- Roediger, H. L. & Karpicke, J. D. 2006. Test-enhanced learning. *Psychological Science* 17(3).
- Sakai, M. & Moorman, C. 2018. Can perception training improve the production of second language phonemes? A meta-analytic review of 25 years of perception training research. *Applied Psycholinguistics* 39(1).
- UNESCO, groupe d'experts ad hoc. 2003. *Language Vitality and Endangerment*.
- Vydrin, Valentin. 2016. Tonal inflection in Mande languages: The cases of Bamana and Dan-Gwɛɛtaa. In *Tone and Inflection*.
- Vydrin, Valentin. 2021. Esquisse de grammaire du dan de l'Est (dialecte de Gouèta). *Mandenkan* 64, 3-80.
- Vydrin, Valentin & Mongnan, Alphonse. 2008. Dictionnaire dan-français (dan de l'Est), avec une esquisse de grammaire.
- Wang, Y., Spence, M. M., Jongman, A. & Sereno, J. A. 1999. Training American listeners to perceive Mandarin tones. *Journal of the Acoustical Society of America* 106(6).
