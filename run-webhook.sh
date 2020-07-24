#!/bin/bash
export BOT_TOKEN="${BOT_TOKEN:-127312313:WHYHELLLOTHERE}";
export LIST_PATH="${LIST_PATH:-voicelines.json}";
export WEBHOOK_HOST="${WEBHOOK_HOST:-example.com:433/webhook}";
export WEBHOOK_PATH="/$BOT_TOKEN/";
# final webhook will be "${WEBHOOK_HOST}${WEBHOOK_PATH}"
export PORT="${PORT:-8101}" # local port
export GUNICORN=/usr/local/bin/gunicorn

python3 pre-init.py; # set webhooks and etc
$GUNICORN -b localhost:$PORT -w 1 app:app;
# Only ONE worker. Even two may crash bot.

