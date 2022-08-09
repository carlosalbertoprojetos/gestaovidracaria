release: python manage.py migrate
web: gunicorn gestaovidracaria.wsgi --preload --log-file -
python3
manage.py collectstatic --noinput
