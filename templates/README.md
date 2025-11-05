# Templates

Ce dossier contient les fichiers HTML utilisés pour l’interface utilisateur
de l’application PolyCalc.

## Raison d’être
Fournir les pages web rendues par Flask pour permettre à l’utilisateur
de saisir une expression et d’afficher le résultat.

## Fichiers principaux
- `index.html` : page principale avec le formulaire et les boutons de calcul.

## Dépendances / hypothèses
- Ces templates utilisent le moteur **Jinja2** intégré à Flask.
- Les variables comme `result` sont passées depuis `app.py` lors du rendu.
