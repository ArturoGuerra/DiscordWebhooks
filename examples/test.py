from discordwebhooks import *
import sys
url = sys.argv[0]
webhook = DiscordWebhooks(url, username="DiscordWebhooks")
embed = Embeds(title="MADARCHOD")
fields = Field()
fields.add_field("Testing Title", "Testing Value", False)
fields.add_field("Testing Title", "Testing Value", False)
embed.add_fields(fields)
webhook.embed(embed)
webhook.send_message()


