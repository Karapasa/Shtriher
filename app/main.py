from aiohttp import web
from .views import routes
import aiohttp_jinja2
import jinja2
import pathlib

TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'

async def create_app():
    app = web.Application()
    app.add_routes(routes)
    app.add_routes([web.static('/static', 'app/static')])
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATES_ROOT))
    return app