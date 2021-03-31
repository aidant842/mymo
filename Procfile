web: gunicorn mymo.wsgi:application
celery -A mymo worker --beat -Q uw -l info