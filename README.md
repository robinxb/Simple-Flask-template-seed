#Simple Flask app template seed

Features:

+ Use Flask-Assets
+ Flask-SQLAlchemy support
+ bower support
+ light-weight, keep the code as simple as possible

## Useage

### first run
```
pip install -r requirements.txt
bower install
python manage.py create_db
```

### run server
```
python manage.py server
```

### create database

`python manage.py create_db`

### drop database

`python manage.py drop_db`

### clean project

`python manage.py clean`

## Use bower to install libs

`bower install -S angularjs`

in `app/assets.py`, add libs you want to the Bundle