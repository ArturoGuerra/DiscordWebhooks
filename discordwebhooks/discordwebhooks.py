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

class Embeds():
    def __init__(self, **kwargs):
        self.embed = dict()
        self.embed['fields'] = list()
        valid_args = ["title", "description", "url", "color", "footer"]
        for arg in kwargs:
            if arg in valid_args:
                self.embed[arg] = kwargs[arg]
    def add_fields(self, field):
        if field.__class__.__name__ == "Field":
            self.embed['fields'] = field.content()
    def add_footer(self, text, icon_url=None):
        footer = dict()
        footer['text'] = text
        if icon_url:
            footer['icon_url'] = icon_url
        self.embed['footer'] = footer
    def add_video(self, url, height, width):
        video = dict()
        video['url'] = url
        video['width'] = width
        video['height'] = height
        self.embed['video'] = video
    def add_image(self, url, height, width):
        image = dict()
        image['url'] = url
        image['width'] = width
        image['height'] = height
        self.embed['image'] = image
    def add_author(self, name, url=None, icon_url=None):
        author = dict()
        author['name'] = name
        if icon_url:
            author['icon_url'] = icon_url
        if url:
            author['url'] = url
        self.embed['author'] = author
    def add_provider(self, name, url):
        provider = dict()
        provider['url'] = url
        provider['name'] = name
        self.embed['provider'] = provider
    def add_thumbnail(self, url, height, width, proxy_url=None):
        thumbnail = dict()
        thumbnail['url'] = url
        thumbnail['height'] = height
        thumbnail['width'] = width
        if proxy_url:
            thumbnail['proxy_url'] = proxy_url
        self.embed['thumbnail'] = thumbnail
    def content(self):
        return self.embed

class Field():
    def __init__(self):
        self.field = list()
    def add_field(self, title, value, inline=True):
        field = dict()
        if inline == True:
            inline = 'true'
        elif inline == False:
            inline = 'false'
        field['name'] = title
        field['value'] = value
        field['inline'] = inline
        self.field.append(field)
    def content(self):
        return self.field
