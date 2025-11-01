 # PolyCalc
**Équipe 18**

## Objectif
Ce projet a pour but de développer une calculatrice web.

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
1. Ouvrir le terminal et se diriger vers le répertoire du projet `/PolyCalc`
2. Créer un environnement virtuel `venv`
```shell
    python3 -m venv venv
```
3. Activé l'environnement virtuel `venv`
- Sur **macOS/Linux**
```shell
    source venv/bin/activate
```
- Sur **Windows**
```shell
    Scripts\activate
```
4. Installer les dépendances listés dans le fichier `requirement.txt` dans votre environnement virtuel
```shell
    pip install -r requirements.txt
```

## Démarrer l'application
Partir l'application avec la commande 
```shell
    python3 app.py
```

## Tests
Vous pouvez exécuter tous les tests avec la commande :
```shell
    pytest
```
ou si vous voulez exécuter les tests un fichier spécifique, vous devez vous diriger vers le module `tests` et effectuer la commanded suivante:
```shell
     pytest test_operators.py
```