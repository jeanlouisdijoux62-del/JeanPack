# JeanPack

> Paquet d'exemples : site statique, backend Flask, utilitaire Python et outils Windows.

## Contenu

- `site/` : site statique (HTML/CSS/JS)
- `backend/` : API Flask pour le formulaire de contact
- `python_app/` : application CLI Python
- `windows_tools/` : script batch Windows

## Lancer localement

### Lancer le site statique
Ouvrez le dossier `site` et lancez un serveur HTTP simple :

```powershell
Set-Location 'C:\Users\utilisateur\Desktop\tout en un\JeanPack\site'
python -m http.server 8000
# puis ouvrez http://localhost:8000
```

### Lancer le backend Flask
Créez un environnement, installez les dépendances et lancez l'application :

```powershell
Set-Location 'C:\Users\utilisateur\Desktop\tout en un\JeanPack\backend'
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
# backend accessible sur http://127.0.0.1:5000
```

Pour envoyer de vrais e‑mails, définissez les variables d'environnement (voir `backend/.env.example`).

### Utilitaire Python
```powershell
Set-Location 'C:\Users\utilisateur\Desktop\tout en un\JeanPack\python_app'
python main.py
```

### GitHub
Le dépôt distant est : https://github.com/jeanlouisdijoux62-del/JeanPack

Le site est publié via GitHub Pages sur : https://jeanlouisdijoux62-del.github.io/JeanPack/

## Configuration SMTP pour le backend
Copiez `backend/.env.example` en `.env` ou exportez les variables d'environnement listées avant de lancer le backend.

## Licence
MIT