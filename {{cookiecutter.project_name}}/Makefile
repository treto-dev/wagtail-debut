init:
	git init
	cp docker/config/python.example.env docker/config/python.env
	ln -nfs $(PWD)/.githooks/pre-push.sh .git/hooks/pre-push
	ln -nfs $(PWD)/.githooks/pre-commit.sh .git/hooks/pre-commit
	{% if cookiecutter.use_gitflow == "yes" %}ln -nfs $(PWD)/.githooks/bump-version.sh .git/hooks/post-flow-release-start
	ln -nfs $(PWD)/.githooks/bump-version.sh .git/hooks/post-flow-hotfix-start{% endif %}
	make start
	make fixcode
	git add .
	git commit -m "Initial commit"

test:
	docker-compose run --rm python test
	{% if cookiecutter.use_decoupled_frontend == 'yes' %}cd frontend && npm install && npm run test{% endif %}

fixcode:
	docker-compose exec python black --exclude "/(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|migrations)/" ./

translate:
	docker-compose exec python bash -c "python manage.py makemessages -l sv_SE"

coverage:
	docker-compose exec python coverage run -m pytest --ds=pipit.settings.test
	docker-compose exec python coverage html

typecheck:
	docker-compose run --rm python typecheck

start:
	docker-compose up -d
	{% if cookiecutter.use_decoupled_frontend == 'yes' %}cd frontend && npm install && npm run dev{% endif %}

stop:
	docker-compose stop

logs:
	docker-compose logs -f python

shell:
	docker-compose exec python /bin/bash

makemigrations:
	docker-compose exec python ./manage.py makemigrations

migrate:
	docker-compose exec python ./manage.py migrate

build:
	docker-compose build

restart:
	docker-compose restart
