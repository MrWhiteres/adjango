asgi:
	granian --interface asgi project.network.asgi:application
wsgi:
	granian --interface wsgi project.network.wsgi:application
static:
	python manage.py collectstatic --noinput
base:
	python manage.py runserver
migrate:
	python manage.py migrate
make:
	python manage.py makemigrations --lint
lint:
	python manage.py lintmigrations
pip:
	pip install -r requirements.txt
fr:
	pip freeze > req.txt