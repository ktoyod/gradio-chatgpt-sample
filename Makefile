up:
	docker compose --env-file .env.dev up -d

down:
	docker compose down

rm:
	docker compose down --rmi all

logs:
	docker compose logs -f

restart: rm up
