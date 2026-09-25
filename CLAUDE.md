# MinWoo — Règles de design

Ce fichier documente le système visuel de MinWoo pour que tout futur travail (code ou design) reste cohérent. À lire avant de créer un nouvel écran.

## Principe directeur

Habiller l'app des couleurs/matières des tenues traditionnelles ivoiriennes, avec élégance — jamais folklorique. Deux univers :
- **Pagne tissé indigo** — calme, concentration, usage quotidien (navigation, leçons, contenu)
- **Kita/kente** — célébration, énergie, récompense, réservé aux moments forts uniquement

**Règle de proportion stricte : 70% indigo/coton, 20% ivoire/raphia, 10% kita.** Le kita n'apparaît que lors des réussites (fin de leçon, badge, montée de niveau) — jamais comme couleur d'interface permanente.

## Ne jamais faire (leçon apprise, voir historique du projet)

Un premier jet de palette a été jugé "trop générique" par le fondateur car il reproduisait le gabarit SaaS par défaut : bleu = couleur principale, orange = CTA, vert = bonne réponse. **Ce gabarit est interdit ici.** Règles qui en découlent :
- L'indigo (`--encre`, `--indigo-tisse`) est un **neutre**, jamais "la couleur de marque".
- La **Braise** (`--braise`, `#B7431E`) est LA couleur signature — sobre, utilisée pour l'identité (logo, CTA, liens, focus), jamais diluée en la mélangeant à d'autres accents chauds sur un même écran.
- **Jamais de vert pour "bonne réponse"** (cliché Duolingo). Le feedback positif passe par le cauris qui se remplit d'or — un mécanisme, pas une couleur importée d'un concurrent.
- `--corail-alerte` (erreur) est une teinte volontairement différente de `--braise` pour ne jamais confondre "erreur" et "identité".

## Design tokens

Fichiers sources : `css/tokens.css` (couleurs, typographie, espacements, ombres, mouvement), `css/patterns.css` (motifs génératifs), `css/components.css` (composants de base).

Palette complète et mesures d'origine (photos de référence) : `references/analysis.md`.

**Ne jamais coder une couleur en dur** — toujours passer par les variables CSS (`var(--braise)`, etc.), y compris dans un nouveau composant.

## Typographie

- **Titres** : Fraunces (Google Fonts, variable) — courbes "wonky" qui évoquent le tissage sans jamais citer un motif littéral.
- **Texte courant, UI, contenu linguistique** : Noto Sans — choisie spécifiquement pour sa couverture Unicode quasi-totale (tons, voyelles ouvertes ɛ/ɔ, ŋ, diacritiques combinés). Ne jamais utiliser une autre police pour du contenu en langue Yacouba/Toura/Gouro sans vérifier sa couverture IPA au préalable.
- Clash Display et Space Grotesk ont été testés (voir `references/palette-preview.html`) mais écartés du système actif : couverture diacritique incertaine (Clash Display) et système à 2 familles suffisant pour la performance mobile visée.

## Motifs génératifs (jamais de photo)

- `.motif-tisse` — bandeau de rayures irrégulières, en-têtes/séparateurs, univers indigo quotidien.
- `.motif-grain` — grain textile léger en surimpression sur surfaces claires, très subtil par design.
- `.motif-kita` — damier, réservé aux célébrations.
- Chaque langue a son propre motif tissé de tuile (`.motif-yacouba`, `.motif-toura`, voir `app/index.html`) — variation de rayures colorées par langue, jamais une photo de pagne.

## Composants signature

- **Cauris** (`.cauris`) — monnaie de progression. Contour = à gagner, plein or = obtenu. Un cauris se remplit par leçon terminée.
- **Collier de perles** (`.collier`/`.perle`) — barre de progression d'un exercice, perles dorées qui s'enfilent au fil des réponses.
- **Damier kita** — animation de célébration fin de leçon/badge/niveau (< 2s, transform/opacity uniquement).

## Contraintes techniques

- Mobile-first, cible Android milieu de gamme + 3G/4G — pas de framework, CSS/SVG uniquement pour les motifs (aucune image de fond).
- Mode clair (coton) par défaut, mode sombre (indigo nuit) via `prefers-color-scheme` + override manuel `data-theme`.
- Animations en `transform`/`opacity` uniquement ; `prefers-reduced-motion` respecté globalement (voir `tokens.css`).
- Contraste WCAG AA : `--braise` et `--jaune-kita` ne servent jamais de texte fin sur fond clair — uniquement fond de bouton/badge avec texte blanc ou `--encre`.

## À éviter

Photos en fond, mélange de toutes les couleurs kita en même temps hors célébration, clichés "Afrique générique" (silhouettes savane, masques décoratifs, motifs tribaux inventés), dégradés violets, polices par défaut (Inter/Roboto) pour les titres.

## Écrans construits

1. **Accueil / choix de langue** (`app/index.html`) — tuiles tissées par langue, validé le 2026-09-25.
2. Parcours d'apprentissage — à construire.
3. Exercice — à construire.
4. Écran de réussite (moment signature kita) — à construire.
5. Profil (cauris, parures, série) — à construire.
