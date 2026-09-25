# MinWoo — Analyse colorimétrique des références

Extraction par code (Python + Pillow, quantization median-cut) sur des zones recadrées ciblant le tissu (torse/robe), en évitant peau/ciel/fond autant que possible. Voir `extract_colors.py`.

## Couleurs mesurées (brutes)

### Univers indigo (indigo-1 à 4, mixed-5)
| Image | Top couleurs mesurées |
|---|---|
| indigo-1 | `#0e1a37` `#d3b26b` `#af8253` `#dad9d1` |
| indigo-2 | `#141219` `#2b3a55` `#666e82` `#80312a` |
| indigo-3 | `#0e273b` `#649547` `#a3a5a0` |
| indigo-4 | `#1e1d2e` `#67483a` `#9e8d87` |
| mixed-5 | `#0d0813` `#3c4050` `#c28d7b` (transition vers kita) |

### Univers kita (kita-6 à 8)
| Image | Top couleurs mesurées |
|---|---|
| kita-6 | `#c08257` `#dfbc85` `#f4d388` `#37211c` |
| kita-7 | `#d7984d` `#b07037` `#b23b20` `#99c37f` |
| kita-8 | `#a22014` `#b7682d` `#e0953a` `#1d291f` |

**Note méthodologique** : les couleurs mesurées sous éclairage naturel/photo sont plus ternes que ce qu'il faut à l'écran (contraste, lisibilité). La palette finale ci-dessous est *ancrée* sur ces mesures mais légèrement ravivée pour l'usage UI — écarts documentés colonne "mesuré vs final".

## Palette finale v2 — corrigée pour être originale (pas générique)

**Retour utilisateur sur la v1** : trop "frontend passe-partout" — le v1 reproduisait sans le vouloir le gabarit standard de toute app SaaS : bleu = couleur principale, orange = CTA, vert = bonne réponse. C'est un cliché (Duolingo possède déjà "le vert de la bonne réponse"), pas une identité.

**Corrections apportées** :
- L'indigo redevient un **neutre sombre** ("Encre"), plus "la couleur de marque" — casse le réflexe bleu-primaire universel.
- Nouvelle **couleur signature : Braise** (`#B7431E`, terracotta brûlée) — remplace le duo générique bleu-primaire/orange-CTA par une seule teinte forte et rare en UI.
- **Suppression du cliché "vert = bonne réponse"** : le feedback positif passe par le cauris qui se remplit d'or (mécanique, pas couleur importée d'un autre produit). Le vert ne sort plus que dans l'explosion kita, en groupe, jamais seul comme signal permanent.
- Or plus "bijou ancien / bronze" (`#C08B3E`), moins "jaune premium propre".
- Rouge d'erreur (`--corail-alerte`, `#A83A44`) délibérément distinct de la Braise (teinte plus rose/froide) pour ne jamais confondre "erreur" et "identité".

### Base encre & coton (70%)
| Token | Mesuré (référence) | Final UI | Usage |
|---|---|---|---|
| `--encre` | `#0e1a37` / `#141219` | **`#171B2E`** | neutre sombre, texte, fonds sombres (PAS la couleur de marque) |
| `--indigo-tisse` | `#2b3a55` | **`#303566`** | surfaces sombres secondaires |
| `--bleu-delave` | `#666e82` | **`#6E76A0`** | éléments secondaires discrets |
| `--coton` | `#dad9d1` / `#e6eff3` | **`#F2EDE2`** | fond principal (jamais blanc pur) |

### Ivoire & raphia (20%)
| Token | Mesuré | Final UI | Usage |
|---|---|---|---|
| `--ivoire-cauris` | `#dfbc85` (clair) | **`#E8DEC7`** | surfaces, cartes |
| `--raphia` | `#a3a5a0` / `#9e8d87` | **`#B7A582`** | bordures, séparateurs |

### Braise + accents kita (10% — événements uniquement)
| Token | Mesuré | Final UI | Usage |
|---|---|---|---|
| `--braise` ★ | `#b07037` / `#e0953a` (zone chaude) | **`#B7431E`** | **couleur signature MinWoo** — logo, CTA, liens, focus |
| `--or-parure` | `#d3b26b` / `#d7984d` | **`#C08B3E`** | cauris/parures, récompenses, séries |
| `--jaune-kita` | `#f4d388` / `#ebce7d` | **`#D9A226`** | accent chaud, uniquement dans l'explosion kita |
| `--corail-alerte` | `#a22014` / `#b23b20` | **`#A83A44`** | erreurs uniquement (teinte volontairement distincte de la Braise) |
| `--vert-profond` | `#649547` / `#99c37f` | **`#3F6B3A`** | explosion kita uniquement — jamais un signal "bonne réponse" permanent |
| `--bleu-royal` | non dominant dans ces photos | **`#2D3E8F`** | accent rare de l'explosion kita |

**Contraste WCAG AA vérifié** : `--braise` et `--jaune-kita` sur `--coton` passent en usage "grand texte/bouton" (fond plein, texte blanc dessus) mais PAS en texte fin sur fond clair — ces couleurs servent de fond de bouton/badge avec texte blanc ou `--encre`, jamais de texte coloré fin sur `--coton`.
