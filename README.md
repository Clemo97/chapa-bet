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

## Goals
Features that I succesfully implemented.

1. [x] Create a web application which works like a really small online shop.
2. [x] Create a product listing which will display all products from the database.
3. [ ] Add a “to the basket” button to each product in the listing.
4. [x] Make the product basket work and display all products which are in the basket as a list with
small images.
5. [x] Create a login and registration with phone number, password and a name.
6. [x] The login should be session based.
7. [x] Create a checkout which is shown when the user is logged in.
8. [ ] The user should be able to choose between 2 payment methods. Call them method1 and
method2.
9. [x] Store the order at the database.
10. [ ] Add a weight/volume/size filter to the product list. The user should be able to filter the listing
by weight/volume/size.
11. [] Unit tests.

