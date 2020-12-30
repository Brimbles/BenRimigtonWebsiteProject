release: python manage.py migrate
web: gunicorn benrimingtondotcom.wsgi --log-file - --bind 0.0.0.0:$PORT