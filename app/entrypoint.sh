#!/bin/sh

if [ -f "db.sqlite3" ]
then
    rm db.sqlite3
fi

touch db.sqlite3
python manage.py loaddata db.json
python manage.py migrate --no-input
python manage.py collectstatic --no-input


exec "$@"