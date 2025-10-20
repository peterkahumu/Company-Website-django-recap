# Pages app — learning notes

This `pages` app is intentionally small. It's used as the primary place to practice and relearn Django basics: views, URL routing, templates, and minimal models/admin usage.

Why this app exists
- A focused playground to relearn Django fundamentals and to record what I rediscover.
- Keep examples compact so it's easy to iterate and add notes.

What you'll find here
- `views.py` — simple generic class based views for `home` and `about` pages.
- `urls.py` — app-level URL configuration included in the project `urls.py`.

Relearning notes (starter list)
- Remember how URL namespaces work — consider namespacing this app if you add more apps.
- Template inheritance with `base.html` keeps markup DRY; practice by adding blocks and extending them.
- Tests: write a couple of simple tests for views and any model logic.

Notes to future me
- Keep changes small and commit often — this repo is a learning journal as much as working code.
