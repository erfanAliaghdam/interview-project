## delete migrations
> find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

> find . -path "*/migrations/*.pyc"  -delete

## development seed
> python manage.py generate_dev_seeds
> 
note: you can use -y for answering all questions yes by default...

