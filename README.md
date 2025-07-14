# 🍕 Django Pizza Ordering Website

A simple pizza delivery web app built with Django — designed as a bootcamp project and expanded into a personal portfolio piece. Inspired by Domino’s-style ordering systems.

#Features

- Add pizzas to cart with real-time quantity tracking
- Ingredient and product management via Django admin
- Customizable menu loaded from JSON fixtures
- Database seeded with initial ingredients and pizzas
- Responsive homepage UI inspired by Domino’s Pizza
- Order summary with dynamic quantity/price calculation

#Tech Stack

- Python 3.11+
- Django 4.x
- HTML/CSS
- SQLite (default)
- JSON Fixtures

Getting Started

1. Clone the repository

git clone https://github.com/Dmarzorro/PizzeriaSite-.git
cd pizza-ordering-site

2. Create virtual environment and install dependencies

python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

3. Apply migrations and load data
python manage.py migrate
python manage.py loaddata ingredients.json
python manage.py loaddata pizzas.json

4. Finally, run the server

python manage.py runserver

