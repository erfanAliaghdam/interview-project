## delete migrations
> find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

> find . -path "*/migrations/*.pyc"  -delete

## generate dev seeds
step 1 :
> docker-compose run project-backend sh

step 2:
> python manage.py generate_dev_seeds

note: you can use -y for answering all questions yes by default...

## development users
superuser :
> email: superuser@example.com

> password: DefaultPassword

support user (Support Group):
> email: user140@example.com

> password: DefaultPassword

seller user (Sale Group):
> email: user141@example.com

> password: DefaultPassword

