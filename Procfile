web: gunicorn mymo.wsgi:application
main-worker: celery -A mymo worker --beat -A mymo -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler