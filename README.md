# [Unsimply Tech](https://github.com/Miss-Faith/Unsimply-Tech)
#### By [Faith Mwangi](https://github.com/miss-faith)
### Description
A landing page that provides users with blogs. A User is able to create an account, update their profile, add new blogs, delete or update their blogs and comment on existing blogs.
## Site
[Unsimply Tech](https://unsimplytech.herokuapp.com/)
### Setup Requirements

##Developer
## Prerequisites
**Installing Python**

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

You may check your Python version by running:

```bash
$python --version
```

Depending on your installation you might have access to Python3 interpreter either by running `python` or `python3`.

```bash
$python
```
Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Cloning**
Fork the repository and Git clone to your local machine. Access the file and run the program on the code editor, ubuntu, mac or windows terminal.
```bash
$git clone https://github.com/user-name/Unsimply-Tech/
$cd Unsimply-Tech
```

**Creating a Virtual Environment**
Inside the Unsimply Tech directory create a virtual environment by running
```bash
$ pip install pip-env
```
activate the virtual environment by running
```bash
$ pipenv shell
```
**Adding dependencies**
Install Flask
```bash
(virtual) $ pipenv install flask
```
Install Bootstrap
```bash
(virtual) $ pipenv install flask-bootstrap
```
Install Flask Script
```bash
(virtual) $ pipenv install flask-script
```
Install Flask sqlalchemy
```bash
(virtual) $ pipenv install flask-sqlalchemy
```
Install Flask psycopg2
```bash
(virtual) $ pipenv install psycopg2
```
Install Flask psycopg2-binary
```bash
(virtual) $ pipenv install psycopg2-binary
```
Install Flask gunicorn
```bash
(virtual) $ pipenv install gunicorn
```
Install Flask flask-login
```bash
(virtual) $ pipenv install flask-login
```
Install Flask flask-uploads
```bash
(virtual) $ pipenv flask-uploads
```
Install Flask werkzeug
```bash
(virtual) $ pipenv install werkzeug==0.16.0
```
Install Flask markupsafe
```bash
(virtual) $ pipenv install markupsafe==2.0.1
```
Install Flask Flask Mail
```bash
(virtual) $ pipenv install Flask-Mail
```
Install Flask Flask Migrate
```bash
(virtual) $ pipenv install Flask-Migrate ==2.7.0
```
Install Flask Flask wtf
```bash
(virtual) $ pipenv install flask-wtf
```
Install Flask Email validator
```bash
(virtual) $ pipenv install wtforms[email]
```
Install Flask Dotenv
```bash
(virtual) $ pipenv install python-dotenv
```

**Running the app** 
To make the program executable, run:
```bash
(virtual) $chmod a+x start.sh
```
To run the program, run:
```bash
(virtual) $./start.sh
```
Follow the local link generated to view your live site

**Running tests** 
To run test cases:
```bash
(virtual) $python3 manage.py test
```

**Migrate data** 
To run test cases:
```bash
(virtual) $python3 manage.py db init
```
```bash
(virtual) $python3 manage.py db migrate -m "Initial Migration"
```
```bash
(virtual) $python3 manage.py db upgrade
```

## Technology Used
### Frameworks
* Flask
* Bootstrap
* Heroku
###Languages
* Python
* CSS
* HTML
### Other resources
* [Google Fonts](https://fonts.google.com/)


## Development
### Want to contribute? Great!
To fix a bug or enhance an existing module, follow these steps:
* Fork the repo
* Create a new branch ('git checkout -b improve-feature')
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes ('git commit -am 'Improve feature')
* Push to the branch ('git push origin improve-feature')
* Create a Pull Request
### Bug / Feature Request
If you find a bug/error, kindly open an issue [here](https://github.com/miss-faith/Unsimply-Tech/issues/new)
Include your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/miss-faith/Unsimply-Tech/issues/new)
Include sample queries and their corresponding results.
## To-Do
Future update to include a data base that stores information accessible when the application is closed and re-opened
## Contact information
[Faith Mwangi](https://github.com/miss-faith)

[Email](faith.mwangi@student.moringaschool.com)
## License
MIT License
Copyright (c) 2022 **Faith Mwangi**