import discordwebhooks
url = "discord webhook url"
webhook = discordwebhooks.DiscordWebhooks(url, username="DiscordWebhooks")
embed = discordwebhooks.Embed(title="Embed Title")
fields = discordwebhooks.Fields()
fields.add_field("Testing Title", "Testing Value", False)
fields.add_field("Testing Title", "Testing Value", False)
embed.add_fields(fields)
embed.add_footer("Footer Text")
webhook.embed(embed)
webhook.loop.run_until_complete(webhook.send_message())
webhook.loop.close()
