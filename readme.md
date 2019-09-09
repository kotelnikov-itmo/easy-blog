### Install:

1. Clone this rep
2. make virtual env
3. `pip install -r requirements.txt`
4. `./manage.py migrate` (SQLite3 as DB)

### Demo:

1. `./manage.py loaddata blog/fixtures/example.json`
2. `./manage.py runserver 8000`
3. Open localhost:8000/api/posts/ in browser
