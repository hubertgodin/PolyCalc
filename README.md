 # PolyCalc
**Équipe 18**


PolyCalc est une application web développée avec **Flask** permettant d’effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division) à travers une interface web simple et intuitive.

## Objectif
L’objectif du projet **PolyCalc** est de développer une **application web de calculatrice interactive** à l’aide du framework **Flask**.  
Cette application permet à l’utilisateur d’effectuer des **opérations arithmétiques de base** directement depuis une interface web intuitive.

Ce projet a pour buts de :
- Offrir une interface simple et ergonomique pour les calculs de base.
- Mettre en œuvre une architecture **backend Flask** connectée à un **frontend HTML/CSS**.  
- Gérer les erreurs de saisie et les expressions invalides de manière robuste.  
- Fournir un code **structuré, réutilisable et bien documenté**.  
- Assurer la fiabilité du système grâce à des **tests unitaires et d’intégration**.

## Prérequis d’installation
- Avoir une version récente de [Python](https://www.python.org/downloads/) d'installé **>=3.14.0**. Vous pouvez vérifer en effectuant la commande suivante dans votre terminal:
```shell
    python3 --version
```
- Avoir une version récente de `pip` d'installé. Viens souvent avec l'installation de [Python](https://www.python.org/downloads/). Vous pouvez vérifer en effectuant la commande suivante dans votre terminal:
```shell
    pip --version
```

## Instructions d’installation
1. Cloner le dépôt
1. Ouvrir le terminal et se diriger vers le répertoire du projet `/PolyCalc`
2. Créer un environnement virtuel `venv`
```shell
    python3 -m venv venv
```
3. Activer l'environnement virtuel `venv`
- Sur **macOS/Linux**
```shell
    source venv/bin/activate
```
- Sur **Windows**
```shell
    Scripts\activate
```
o4. Installer les dépendances listés dans le fichier `requirement.txt` dans votre environnement virtuel
```shell
    pip install -r requirements.txt
```

## Démarrer l'application 
Lancer l'application avec la commande 
```shell
    python3 app.py
```
Ensuite, ouvrir votre navigateur à l’adresse :
http://127.0.0.1:5000
Fonctionnalités :
Interface web simple permettant de saisir des expressions arithmétiques.
Opérations disponibles : addition (+), soustraction (−), multiplication (×), division (÷).
Affichage du résultat instantané après validation.
Gestion des erreurs (opérateur manquant, division par zéro, etc.).


## Tests
Les tests sont réalisés à l’aide de pytest et BeautifulSoup.
Vous pouvez exécuter tous les tests avec la commande :
```shell
    pytest -v
```
Les tests couvrent :
Le bon fonctionnement des routes Flask (test_app.py).
La logique de calcul dans calculate() (test_calculate.py).
Les opérations arithmétiques (test_operators.py).

ou, si vous voulez exécuter les tests un fichier spécifique, vous devez vous diriger vers le module `tests` et effectuer la commanded suivante:
```shell
     pytest test_nom_du_fichier.py
```
## Flux de contribution
Ce projet suit un flux de travail collaboratif basé sur les branches et les Pull Requests.

**Étapes pour contribuer :**

1. Créer une nouvelle branche à partir de main :
```
git checkout -b feature/nom-de-ta-branche
```

(exemples : feature/add-tests, fix/division-error)

2. Faire les modifications dans le code ou la documentation.

3. Ajouter et committer les changements :
```
git add .
git commit -m "feat: ajout de la nouvelle fonctionnalité"
```

4. Pousser la branche sur GitHub :

```
git push origin feature/nom-de-ta-branche
```

5. Ouvrir une Pull Request (PR) sur GitHub :

Décrire brièvement les changements effectués.

Demander une révision si nécessaire.

Une fois la PR validée, elle peut être fusionnée dans la branche main.
