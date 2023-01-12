# Projet Partie 1

## Description du projet

Au jeu de Poker, à partir d’une main de 7 cartes, il s’agit de trouver la meilleure combinaison à 5 cartes.
Dans ce jeu, les combinaisons possibles sont du plus fort au moins fort:

+ La suite à la couleur, les cartes se suivent sans trous et sont de la même couleur: Dix, Neuf, Huit, Sept et Six de Carreau.
+ Le carré, 4 cartes identiques, les 4 Neufs
+ Le full, 3 cartes identiques et 2 autres cartes identiques, 3 Rois et 2 Valets.
+ La couleur, la même couleur pour toutes les cartes: toutes les cartes sont du Pique.
+ La suite, les cartes se suivent sans trous: As, Roi, Dame, Valet et dix.
+ Le brelan, 3 cartes identiques: 3 Septs.
+ La double paire, 2 fois 2 cartes identiques: 2 Neufs et 2 Quatres.
+ La paire: 2 cartes identiques: 2 Cinqs.
+ Aucune combinaison.

## Travail à faire

A partir d'une main de 7 cartes, vous devrez indiquer quelle est la combinaison la plus forte trouvée. Vous préciserez la hauteur et/ou la couleiur des cartes qui forment la combinaison ainsi que celles qui restent. Ces infos seront consignées dans un tuple. Voici des exemples de tuples attendus pour:

+ La suite à la couleur:    couleur et hauteur de la carte la plus forte.
+ Le carré: 			2 hauteurs: celle du carré, puis de la carte restante.
+ Le full: 			2 hauteurs, celle du brelan, puis celle de la paire.
+ La couleur: 			couleur et hauteur de toutes les cartes, par ordre décroissant.
+ La suite: 			hauteur de la carte la plus forte.
+ Le brelan:			3 hauteurs, celui du brelan, puis les 2 suivantes par hauteur décroissante.
+ La double paire:		3 hauteurs, celle de la paire la plus forte en premier, puis la seconde paire et enfin la carte restante.
+ La paire: 			4 hauteurs, celle de la paire, puis les autres cartes par hauteur décroissante.
+ Rien:				Toutes les hauteurs par ordre décroissant.

Vous devrez rendre un fichier source en Python, dont l’une des fonctions (ou une méthode d’un classe) renverront le résultat attendu. La main de 7 cartes sera passée en paramètres. Par exemple:

```py
d = Deck()
h = [d.pop() for _ in range(7)]
res = find_combinaisons(h)

# est ce un BRELAN ?
assert res == (Combinaison.BRELAN, (Value.NEUF, Value.ROI, Value.DEUX))
```
Le travail doit être rendu sous la forme de fichiers source en `Python` autodocumenté pour le **jeudi 26 janvier 2023**. En plus de ces sources, seront les bienvenus:
+ un fichier `exemple` de mise en oeuvre.
+ les fichiers de tests unitaires.

L'ensemble des livrables, sous forme de Zip dont le nom sera composé du numéro de votre groupe, sera à déposer sur Teams, dans un dossier dédié, dont le nom vous sera précisé utltérieurement.

## Fichiers source fournis à utiliser de manière obligatoire:

Le fichier `card_deck.py` qui contient:
+ 2 énumérations qui correspondent aux valeurs et couleurs des cartes.
+ 1 classe Card qui correspond à une carte.
+ 1 classe Deck qui contient un jeu de 52 cartes.

Le fichier `combinaison.py` qui contient:
+ une énumération des combinaison en poker.

Le fichier de test `test_card_deck.py`.
