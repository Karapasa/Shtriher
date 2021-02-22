import os
import barcode
from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter

dir_name = os.path.join(os.getcwd(), 'app/static/labels/')

try:
    os.mkdir(dir_name)
    print('Directory ',dir_name,' created')
except FileExistsError:
    pass

class Etich():
    font = ImageFont.truetype("DejaVuSansMono.ttf", size=18, encoding='utf-8')

    def __init__(self, number, compy, name, sku, field, view='ver', width=120, height=75):
        self.number = number
        self.view = view
        self.width = width
        self.height = height
        self.compy = compy
        self.name = name
        self.sku = sku
        self.field = field

    def get_company(self):
        return 'Название компании: ' + self.compy

    def get_sku(self):
        return 'Артикул: ' + self.sku

    def get_name(self):
        return 'Наименование продукции: ' + self.name

    def get_field(self):
        return 'Описание: ' + self.field

    def get_shtrich(self):
        a1 = Code(self.number)
        a1.save_code()

    def create_etich(self):
        img = Image.new('RGBA', (455, 284), 'white')
        idraw = ImageDraw.Draw(img)
        data = (self.get_company(), self.get_name(), self.get_sku(), self.get_field())
        x, y = 40, 25
        for text in data:
            idraw.text((x, y), text, font=self.font, fill='black')
            y += 25
        self.get_shtrich()
        sht = Image.open(dir_name + self.number + '_sht.png', 'r').resize((250, 120))

        img.paste(sht, (102, 150))
        return img

    def save_etich(self):
        img = self.create_etich()
        img.save(dir_name + self.number + '_et.png')


class Code():
    CODE = 'ean13'

    def __init__(self, number, type='ver', width=0.2, height=20):
        self.type = type
        self.number = str(number)
        self.width = width
        self.height = height
        self.name = dir_name + self.number + "_sht"


    def generate(self):
        return barcode.get(Code.CODE, self.number, writer=ImageWriter())

    def save_code(self):
        ean = self.generate()
        ean.save(self.name,
                 options={'background': 'white', 'module_width': 0.4, 'module_height': 20, 'foreground': 'black',
                          'text_distance': 1, 'font_size': 11})
