from browser import document, html, window, bind, ajax, console
import json


@bind(document['btn_code'], 'click')
def generate_code(e):
    url = 'http://shtrih.karapasa.ru/generate_code'
    number = document['number'].value
    window.clearHtml()
    if test_number(number):
        data = json.dumps({'number': int(number)})
        ajax.post(url, data=data, oncomplete=output_code)


def output_code(request):
    if request.text == 'error':
        document['hintSht'] <= 'УПС, что-то пошло не так, попробуйте изменить данные'
    else:
        window.resultHtml(1, request.text)
        window.getCoords()


@bind(document['btn_label'],'click')
def generate_label(e):
    url = 'http://shtrih.karapasa.ru/generate_label'
    number = document['number'].value
    compy = document['name'].value
    name = document['product'].value
    sku = document['sku'].value
    field = document['description'].value
    datas = (number, compy, name, sku, field)
    window.clearHtml()
    if test_number(number) and len([x for x in datas if x != '']) > 0:
        data = json.dumps({'number': number,
                           'compy': compy,
                           'name': name,
                           'sku': sku,
                           'field': field})
        ajax.post(url, data=data, oncomlete=output_label)
    elif test_number(number) and len(''.join(datas)) > 700:
        document['hints'] <= 'ВЫ ПРЕВЫСИЛИ ОБЩИЙ ЛИМИТ ЗНАКОВ В 700'
    else:
        document['hints'] <= 'ВЫ НЕ ЗАПОЛНИЛИ НИ ОДНОГО ПОЛЯ!'

def output_label(request):
    if request.text == 'error':
        document['hints'] <= 'УПС, что-то пошло не так. Попробуйте изменить данные!'
    else:
        numberEAN = request.text
        window.resultHtml(2, numberEAN)
        window.getCoords()

def test_number(num):
    if len(num) == 12: return True
    else:
        if num == '': document['hintSht'] <= 'ВЫ НЕ ВВЕЛИ НОМЕР ШТРИХКОДА!'
        else: document['hintSht'] <= 'Введите 12 чисел штрихкода, последний генерируется автоматически'
        return False
