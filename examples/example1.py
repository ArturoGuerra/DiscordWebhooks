from discordwebhooks import *
url = "discord webhook url"
webhook = DiscordWebhooks(url, username="DiscordWebhooks")
embed = Embeds(title="Embed Title")
fields = Field()
fields.add_field("Testing Title", "Testing Value", False)
fields.add_field("Testing Title", "Testing Value", False)
embed.add_fields(fields)
webhook.embed(embed)
webhook.loop.run_until_complete(webhook.send_message())
webhook.loop.close()
