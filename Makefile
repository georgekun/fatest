up:
	sudo  docker-compose  -f docker-compose.yml up --build -d

down:
	sudo	docker-compose -f docker-compose.yml down -v
