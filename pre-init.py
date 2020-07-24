from mainapp import bot, WEBHOOK_HOST, WEBHOOK_PATH
import time
webhook_url = WEBHOOK_HOST + WEBHOOK_PATH

print(bot.remove_webhook())
time.sleep(3)
print('Webhook set to', webhook_url)
print(bot.set_webhook(url=webhook_url))

