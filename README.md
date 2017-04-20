# DiscordWebhooks
DiscordWebhook api wrapper, It makes the use of embed easy thanks to its Object oriented design.
This wrapper uses the requests module and an asyncio executor to make all requests threaded so there will be no blocking.

# Requirements
- requests

# Example
The example below sends a message saying hello word!!
```python
import discordwebhooks

url = 'discord webhook url'
webhook = discordwebhooks.DiscordWebhooks(url, username="Disord Bot", content="Hello Word!!")

async def run():
    await webhook.send_message()

webhook.loop.run_until_complete(run())
```



# Credit
Credit to [Derpolino](https://github.com/Derpolino)
