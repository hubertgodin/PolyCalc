# Tests

Ce dossier contient les tests **unitaires** et **d’intégration** de l’application **PolyCalc**.

---

##  Raison d’être
Valider le bon fonctionnement :
- des **routes Flask** définies dans `app.py` ;
- de la **logique de calcul** gérée par la fonction `calculate()` dans `app.py` ;
- des **fonctions arithmétiques** définies dans `operators.py`.

Ces tests permettent de s’assurer que l’application répond correctement aux requêtes HTTP
et que les opérations arithmétiques produisent les bons résultats.

---

## Fichiers principaux
- `test_app.py` : teste l’affichage et les éléments de l’interface web.
- `test_operators.py` : teste les fonctions arithmétiques (`add`, `subtract`, `multiply`, `divide`).
- `test_calculate.py` : vérifie la logique de la fonction `calculate()` de `app.py`.
- 

---

## Dépendances / hypothèses
- Les tests utilisent les modules 
- **pytest**
- **pytest-mock**
- **pytest-check**
- **BeautifulSoup4** 
Avant d’exécuter les tests, assurez-vous que :
1. L’environnement virtuel est activé :
   ```bash
   Scripts\activate
   ```
2. Les dépendances sont installées :
 ```bash
pip install -r requirements.txt
   ```
- Pour exécuter tous les tests, utiliser la commande suivante :

```bash
pytest -v
   ```
Exécuter les tests d’un fichier spécifique:
```bash
pytest -v tests/test_nom_du_fichier.py
   ```

Exécuter un cas de test précis:
```bash
pytest -v tests/test_nom_du_fichier.py::nom_du_test
   ```