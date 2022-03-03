# https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django
# https://forum.djangoproject.com/t/items-are-not-being-added-in-the-cart/10564/26
# https://stackoverflow.com/questions/1194737/how-to-update-manytomany-field-in-django
# https://pythonspeed.com/articles/alpine-docker-python/
# https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ ***
# https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
# https://computingforgeeks.com/dockerize-django-application-with-postgresql/

docker-compose run zuri python manage.py makemigrations
docker-compose run zuri python manage.py migrate
docker-compose up
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev