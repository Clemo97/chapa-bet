# Chapabet Assesment
This is a simple project to demonstrate how to implement session authentication in a Django and Ajax in building an Online Shop. This project will show how to send your session cookie and CSRF token along with your request in order to properly access API endpoints that require you to be authenticated.

In order to test out this project, follow these steps:
- clone the repository
- in the backend folder, run: `python3 -m venv venv`
- then activate the virtual environment `source venv/bin/activate`
- in the backend folder, run: `pip install -r requirements.txt`
- make migrations by running the command `python manage.py makemigrations`
- followed by `python manage.py migrate`
- go to backend/session_auth/settings.py, and under DATABASES, set the PASSWORD field to your database password.
- start the server `python manage.py runserver 8100`
python manage.py makemigrations