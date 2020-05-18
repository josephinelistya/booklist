# BOOK LIST

In computer programming, create, read, update, and delete (CRUD) are the four basic functions. Here is a web app that does those four basic functions to CRUD a book list.

## HOW TO RUN THE WEB APP

- Download Django and install it on command prompt by typing: 
```python
python -m pip install Django
```
- Download or clone the repository.
- Open with source code editor (I use VS Code).
- Download postgreSQL.
- Create a database named BooklistDB on pgAdmin. You can check the database name on settings.py
- On setting.py, you may need to change the DATABASE details such as user and password based on your postgreSQL.
- Connect the project and database. On VS Code terminal, type: 
```python
python manage.py sqlmigrate booklist_register 0001
```
- You need to make migration by typing: 
```python
python manage.py makemigrations booklist_register
```
- You need to migrate by typing: python manage.py migrate
```python
python manage.py migrate
```
- You need to add any booktype(s) on database table and run the SQL code. If you are using postgreSQL, open the pgAdmin, go to Tables and booklist_register_booktype.
- You may need to install crispy form and psycopg2 by typing: 
```python
pip install django-crispy-forms
py -m pip install psycopg2
```
- Open the terminal and run the server with: 
```python
python manage.py runserver
```
- Click the server. If this fails, try to close other source code editor and do run server again.
- Go to booklist/ to CRUD the database.
- All the changes saved to BooklistDB database.
