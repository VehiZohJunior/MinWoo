import json, html, pathlib

ROOT = pathlib.Path(r"C:\Users\PC MARKET CI\Desktop\DOSSIER CODAGE\MinWoo")
prog = json.loads((ROOT / "content/curriculum/programme.json").read_text(encoding="utf-8"))
E = html.escape
noms_pistes = {p["id"]: p["nom"] for p in prog["pistes"]}

principes = [
    ("L'apprenant agit dans une situation réelle", "Chaque unité aboutit à une tâche de communication (saluer un aîné, acheter au marché, raconter un conte), selon l'approche actionnelle du CECR."),
    ("Quatre volets équilibrés", "Écoute centrée sur le sens, production centrée sur le sens, étude explicite de la langue et fluidité, en proportions voisines (Nation 2007). L'étude explicite ne dépasse pas un quart du temps."),
    ("L'oreille d'abord", "On entend avant de parler, et on entend plusieurs voix : l'entraînement perceptif à voix multiples améliore la perception des tons chez l'adulte et se transfère en partie à la production (Wang et al. 1999 ; Sakai & Moorman 2018). D'où trois enregistrements par mot, par des locuteurs différents."),
    ("Le ton fait partie du mot dès le premier jour", "En dan, le ton distingue les mots et porte une partie de la grammaire (Vydrin 2021). Il n'est jamais présenté comme un détail réservé aux avancés."),
    ("La grammaire se découvre avant de s'expliquer", "L'apprenant observe des exemples, remarque la régularité, puis reçoit l'explication en français simple."),
    ("On se souvient de ce qu'on rappelle", "Révision espacée et rappel actif plutôt que relecture (Pimsleur 1967 ; Roediger & Karpicke 2006 ; Cepeda et al. 2006)."),
    ("La langue vit dans une société", "Variation dialectale, registres, âge et statut des interlocuteurs, contact avec le français et le dioula sont enseignés, pas gommés."),
    ("La langue est la mémoire d'un milieu", "Parenté, calendrier agricole, plantes, animaux, lieux et savoir-faire sont des contenus à part entière (Haugen 1972, écologie des langues)."),
    ("Rien sans source ni validation", "Chaque donnée porte sa source, son locuteur, son consentement, et la validation d'un second membre du comité. Exemples présentés selon les règles de glose de Leipzig."),
    ("Un outil d'aménagement linguistique", "La plateforme contribue à la planification de l'acquisition (Cooper 1989), à la transmission intergénérationnelle et au matériel d'enseignement, deux facteurs de vitalité retenus par l'UNESCO (2003), dans la continuité de l'ILA et du Projet École Intégrée."),
]

dan_rows = [
    ("Locuteurs", "Environ 1 300 000 en Côte d'Ivoire ; Biankouma, Sipilou, Man", "Public large, diaspora importante"),
    ("Normes", "Gouèta (Santa) pour le nord-est ; Blo pour le sud-ouest", "Une norme de référence par cours, variantes signalées"),
    ("Voyelles", "12 orales, 9 nasales ; nasalité écrite par -n", "Unité dédiée dès la bande 0"),
    ("Consonnes", "Labio-vélaires kp, gb ; labialisées kw, gw ; implosives bh, dh", "Unité dédiée aux consonnes de la région"),
    ("Tons", "5 tons ponctuels et 3 tons modulés ; échelle illustrée par Vydrin : ka̋a, káa, kāa, kàa, kȁa", "Perception progressive : tons éloignés d'abord, puis tons voisins"),
    ("Ton grammatical", "Extra-bas : aspect neutre du verbe, tête de construction génitivale ; pluriel et intensité des adjectifs par le ton", "Les tons rejoignent la grammaire dès la bande 2"),
    ("Ordre des mots", "Sujet – marque prédicative pronominale – objet – verbe – oblique", "Exercices « Remets dans l'ordre » en bandes 1 et 2"),
    ("Pronoms", "10 séries ; marques prédicatives fusionnant personne, aspect, mode et polarité", "Enseignées par paradigmes, en contexte"),
    ("Possession", "Noms relationnels sans connecteur ; noms libres avec bhȁ ou ȁ", "Deux unités : famille et corps, puis objets possédés"),
    ("Lieux", "Noms locatifs avec déclinaison ; postpositions", "Unité « Dans, sur, devant »"),
    ("Formation des mots", "Dérivation, composition, préverbes, redoublement", "Unités « Fabriquer des mots » et « Redoubler »"),
]

