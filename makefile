local:
	pipenv run lylesightings/manage.py runserver

scrape:
	pipenv run lylesightings/manage.py scrapelyles

deploy:
	git push heroku