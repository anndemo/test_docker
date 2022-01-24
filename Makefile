run:
	docker run  --rm --name test-docker  test-docker:db
stop:
	docker stop anndemo/test-docker

run_term:
	python index.py
run-dev:
# контейнер для разработки
	docker run -v "/Users/anndemo/PycharmProjects/test_docker:/app"  -v logs:/app/data --rm --name test-docker  test-docker:volume

run-mongo:
# контейнер с mongo
	docker run --name mongodb -d -p 27017:27017 mongo
