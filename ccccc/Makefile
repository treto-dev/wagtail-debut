init:
	git init
	cp docker/config/python.example.env docker/config/python.env
	ln -nfs $(PWD)/.githooks/pre-push.sh .git/hooks/pre-push
	ln -nfs $(PWD)/.githooks/pre-commit.sh .git/hooks/pre-commit

	make start
	make fixcode
	git add .
	git commit -m "Initial commit"

test:
	docker-compose run --rm python test
	cd frontend && npm install && npm run test

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
	cd frontend && npm install && npm run dev

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

restart:
	docker-compose restart
