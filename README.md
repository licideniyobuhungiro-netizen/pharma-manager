# pharma-manager
Application de gestion de pharmacie – Développé dans le cadre du test technique SMARTHOLOL.

## Stack Technique
- Backend : Django 4.x + Django REST Framework + PostgreSQL
- Documentation API : Swagger (drf-spectacular)

## Installation Backend
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver