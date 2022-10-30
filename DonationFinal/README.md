# Ploranzai a one stop trading platform

This project is aimed to build an advertisement platform where people in Afghanistan can place their goods ad and others can search those products and buy it.

## Setup the development environment

1. clone the project with `git clone git@github.com:ssahim/ploranzai.git`.
2. Open the project folder in vscode. and open terminal in vscode and and follow the instructions below 
### Backend setup
1. create virtual environment with `python3 -m venv venv`
2. activate the virtual environment with `source venv/bin/activate`
3. Database Setup
    * install `postgresql` DBMS in your computer and login to PostgreSQL via terminal or you can install PgAdmin on your computer to use the GUI.
    * create `ploranzai` user with `ploranzai@pl22` password.
    * create `ploranzaidb` database and assign `ploranzai` as the manager of the database so with `ploranzai` user we should be able manipulate the database.
4. in the terminal type `python manage.py migrate` to apply migrations to the database.
5. type `python manage.py runserver` should run the the backend without any error.

### Frontend setup

1. open another terminal in vscode. the terminal automatically opens in the project root folder.
2. change directory `cd frontend` folder.
3. type `npm install` will install all the dependencies for the frontend.
4. type `npm run dev` will run the frontend.
5. with   [http://localhost:8000](http://localhost:8000) you should be able to access the index page in the browser.


