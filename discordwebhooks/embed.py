
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
