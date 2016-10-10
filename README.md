# ESHOTS Test Project Documentation

## How the code is organized
It was important to follow best practices for this assignment. It would have been simpler and quicker to have Django handle both the frontend and backend tasks. However, when developing more advances web applications it is always best practice to have these environments separated. The backend directory contains the REST api written with Django. The frontend directory contains the front end application written with Angular.

## Steps to launch
1. Clone or pull the git repo
2. Create a virtual env
3. Open up a new terminal process (need two process -> backend & frontend)
3. cd into the backend directory
4. Install requirements using command `pip install -r requirements.txt`
5. Data should already be present in sqlite3, but if its not run `python manage.py migrate` and then `python manage.py loaddata students_classes.json` to load the initial data provided.
