# Calorie Counter

A simple, clean web app for tracking daily meal calories — built with Django and styled with Tailwind CSS. Designed for everyday use, it lets you log meals throughout the day, monitor your running calorie total, and reset when the day is done. 


## Features
 
- Add meals with a name and calorie count
- View all meals logged for the day in a clean table
- Edit or delete any meal entry
- See the total calories consumed for the day
- Reset the day's meals with a single click
---
 
## Tech Stack
 
| Layer | Technology |
|---|---|
| Backend | Python 3.x, Django 3.x |
| Database | PostgreSQL |
| Frontend | HTML5, Tailwind CSS |
| Deployment | Render |
| Version Control | Git |
 
---
 
## Local Setup
 
### 1. Clone the repository
 
```bash
git clone https://github.com/your-username/calorie-counter.git
cd calorie-counter
```
 
### 2. Create and activate a virtual environment
 
```bash
python -m venv venv
 
# Windows
venv\Scripts\activate
 
# macOS/Linux
source venv/bin/activate
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Configure environment variables
 
Create a `.env` file in the root directory:
 
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:password@host:5432/dbname
```
 
> For local development you can use a local PostgreSQL instance or a free cloud database like [Neon](https://neon.tech).
 
### 5. Run migrations
 
```bash
python manage.py migrate
```
 
### 6. Start the development server
 
```bash
python manage.py runserver
```
 
Visit `http://127.0.0.1:8000` in your browser.
 
## Project Structure
 
```
calorie-counter/
├── calorieproject/         # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── calorieapp/             # Main Django app
│   ├── models.py           # Meal model
│   ├── views.py            # CRUD + reset + total calories logic
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── insert.html
│       └── edit.html
├── requirements.txt
├── manage.py
└── README.md
```
 
---
 
## Dependencies
 
Key packages in `requirements.txt`:
 
```
asgiref==3.11.1
dj-database-url==3.1.2
Django==6.0.5
gunicorn==26.0.0
packaging==26.2
psycopg2==2.9.12
python-dotenv==1.2.2
sqlparse==0.5.5
tzdata==2026.2

```
 
---
 
## Security Notes
 
- `SECRET_KEY` and `DATABASE_URL` are stored as environment variables, never hardcoded
- `DEBUG` should be set to `False` in production
- Django's built-in CSRF protection is enabled on all forms
- Input validation is handled at the model and form level