toura_points = [
    "Environ 50 000 à 67 000 locuteurs selon les sources ; département de Biankouma, au nord-est de Man ; forte présence à Abidjan et Yamoussoukro.",
    "Dialectes : naò, boo, yiligele, gwéò, wáádú, guse.",
    "Quatre tons ponctuels (Bearth 1968). Orthographe pratique de Thomas Bearth : haut ‹á›, mi-haut ‹â›, mi-bas non marqué, bas ‹à› ; enclitiques tonals notés après le mot ; nasalité par -n.",
    "Séparer ou lier les mots composés est une vraie difficulté orthographique ; Idiatov propose des critères explicites, à adopter ou adapter par le comité.",
    "Même architecture mandé-sud que le dan ; les détails propres au toura sont à établir à partir de Bearth (1971, 1983) et Idiatov (2008) avant la rédaction des unités de grammaire.",
]

contenus = [
    ("Entrée lexicale", "Forme écrite avec tons, API, schéma tonal, catégorie (dont nom relationnel et nom locatif), pluriel, formes liées, sens, champ sémantique, registre, exemples glosés, enregistrements, note culturelle."),
    ("Point de grammaire", "Explication en français simple, règle, au moins deux exemples glosés, prérequis."),
    ("Situation pragmatique", "Qui parle à qui, ce qui se dit, ce qu'il faut éviter."),
    ("Texte oral", "Conte, proverbe, devinette, chant, récit, parole de cérémonie, avec contexte d'emploi et restrictions éventuelles."),
    ("Fiche phonologique", "Un son ou un ton, ses réalisations, ses paires minimales."),
    ("Unité", "Objectif, pistes, tâche finale, éléments liés : déjà définie dans le programme."),
]

decisions = [
    ("Norme de référence", "Pour le dan : gouèta, blo, ou deux cours parallèles. Pour le toura : le dialecte de référence."),
    ("Orthographe", "Adoption formelle de l'alphabet officiel et des règles de découpage des mots, en s'appuyant sur Idiatov pour le toura."),
    ("Liste de fréquence", "Il n'existe pas encore de liste de fréquence publiée pour le dan ou le toura : le comité constitue une première liste pour ordonner le vocabulaire des bandes 1 et 2."),
    ("Calibrage des niveaux", "Les correspondances avec le CECR sont des objectifs, ajustées après les premiers apprenants."),
    ("Contenus culturels", "Ce qui peut être enseigné publiquement, et ce qui ne le peut pas."),
    ("Gouro", "Même architecture, à ouvrir quand le comité dispose de contributeurs gouro."),
]

methodes = [
    ("Méthodes audio à rappel espacé (Pimsleur 1967)", "Audio d'abord, rappel à intervalles croissants", "Plusieurs voix ; l'écrit arrive tôt car l'orthographe est un enjeu d'aménagement"),
    ("Applications à micro-leçons", "Séances courtes, progression visible, régularité", "Pas de traduction mot à mot comme exercice principal ; contenus validés par des linguistes"),
    ("Méthodes à phase passive puis active", "Longue exposition avant la production", "Production enregistrée dès la bande 0, pour les tons"),
    ("Transmission maître-apprenti (Hinton 2002)", "La langue se transmet de personne à personne, en situation", "La bande 5 fait de l'apprenant un passeur et un contributeur"),
    ("Documentation des langues (Himmelmann 1998)", "Données primaires enregistrées, métadonnées, consentement", "Ces données servent aussi directement l'enseignement"),
]

