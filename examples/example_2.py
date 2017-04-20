import discordwebhooks
url = 'discord webhook url'
webhook = discordwebhooks.DiscordWebhooks(url, username="WebHook", content="Discord Webhook")
webhook.loop.run_until_complete(webhook.send_message())
