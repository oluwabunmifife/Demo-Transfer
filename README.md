# Overview
A *mini* project modelling how a transfer app works🧔🏾
---
<br><br><br><br>

# Installation
1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: pip install -r requirements.txt in your shell.

**Like So:**
-  ``pip install virtualenvwrapper`` #This is just to ensure you can create *virtual envs* on your computer, you can do these steps however you know best
-  ``mkvirtualenv venv`` #This will create the virtual env called *venv*
-  ``workon venv`` #This will activate the *virtual env*
-  ``pip install -r requirements.txt`` #Make sure you're in the *dir* that has the requirements.txt file. <br><br><br><br><br>

# Setup👨🏾‍💻👩🏾‍💻
> In your command line, run the following code to set up the *database* (I used sqlite😅)
---
1. ``python manage.py makemigrations``

2. ``python manage.py migrate``

3. ``python manage.py runserver``
With that your server is running and you're all set🐱‍👤 <br><br>


Note. [^1]

[^1]: This is a Python/Django project
