#! /bin/bash
LOCATION_PATH="./jfelipef.sh"

if [[ -e "$LOCATION_PATH" ]]; then
	rm -f "$LOCATION_PATH"
fi

touch "$LOCATION_PATH"

echo "export POSTGRES_DB=\"query\"" >>"$LOCATION_PATH"
echo "export POSTGRES_USER=\"jfelipef\"" >>"$LOCATION_PATH"
echo "export POSTGRES_PASSWORD=\"password\"" >>"$LOCATION_PATH"
echo "export DB_URL=\"postgresql+asyncpg://jfelipef:password@postgres_query:5432/query\"" >>"$LOCATION_PATH"

sudo chmod +x "$LOCATION_PATH"

source "$LOCATION_PATH"

docker compose -f docker-compose.yaml up
