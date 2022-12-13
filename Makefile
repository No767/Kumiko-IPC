all: start-dev-deps

start-dev-deps:
	sudo docker compose -f docker-compose-dev.yml up -d
