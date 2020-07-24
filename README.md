# A Hat in Time Voice bot
I have nothing to say, actually, just check it out: https://t.me/ahitvoicebot

## Installation

### Clone repository:
`$ git clone https://github.com/hatkidchan/ahitvoicebot && cd ahitvoicebot`

### Install requirements:
`$ pip install -r requirements-poll.txt` if you will use polling
`$ pip install -r requirements-wh.txt` if you will use webhooks

### Download voicelines
That is entirely must be done with you. I don't want problems with GfB.
And also you must host them somewhere. No matter where.
Anyway, you must create voicelines list. That may be done by using provided script.

### Run bot:

#### Polling example
`$ BOT_TOKEN=12344356:WHYHELLLOTHERE bash run-polling.sh`
And it will just work, I hope.

#### Webhooks example
```bash
$ BOT_TOKEN=12344356:WHYHELLLOTHERE \  # Bot token, obviously
WEBHOOK_HOST=example.com:443/webhook \ # Webhook prefix
PORT=8101 \                            # Port for flask
bash run-webhook.sh # Actually, webhook will be "${WEBHOOK_HOST}/${BOT_TOKEN}/"
```
You also must somehow proxy requests to flask server. Apache example:
```apache
<VirtualHost *:443>
    ServerName example.com
    ProxyPreserveHost On
    ProxyPass /webhook/ http://127.0.0.1:8101/
    ProxyPassReverse /webhook/ http://127.0.0.1:8101/
</VirtualHost>
```
I have no idea how that will be done in NGINX or somewhere else. Please, don't ask me about that.


## PS

 * `"basedir"` in voices list is unused, but I'm too scared to delete it
 * `make-voicelines.py` changed not a lot since first creation, so it's ugly as shit
 * I forgot to add one feature: bot stats/uptime and some others. But that not so important
 * If someone want create Dockerfile - PR's are welcome :)
 * No, I will NOT rewrite bot with async/other shit. This is my project, kiriharu, please, fuck off

