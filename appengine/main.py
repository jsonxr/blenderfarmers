import imports  # Must be imported first to fix the import path

import logging
import settings
import webapp2

logging.getLogger().setLevel(settings.LOGGING_LEVEL)
logging.debug('Initializing.')

routes = [
  ('/', "handlers.home.HomeHandler"),
]

config = {}

app = webapp2.WSGIApplication(routes=routes, debug=settings.DEBUG,
    config=config)
