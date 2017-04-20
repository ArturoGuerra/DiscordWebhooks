#!/usr/bin/env python3.6
from  discordwebhooks import *
url = "https://ptb.discordapp.com/api/webhooks/304358573285310464/0HZAW9x2fJa4DkaPbSHSyST5cfCxZgbXswGonXOEyUkjRdsKzkQFaB-s4WZ34-EepUQm"
webhook = DiscordWebhooks(url, username="DiscordWebhooks")
embed = Embeds(title="Embed Title")
fields = Field()
fields.add_field("Testing Title", "Testing Value", False)
fields.add_field("Testing Title", "Testing Value", False)
embed.add_fields(fields)
embed.add_footer("Testing")
webhook.embed(embed)
webhook.loop.run_until_complete(webhook.send_message())
webhook.loop.close()
