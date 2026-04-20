#!/usr/bin/env sh

set -eu

cd "$(dirname "$0")"

timeout_seconds=60
elapsed=0

docker compose build --no-cache
docker compose up -d

while [ "$elapsed" -lt "$timeout_seconds" ]; do
  if curl -fsS http://localhost/ >/dev/null 2>&1; then
    echo "✅ Stack déployée avec succès"
    exit 0
  fi

  elapsed=$((elapsed + 1))
  sleep 1
done

echo "❌ Timeout — vérifiez les logs"
exit 1