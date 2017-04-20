import json
import logging
import asyncio
import requests
from functools import partial

class DiscordWebhooks():
    def __init__(self, url, content="", username="", avatar_url="", logger=None, loop=None):
        self.url = url
        self.loop = asyncio.get_event_loop() if loop is None else loop
        if logger == None:
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger("DiscordWebhooks")
        else:
            self.logger = logger
        self.username = username
        self.content = content
        self.avatar_url = avatar_url
        self.tts = False
        self.embeds = list()
        self.data = dict()
    def embed(self, embed):
        if embed.__class__.__name__ == "Embeds":
            self.embeds.append(embed.content())
    def format(self):
        self.data['username'] = self.username
        self.data['content'] = self.content
        self.data['embeds'] = self.embeds
        self.logger.info(self.data)
        return self.data
    async def send_message(self):
        data = json.dumps(self.format())
        func = partial(requests.post, self.url, data=data, headers={"Content-Type": "application/json"})
        response = await self.loop.run_in_executor(None, func)
        self.logger.info(response)
        self.logger.info(response.text)


