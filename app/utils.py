import os
import math
import barcode
import logging.config

from settings import logging_config
from PIL import Image, ImageDraw, ImageFont
from barcode.writer import ImageWriter

logging.config.dictConfig(logging_config)
logger = logging.getLogger('shtriher_logger')

dir_name = os.path.join(os.getcwd(), 'app/static/labels/')

try:
    os.mkdir(dir_name)
    print('Directory ',dir_name,' created')
except FileExistsError:
    print('Directory ',dir_name,' already exists')


class Etich():

    def __init__(self, number, compy, name, sku, field, view='ver', width=120, height=75):
        self.number = number
        self.view = view
        self.width = width
        self.height = height
        self.compy = compy
        self.name = name
        self.sku = sku
        self.field = field

    def _get_font_size(self, data):
        if len(''.join(data)) > 700:
            logger.debug('Превышен лимит символов для %s - %s', self.compy, self.number)
            return Exception
        size_table = {18: (7, 37), 16: (8, 40), 14: (9, 51), 12: (10, 59), 10: (11, 69)}
        for size in size_table:
            quan_total_str = 0
            for block in data:
                quan_str = math.ceil(len(block) / size_table[size][1])
                quan_total_str += quan_str
            if quan_total_str <= size_table[size][0]:
                return size, size_table[size][1]
        return None


    def _get_text_per_str(self, block, len_str):
        words = block.split(' ')
        res_txt = ''
        str = ''
        while len(str) <= len_str and len(' '.join(words)) >= len_str:
            for word in words:
                if (len(str) + len(word) + 1) <= len_str:
                    str += word + ' '
                else:
                    res_txt += str + '\n'
                    words = words[words.index(word):]
                    str = ''
                    break
        res_txt+=' '.join(words)
        return res_txt


    def _get_font(self, size):
        return ImageFont.truetype("DejaVuSansMono.ttf", size, encoding='utf-8')

    def _get_company(self):
        return 'Название компании: ' + self.compy if self.compy else ''

    def _get_sku(self):
        return '\nАртикул: ' + self.sku if self.sku else ''

    def _get_name(self):
        return '\nНаименование продукции: ' + self.name if self.name else ''

    def _get_field(self):
        return '\nОписание: ' + self.field if self.field else ''

    def _get_shtrich(self):
        a1 = Code(self.number)
        a1.save_code()

    def _create_etich(self):
        img = Image.new('RGBA', (455, 284), 'white')
        idraw = ImageDraw.Draw(img)
        data = tuple(x for x in (self._get_company(), self._get_name(), self._get_sku(), self._get_field()) if x)
        size, len_str = self._get_font_size(data)
        logger.debug('Размеры шрифта (%s, %s); Кол-во символов %s', size, len_str, len(''.join(data)))
        txt = ''.join((self._get_text_per_str(x, len_str) if len(x) >= len_str else x for x in data))
        x, y = 25, 10
        idraw.multiline_text((x,y), text=txt, fill='black', font=self._get_font(size), spacing=2, align='left')
        self._get_shtrich()
        sht = Image.open(dir_name + self.number + '_sht.png', 'r').resize((250, 110))

        img.paste(sht, (102, 170))
        return img

    def save_etich(self):
        img = self._create_etich()
        logger.debug('Создана этикетка с %s для %s', self.number, self.compy)
        img.save(dir_name + self.number + '_et.png')

class Code():
    CODE = 'ean13'

    def __init__(self, number, type='ver', width=0.2, height=20):
        self.type = type
        self.number = str(number)
        self.width = width
        self.height = height
        self.name = dir_name + self.number + "_sht"


    def _generate(self):
        return barcode.get(Code.CODE, self.number, writer=ImageWriter())

    def save_code(self):
        ean = self._generate()
        logger.debug('Создан штрихкод %s', self.number)
        ean.save(self.name,
                 options={'background': 'white', 'module_width': 0.4, 'module_height': 20, 'foreground': 'black',
                          'text_distance': 1, 'font_size': 11})
