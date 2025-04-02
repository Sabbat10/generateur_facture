# King's Store - Application de Gestion de Magasin

## Description

King's Store est une application simple de gestion de magasin en ligne, développée en Python. Elle permet aux utilisateurs de :

- Ajouter des produits à un panier.
- Visualiser le contenu du panier avec les quantités, prix unitaires et totaux.
- Générer des factures dans différents formats (TXT, Word, PDF, Excel).

Ce projet est conçu à des fins d'apprentissage et de démonstration.

## Fonctionnalités

- **Ajout de produits :** Les utilisateurs peuvent ajouter des produits au panier en spécifiant le nom, la quantité et le prix.
- **Visualisation du panier :** Affiche la liste des produits dans le panier avec les détails (quantité, prix unitaire, total) et le total général.
- **Génération de factures :** Permet de générer des factures au format TXT, Word, PDF et Excel.

## Prérequis

- Python 3.x installé sur votre système.
- Les paquets Python listés dans le fichier `requirements.txt`.

## Installation

1.  **Cloner le dépôt :**

    ```bash
    git clone https://github.com/Sabbat10/generateur_facture.git
    cd [NOM_DU_REPO]
    ```

2.  **Créer un environnement virtuel (recommandé) :**

    ```bash
    python3 -m venv venv  # ou python -m venv venv
    ```

3.  **Activer l'environnement virtuel :**

    - **Sur Linux/macOS :**

      ```bash
      source venv/bin/activate
      ```

    - **Sur Windows :**

      ```bash
      .\venv\Scripts\activate
      ```

4.  **Installer les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1.  **Exécuter l'application :**

    ```bash
    python main.py # ou le nom de votre fichier principal
    ```

2.  **Suivre les instructions à l'écran pour effectuer des achats, consulter le panier et générer des factures.**

## Structure du projet

## Dépendances (Packages Python)

Le fichier `requirements.txt` contient la liste des paquets Python nécessaires pour exécuter ce projet. Voici une explication des paquets couramment utilisés pour la création de factures dans différents formats :

- **python-docx:** (Si utilisé pour les factures Word) Permet de créer et de modifier des documents Microsoft Word (`.docx`).

  ```bash
  pip install python-docx
  ```

- **fpdf:** (Si utilisé pour les factures PDF) Une bibliothèque pour générer des fichiers PDF. Offre un contrôle précis sur la mise en page.

  ```bash
  pip install fdf
  ```

- **pandas:** (Si utilisé pour les factures Excel) Permet de lire et d'écrire des fichiers Excel 2010+ (`.xlsx`).

  ```bash
  pip install openpyxl
  ```

  _Note : Assurez-vous d'ajouter ces paquets à votre `requirements.txt` si vous les utilisez._

## Auteur

Sabbat Lumpantshia
