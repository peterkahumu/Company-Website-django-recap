# Company Website — Django Recap

This repository is a learning-focused recap of building a small Django site. The goal is to relearn core Django concepts I may have forgotten and to pick up patterns or features I missed on earlier passes.

This repo intentionally focuses on clarity over complexity: small, readable code that demonstrates project structure, templates, URL routing, and the basics of models, admin, and testing.

What this repo is for
- Relearning Django fundamentals (project and app layout, URLconf, templates, views, models, migrations)
- Practicing small, testable features and good project hygiene
- Experimenting with patterns I may have missed before (template inheritance, reusable app structure, simple tests)

Quick start

Prerequisites
- Python 3.10+ (or compatible 3.x)
- pip

Setup

1. Create and activate a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Apply migrations and run the dev server:

   python manage.py migrate
   python manage.py runserver

4. (Optional) Create a superuser to use the admin:

   python manage.py createsuperuser

Run tests

   python manage.py test

Notes
- Database: This project uses SQLite by default (db.sqlite3) to keep setup simple.
- Templates live in the `templates/` directory. 
- This is intentionally minimal so the focus stays on learning and iteration.

Where to look next
- App code: `pages/` — see the app-level README for notes about what I relearned and the next exercises.

Learning log and TODOs
- Use the repo README and the `pages/README.md` to record discoveries, questions, and next learning steps.

License
- This is an educational exercise; see [LICENSE](LICENSE) included in the repository for license details.