biblio = [
    "Bearth, Thomas. 1968. <i>Étude instrumentale des tons du toura (Côte d'Ivoire)</i>.",
    "Bearth, Thomas. 1971. <i>L'énoncé toura (Côte d'Ivoire)</i>. Norman : Summer Institute of Linguistics.",
    "Bearth, Thomas. 1983. <i>Le toura : esquisse grammaticale</i>. Abidjan : SIL.",
    "Cepeda, N. J., et al. 2006. Distributed practice in verbal recall tasks. <i>Psychological Bulletin</i> 132(3).",
    "Comrie, B., Haspelmath, M. &amp; Bickel, B. 2008. <i>The Leipzig Glossing Rules</i>.",
    "Conseil de l'Europe. 2001. <i>Cadre européen commun de référence pour les langues</i> ; 2020. <i>Volume complémentaire</i>.",
    "Cooper, Robert L. 1989. <i>Language Planning and Social Change</i>. Cambridge University Press.",
    "Halaoui, N., et al. 1983. <i>Atlas des langues mandé-sud de Côte d'Ivoire</i>. Abidjan : ILA / ACCT.",
    "Haugen, Einar. 1972. <i>The Ecology of Language</i>. Stanford University Press.",
    "Himmelmann, Nikolaus P. 1998. Documentary and descriptive linguistics. <i>Linguistics</i> 36.",
    "Hinton, Leanne. 2002. <i>How to Keep Your Language Alive</i>. Heyday.",
    "Idiatov, Dmitry. 2008. <i>Dictionnaire toura-français</i>.",
    "Idiatov, Dmitry. La détermination des limites des mots : l'exemple de l'orthographe toura. <i>Mandenkan</i> 41.",
    "Idiatov, Dmitry. 2017. Mande languages. Introduction (HAL halshs-01481642).",
    "Khachaturyan, Maria. 2021. A typological portrait of Mano, Southern Mande. <i>Linguistic Typology</i>.",
    "Nation, Paul. 2007. The Four Strands. <i>Innovation in Language Learning and Teaching</i> 1(1), 2-13.",
    "Pimsleur, Paul. 1967. A memory schedule. <i>The Modern Language Journal</i> 51(2).",
    "Roediger, H. L. &amp; Karpicke, J. D. 2006. Test-enhanced learning. <i>Psychological Science</i> 17(3).",
    "Sakai, M. &amp; Moorman, C. 2018. Can perception training improve the production of second language phonemes? <i>Applied Psycholinguistics</i> 39(1).",
    "UNESCO, groupe d'experts ad hoc. 2003. <i>Language Vitality and Endangerment</i>.",
    "Vydrin, Valentin. 2016. Tonal inflection in Mande languages: The cases of Bamana and Dan-Gwɛɛtaa. <i>Tone and Inflection</i>.",
    "Vydrin, Valentin. 2021. Esquisse de grammaire du dan de l'Est (dialecte de Gouèta). <i>Mandenkan</i> 64, 3-80.",
    "Vydrin, Valentin &amp; Mongnan, Alphonse. 2008. Dictionnaire dan-français (dan de l'Est), avec une esquisse de grammaire.",
    "Wang, Y., Spence, M. M., Jongman, A. &amp; Sereno, J. A. 1999. Training American listeners to perceive Mandarin tones. <i>JASA</i> 106(6).",
]

def bandes_html():
    out = []
    for b in prog["bandes"]:
        unites = []
        for j, u in enumerate(b["unites"], 1):
            pastilles = "".join(f'<span class="piste">{E(noms_pistes[p])}</span>' for p in u["pistes"])
            unites.append(
                f'<li><span class="num">{b["numero"]}.{j}</span><div class="u-corps">'
                f'<b>{E(u["titre"])}</b><span class="obj">{E(u["objectif"])}</span>'
                f'<span class="tache"><em>Tâche</em> {E(u["tache"])}</span><span class="pistes">{pastilles}</span></div></li>'
            )
        jp = "".join(f"<li>{E(t)}</li>" for t in b["jePeux"])
        out.append(f'''
<details class="bande" id="bande-{b["numero"]}">
  <summary>
    <span class="tissage t-{b["id"]}"></span>
    <span class="tete"><span class="bnum">{b["numero"]}</span><span class="bnom">{E(b["nom"])}</span><span class="cecr">{E(b["cecr"])}</span><span class="nb">{len(b["unites"])} unités</span></span>
    <span class="intention">{E(b["intention"])}</span>
  </summary>
  <div class="bande-corps">
    <div class="jepeux"><span class="etiquette">À la fin de la bande, l'apprenant peut…</span><ul>{jp}</ul></div>
    <ol class="unites">{"".join(unites)}</ol>
  </div>
</details>''')
    return "\n".join(out)

pistes_html = "".join(
    f'<div class="piste-carte"><span class="code">{E(p["code"])}</span><div><b>{E(p["nom"])}</b>'
    f'<span class="disc">{E(" · ".join(p["disciplines"]))}</span><p>{E(p["description"])}</p></div></div>'
    for p in prog["pistes"]
)
cycle_html = "".join(
    f'<li><span class="rond">{e["etape"]}</span><div><b>{E(e["nom"])}</b><span class="volet">{E(e["volet"])}</span><p>{E(e["description"])}</p></div></li>'
    for e in prog["cycleUnite"]
)
exos_par_piste = {}
for t in prog["typesExercices"]:
    exos_par_piste.setdefault(t["pistes"][0], []).append(t)
exos_html = "".join(
    f'<tr><td>{E(t["nom"])}</td><td>{E(", ".join(noms_pistes[p] for p in t["pistes"]))}</td><td>{"oui" if t["audio"] else "non"}</td><td>{E(t["description"])}</td></tr>'
    for t in prog["typesExercices"]
)
principes_html = "".join(f"<li><b>{E(t)}.</b> {E(d)}</li>" for t, d in principes)
dan_html = "".join(f"<tr><th scope='row'>{E(a)}</th><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in dan_rows)
toura_html = "".join(f"<li>{E(t)}</li>" for t in toura_points)
contenus_html = "".join(f"<li><b>{E(t)}</b> {E(d)}</li>" for t, d in contenus)
decisions_html = "".join(f'<li><span class="dn">{i}</span><div><b>{E(t)}</b><p>{E(d)}</p></div></li>' for i, (t, d) in enumerate(decisions, 1))
methodes_html = "".join(f"<tr><th scope='row'>{E(a)}</th><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in methodes)
biblio_html = "".join(f"<li>{b}</li>" for b in biblio)
nb_unites = sum(len(b["unites"]) for b in prog["bandes"])

page = f'''<title>Référentiel MinWoo</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Noto+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap">
<style>
/* Mise en page : une colonne de lecture large, bandes tissées comme repères ; tokens repris du système de design MinWoo */
:root {{
  --encre: #171B2E; --indigo-tisse: #303566; --bleu-delave: #6E76A0; --coton: #F2EDE2;
  --ivoire: #E8DEC7; --raphia: #B7A582; --braise: #B7431E; --or: #C08B3E;
  --bg: var(--coton); --surface: var(--ivoire); --surface-2: #FBF8F1; --texte: var(--encre);
  --texte-att: #555C80; --bordure: #D3C6A8; --accent: var(--braise); --accent-texte: #9A3717;
  --f-titre: 'Fraunces', Georgia, serif; --f-texte: 'Noto Sans', 'Segoe UI', Arial, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #12152A; --surface: #23274A; --surface-2: #1B1F3A; --texte: #F2EDE2;
  --texte-att: #A6ADD2; --bordure: #3A3F6A; --accent: #D9693F; --accent-texte: #E8825A; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #12152A; --surface: #23274A; --surface-2: #1B1F3A; --texte: #F2EDE2;
  --texte-att: #A6ADD2; --bordure: #3A3F6A; --accent: #D9693F; --accent-texte: #E8825A; color-scheme: dark; }}

body {{ background: var(--bg); color: var(--texte); font-family: var(--f-texte); font-size: 16px; line-height: 1.65; }}
.bandeau {{ height: 10px; background: repeating-linear-gradient(100deg, var(--encre) 0 22px, var(--coton) 22px 28px, var(--indigo-tisse) 28px 40px, var(--coton) 40px 44px, var(--encre) 44px 70px, var(--or) 70px 76px, var(--indigo-tisse) 76px 96px, var(--coton) 96px 100px); }}
.page {{ max-width: 860px; margin: 0 auto; padding-block: 40px 80px; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: flex; flex-direction: column; gap: 56px; }}
h1, h2, h3 {{ font-family: var(--f-titre); text-wrap: balance; line-height: 1.2; margin: 0; }}
h1 {{ font-size: clamp(1.9rem, 5vw, 2.7rem); font-weight: 700; }}
h2 {{ font-size: clamp(1.4rem, 3.4vw, 1.8rem); font-weight: 600; }}
h3 {{ font-size: 1.15rem; font-weight: 600; }}
p {{ margin: 0; }}
.etiquette {{ font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--texte-att); }}
section {{ display: flex; flex-direction: column; gap: 18px; }}
section > p, .lecture {{ max-width: 66ch; }}
a {{ color: var(--accent-texte); }}
a:focus-visible, summary:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 3px; border-radius: 6px; }}

.entete {{ display: flex; flex-direction: column; gap: 16px; }}
.chapo {{ font-size: 1.12rem; max-width: 62ch; }}
.chiffres {{ display: flex; flex-wrap: wrap; gap: 10px 28px; font-size: 0.95rem; color: var(--texte-att); }}
.chiffres b {{ font-family: var(--f-titre); font-size: 1.5rem; color: var(--texte); margin-right: 6px; font-variant-numeric: tabular-nums; }}
.appel {{ border-left: 4px solid var(--accent); background: var(--surface-2); padding: 16px 20px; border-radius: 0 10px 10px 0; display: flex; flex-direction: column; gap: 6px; max-width: 66ch; }}
.liens {{ display: flex; flex-wrap: wrap; gap: 10px 20px; font-size: 0.95rem; }}

nav.sommaire ol {{ margin: 0; padding: 0; list-style: none; display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 6px 24px; }}
nav.sommaire li {{ counter-increment: s; }}
nav.sommaire a {{ text-decoration: none; color: var(--texte); border-bottom: 1px solid var(--bordure); display: block; padding: 6px 0; }}
nav.sommaire a::before {{ content: counter(s) ". "; color: var(--texte-att); font-variant-numeric: tabular-nums; }}
nav.sommaire a:hover {{ color: var(--accent-texte); }}

ol.principes {{ margin: 0; padding-left: 1.4em; display: flex; flex-direction: column; gap: 10px; max-width: 70ch; }}
ol.principes li::marker {{ font-family: var(--f-titre); font-weight: 700; color: var(--accent-texte); }}

.tableau {{ overflow-x: auto; border: 1px solid var(--bordure); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; min-width: 560px; font-size: 0.92rem; }}
th, td {{ text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid var(--bordure); }}
thead th {{ background: var(--surface); font-size: 0.78rem; letter-spacing: 0.05em; text-transform: uppercase; color: var(--texte-att); }}
tbody th {{ font-weight: 700; white-space: nowrap; }}
tr:last-child th, tr:last-child td {{ border-bottom: 0; }}
.source {{ font-size: 0.85rem; color: var(--texte-att); font-style: italic; }}
ul.points {{ margin: 0; padding-left: 1.2em; display: flex; flex-direction: column; gap: 8px; max-width: 70ch; }}

.bande {{ border: 1px solid var(--bordure); border-radius: 12px; overflow: hidden; background: var(--surface-2); }}
.bande + .bande {{ margin-top: 12px; }}
.bande summary {{ list-style: none; cursor: pointer; display: flex; flex-direction: column; gap: 10px; padding-bottom: 16px; }}
.bande summary::-webkit-details-marker {{ display: none; }}
.tissage {{ display: block; height: 18px; }}
.tete {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 14px; padding: 0 18px; }}
.bnum {{ font-family: var(--f-titre); font-weight: 700; font-size: 1.4rem; color: var(--texte-att); font-variant-numeric: tabular-nums; }}
.bnom {{ font-family: var(--f-titre); font-weight: 600; font-size: 1.25rem; }}
.cecr {{ font-size: 0.78rem; font-weight: 700; border: 1px solid var(--bordure); border-radius: 999px; padding: 1px 10px; }}
.nb {{ font-size: 0.85rem; color: var(--texte-att); margin-left: auto; }}
.nb::after {{ content: " ▸"; }}
.bande[open] .nb::after {{ content: " ▾"; }}
.intention {{ padding: 0 18px; color: var(--texte-att); max-width: 70ch; }}
.bande-corps {{ padding: 0 18px 18px; display: flex; flex-direction: column; gap: 16px; }}
.jepeux {{ background: var(--surface); border-radius: 10px; padding: 12px 16px; }}
.jepeux ul {{ margin: 6px 0 0; padding-left: 1.2em; }}
ol.unites {{ list-style: none; margin: 0; padding: 0; }}
ol.unites li {{ display: flex; gap: 12px; padding: 12px 0; border-top: 1px solid var(--bordure); }}
.num {{ font-variant-numeric: tabular-nums; color: var(--texte-att); font-size: 0.85rem; min-width: 2.4em; padding-top: 2px; }}
.u-corps {{ display: flex; flex-direction: column; gap: 3px; min-width: 0; }}
.obj {{ color: var(--texte-att); font-size: 0.93rem; }}
.tache {{ font-size: 0.88rem; }}
.tache em {{ font-style: normal; font-weight: 700; margin-right: 4px; }}
.pistes {{ display: flex; flex-wrap: wrap; gap: 4px; margin-top: 4px; }}
.piste {{ font-size: 0.72rem; font-weight: 700; padding: 1px 8px; border-radius: 999px; border: 1px solid var(--bordure); }}

.t-b0 {{ background: repeating-linear-gradient(90deg, var(--raphia) 0 10px, var(--coton) 10px 14px, var(--ivoire) 14px 30px, var(--coton) 30px 34px); }}
.t-b1 {{ background: repeating-linear-gradient(90deg, var(--indigo-tisse) 0 18px, var(--coton) 18px 22px, var(--bleu-delave) 22px 28px, var(--coton) 28px 32px); }}
.t-b2 {{ background: repeating-linear-gradient(90deg, var(--encre) 0 16px, var(--coton) 16px 20px, var(--or) 20px 24px, var(--coton) 24px 28px, var(--indigo-tisse) 28px 40px, var(--coton) 40px 44px); }}
.t-b3 {{ background: repeating-linear-gradient(90deg, var(--indigo-tisse) 0 20px, var(--coton) 20px 23px, var(--encre) 23px 33px, var(--braise) 33px 36px, var(--coton) 36px 39px); }}
.t-b4 {{ background: repeating-linear-gradient(90deg, var(--encre) 0 12px, var(--or) 12px 18px, var(--encre) 18px 30px, var(--coton) 30px 33px, var(--or) 33px 36px, var(--coton) 36px 39px); }}
.t-b5 {{ background: repeating-linear-gradient(90deg, var(--braise) 0 14px, var(--encre) 14px 18px, var(--or) 18px 22px, var(--encre) 22px 26px, var(--braise) 26px 40px, var(--coton) 40px 43px); }}

.grille-pistes {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }}
.piste-carte {{ display: flex; gap: 12px; padding: 14px 16px; border: 1px solid var(--bordure); border-radius: 10px; }}
.piste-carte .code {{ font-family: var(--f-titre); font-weight: 700; color: var(--accent-texte); min-width: 1.8em; }}
.piste-carte div {{ display: flex; flex-direction: column; gap: 4px; min-width: 0; }}
.disc {{ font-size: 0.8rem; color: var(--texte-att); }}
.piste-carte p {{ font-size: 0.9rem; }}

ol.cycle {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; }}
ol.cycle li {{ display: flex; gap: 14px; padding: 12px 0; border-top: 1px solid var(--bordure); }}
.rond {{ width: 30px; height: 30px; border-radius: 50%; border: 2px solid var(--or); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; }}
ol.cycle li div {{ display: flex; flex-direction: column; gap: 2px; }}
.volet {{ font-size: 0.8rem; color: var(--texte-att); }}
.regle {{ font-size: 0.93rem; }}

ol.decisions {{ list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 12px; }}
ol.decisions li {{ display: flex; gap: 12px; padding: 16px; background: var(--surface); border-radius: 10px; }}
.dn {{ font-family: var(--f-titre); font-weight: 700; font-size: 1.4rem; color: var(--accent-texte); line-height: 1; }}
ol.decisions li div {{ display: flex; flex-direction: column; gap: 4px; }}
ol.decisions p {{ font-size: 0.92rem; }}

ol.biblio {{ margin: 0; padding-left: 0; list-style: none; display: flex; flex-direction: column; gap: 6px; font-size: 0.9rem; max-width: 75ch; }}
ol.biblio li {{ padding-left: 1.6em; text-indent: -1.6em; }}
footer {{ font-size: 0.85rem; color: var(--texte-att); border-top: 1px solid var(--bordure); padding-top: 18px; }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}
</style>

<div class="bandeau" aria-hidden="true"></div>
<main class="page">

<header class="entete">
  <span class="etiquette">MinWoo · Comité scientifique · Document de travail v1.0 · 21 novembre 2026</span>
  <h1>Référentiel pédagogique et linguistique</h1>
  <p class="chapo">Comment un débutant complet progresse, en dan ou en toura, depuis la toute première écoute jusqu'à pouvoir transmettre la langue à son tour. Ce document fixe l'architecture ; les mots, phrases et enregistrements viendront exclusivement du comité, après double validation.</p>
  <p class="chiffres"><span><b>6</b>bandes</span><span><b>{nb_unites}</b>unités</span><span><b>8</b>pistes</span><span><b>{len(prog["typesExercices"])}</b>types d'exercices</span><span><b>Pré-A1 → C1</b></span></p>
  <div class="appel">
    <b>Ce que nous attendons du comité</b>
    <p>Relire l'architecture, puis trancher les six décisions de la section 8. Aucune donnée de langue n'a été inventée : les seules formes citées proviennent de publications, avec leur référence.</p>
  </div>
  <p class="liens"><a href="https://vehizohjunior.github.io/MinWoo/app/programme.html">Voir le programme dans l'application</a><a href="https://vehizohjunior.github.io/MinWoo/app/">Ouvrir l'application MinWoo</a></p>
</header>

<nav class="sommaire" aria-label="Sommaire">
  <ol>
    <li><a href="#principes">Dix principes</a></li>
    <li><a href="#langues">Ce que la recherche établit</a></li>
    <li><a href="#bandes">Six bandes, 54 unités</a></li>
    <li><a href="#pistes">Huit pistes</a></li>
    <li><a href="#unite">L'unité type</a></li>
    <li><a href="#exercices">Types d'exercices</a></li>
    <li><a href="#donnees">Évaluation et données</a></li>
    <li><a href="#decisions">Décisions du comité</a></li>
    <li><a href="#methodes">Méthodes existantes</a></li>
    <li><a href="#bibliographie">Bibliographie</a></li>
  </ol>
</nav>

<section id="principes">
  <h2>1. Dix principes</h2>
  <ol class="principes">{principes_html}</ol>
</section>

<section id="langues">
  <h2>2. Ce que la recherche établit sur les langues pilotes</h2>
  <h3>Dan (yacouba)</h3>
  <p class="source">Vydrin (2021), esquisse de grammaire du dan de l'Est, dialecte de Gouèta ; Vydrin &amp; Mongnan (2008).</p>
  <div class="tableau"><table>
    <thead><tr><th scope="col">Domaine</th><th scope="col">Données publiées</th><th scope="col">Conséquence pour l'enseignement</th></tr></thead>
    <tbody>{dan_html}</tbody>
  </table></div>
  <h3>Toura (wan)</h3>
  <p class="source">Bearth (1968, 1971, 1983) ; Idiatov (2008 ; <i>Mandenkan</i> 41).</p>
  <ul class="points">{toura_html}</ul>
  <h3>Ce que les deux langues ont en commun</h3>
  <p>Le mandé-sud partage un ordre des constituants rigide S–Aux–O–V–X, des pronoms qui fusionnent la personne et l'aspect, une distinction aliénable/inaliénable, des postpositions, des idéophones, des constructions en chaîne et des marques de focalisation (Khachaturyan 2021 ; Idiatov 2017). Le même squelette de programme sert donc au dan et au toura, et servira au gouro ; seul le contenu de chaque unité change.</p>
</section>

<section id="bandes">
  <h2>3. Le pagne de la langue : six bandes, {nb_unites} unités</h2>
  <p>Un pagne est fait de bandes étroites tissées puis cousues ensemble. Chaque bande correspond à un niveau du CECR ; la dernière fait de l'apprenant un passeur et un contributeur du comité. Ouvrez une bande pour voir ses unités.</p>
  <div>{bandes_html()}</div>
</section>

<section id="pistes">
  <h2>4. Huit pistes qui traversent toutes les bandes</h2>
  <p>Une piste par grande branche de la linguistique. Chacune progresse en spirale : on revient aux mêmes domaines à chaque bande, avec plus de profondeur.</p>
  <div class="grille-pistes">{pistes_html}</div>
</section>

<section id="unite">
  <h2>5. L'unité type, 15 à 20 minutes sur téléphone</h2>
  <ol class="cycle">{cycle_html}</ol>
  <p class="regle">Dosage : au moins 95 % de mots déjà connus dans les écoutes de l'étape 1, 100 % dans l'étape 6 (Nation 2007). Au plus 8 à 10 éléments nouveaux par unité.</p>
</section>

<section id="exercices">
  <h2>6. Les {len(prog["typesExercices"])} types d'exercices</h2>
  <p>Aucun exercice ne repose sur la seule traduction mot à mot. La bonne réponse est signalée par le cauris qui se remplit d'or.</p>
  <div class="tableau"><table>
    <thead><tr><th scope="col">Exercice</th><th scope="col">Pistes</th><th scope="col">Audio</th><th scope="col">Principe</th></tr></thead>
    <tbody>{exos_html}</tbody>
  </table></div>
</section>

<section id="donnees">
  <h2>7. Évaluation, et circuit de la donnée</h2>
  <h3>Évaluer la progression</h3>
  <ul class="points">
    <li><b>Test de positionnement</b> pour les apprenants qui ne partent pas de zéro (enfants de la diaspora, locuteurs passifs).</li>
    <li><b>Contrôle d'unité</b> : la tâche finale de l'unité.</li>
    <li><b>Examen de bande</b> mêlant les huit pistes ; sa réussite ouvre la bande suivante et donne une parure.</li>
    <li><b>Auto-évaluation « Je peux… »</b> sur le modèle du CECR, y compris l'échelle de maîtrise phonologique du volume complémentaire.</li>
    <li><b>Portfolio sonore</b> : l'apprenant garde ses enregistrements et entend ses progrès.</li>
    <li><b>Révision espacée</b> : chaque élément revient à intervalles croissants, ajustés selon les erreurs.</li>
  </ul>
  <h3>Six types de contenus fournis par le comité</h3>
  <ul class="points">{contenus_html}</ul>
  <h3>Règles du circuit</h3>
  <ul class="points">
    <li>Statuts : brouillon, proposé, validé, rejeté ou à revoir.</li>
    <li><b>La validation est faite par un membre différent de celui qui a saisi</b>, vérifié par la base de données elle-même.</li>
    <li>Chaque enregistrement porte le consentement éclairé du locuteur, son pseudonyme, sa variété et la façon dont il souhaite être crédité.</li>
    <li>Un texte réservé (savoir initiatique, parole qui ne se dit pas en public) est marqué et n'est jamais publié.</li>
    <li>Seuls les contenus validés sont copiés vers le site public.</li>
  </ul>
</section>

<section id="decisions">
  <h2>8. Six décisions qui reviennent au comité</h2>
  <ol class="decisions">{decisions_html}</ol>
</section>

<section id="methodes">
  <h2>9. Ce que MinWoo emprunte aux méthodes existantes</h2>
  <div class="tableau"><table>
    <thead><tr><th scope="col">Modèle</th><th scope="col">Ce qu'on retient</th><th scope="col">Ce qu'on fait autrement</th></tr></thead>
    <tbody>{methodes_html}</tbody>
  </table></div>
</section>

<section id="bibliographie">
  <h2>10. Bibliographie</h2>
  <ol class="biblio">{biblio_html}</ol>
</section>

<footer>MinWoo — plateforme d'apprentissage des langues mandé-sud de Côte d'Ivoire. Version lisible par l'application : content/curriculum/programme.json ; format des données : content/schema/modele-de-donnees.schema.json.</footer>
</main>
'''

out = ROOT / "docs" / "referentiel-comite.html"
out.write_text(page, encoding="utf-8")
print("ecrit", out, len(page), "caracteres,", nb_unites, "unites")
