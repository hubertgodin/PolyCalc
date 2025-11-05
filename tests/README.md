# Tests

Ce dossier contient les tests **unitaires** et **d’intégration** de l’application **PolyCalc**.

---

##  Raison d’être
Valider le bon fonctionnement :
- des **routes Flask** définies dans `app.py` ;
- des **fonctions mathématiques** définies dans `operators.py`.

Ces tests permettent de s’assurer que l’application répond correctement aux requêtes
et que les opérations arithmétiques produisent les bons résultats.

---

## Fichiers principaux
- `test_app.py` : teste l’affichage et les éléments de l’interface web.
- `test_operators.py` : teste les fonctions arithmétiques (`add`, `subtract`, `multiply`, `divide`).
- `test_calculate.py` : vérifie la logique de la fonction `calculate()` de `app.py`.

---

## Dépendances / hypothèses
- Les tests utilisent les modules **pytest** et **BeautifulSoup**.  
- L’environnement virtuel doit être **activé** avant l’exécution des tests.  
- Pour exécuter tous les tests, utiliser la commande suivante :

```bash
pytest -v
