# ESHOTS Test Project Documentation

## How the code is organized
It was important to follow best practices for this assignment. It would have been simpler and quicker to have Django handle both the frontend and backend tasks. However, when developing more advances web applications it is always best practice to have these environments separated. The backend directory contains the REST api written with Django. The frontend directory contains the front end application written with Angular.

## Steps to launch
1. Clone or pull the git repo
2. Create a python3 virtual env and activate it
3. cd into the backend directory
4. Install requirements using command `pip install -r requirements.txt`
5. Start the server by running `python manage.py runserver`
6. Data should already be present in sqlite3, but if its not you can run `python manage.py migrate` and then `python manage.py loaddata students_classes.json` to load the students_classes.json fixture.
