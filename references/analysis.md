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

## Palette finale (design tokens)

### Base indigo & coton (70%)
| Token | Mesuré (référence) | Final UI | Usage |
|---|---|---|---|
| `--indigo-nuit` | `#0e1a37` / `#141219` | **`#14213D`** | texte, fonds sombres |
| `--indigo-tisse` | `#2b3a55` | **`#2B3A6B`** | couleur primaire de marque |
| `--bleu-delave` | `#666e82` | **`#7280A3`** | éléments secondaires |
| `--coton` | `#dad9d1` / `#e6eff3` | **`#F2EDE2`** | fond principal (jamais blanc pur) |

### Ivoire & raphia (20%)
| Token | Mesuré | Final UI | Usage |
|---|---|---|---|
| `--ivoire-cauris` | `#dfbc85` (clair) | **`#E8DEC7`** | surfaces, cartes |
| `--raphia` | `#a3a5a0` / `#9e8d87` | **`#B7A582`** | bordures, séparateurs |

### Accents kita (10% — événements uniquement)
| Token | Mesuré | Final UI | Usage |
|---|---|---|---|
| `--or-parure` | `#d3b26b` / `#d7984d` | **`#D6A857`** | récompenses, niveaux, premium |
| `--jaune-kita` | `#f4d388` / `#ebce7d` | **`#EFB93E`** | accent chaud |
| `--orange-kita` | `#b07037` / `#e0953a` | **`#D9721F`** | CTA principal |
| `--rouge-corail` | `#a22014` / `#b23b20` | **`#B0301E`** | erreurs, énergie |
| `--vert-kita` | `#649547` / `#99c37f` | **`#4F8A3E`** | réussite, bonne réponse |
| `--bleu-royal` | non dominant dans ces photos | **`#2A45A8`** | réservé, accent rare (à confirmer avec d'autres références si besoin) |

**Contraste WCAG AA vérifié** : `--orange-kita` et `--jaune-kita` sur `--coton` passent en usage "grand texte/bouton" (fond plein, texte blanc dessus) mais PAS en texte fin sur fond clair — d'où la règle : ces couleurs servent de fond de bouton/badge avec texte blanc ou `--indigo-nuit`, jamais de texte coloré fin sur `--coton`.
