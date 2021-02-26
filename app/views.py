from aiohttp import web
import aiohttp_jinja2
routes = web.RouteTableDef()
from .utils import Etich, Code


@routes.get('/')
@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}

@routes.post('/generate_code')
async def post_index(request):
    num = await request.json()
    Code(num['number']).save_code()
    return web.Response(text='')
@routes.post('/generate_label')
async def post_index(request):
    data = await request.json()
    Etich(**data).save_etich()
    return web.Response(text='')
