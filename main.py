import asyncio
import os
import logging
from handlers import urls

from tornado.web import Application
from tornado.options import define, options, parse_command_line

# options for running the server
define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


def make_app():
    _loger = logging.getLogger(__name__)
    parse_command_line()
    _loger.info(f"App started with options: {options}")
    return Application(urls,
                       cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
                       template_path=os.path.join(os.path.dirname(__file__), "templates"),
                       static_path=os.path.join(os.path.dirname(__file__), "static"),
                       xsrf_cookies=True,
                       debug=options.debug,
                       )


async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    asyncio.run(main())
