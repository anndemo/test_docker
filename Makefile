run:
	docker run  -v logs:/app/data --rm --name test-docker  test-docker:volume
stop:
	docker stop anndemo/test-docker

run_term:
	python index.py
run-dev:
# контейнер для разработки
	docker run -v "/Users/anndemo/PycharmProjects/test_docker:/app"  -v logs:/app/data --rm --name test-docker  test-docker:volume


