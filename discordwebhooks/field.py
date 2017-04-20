
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
