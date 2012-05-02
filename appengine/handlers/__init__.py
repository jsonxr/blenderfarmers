# Copyright 2010 Will Norris
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging
import os
import settings

import webapp2
from webapp2_extras import jinja2
from webapp2_extras import json

class AbstractHandler(webapp2.RequestHandler):
  """Abstract base class for all page view classes.  This mainly provides
  convience methods for think like rendering pages and returning JSON
  responses."""

  @webapp2.cached_property
  def _jinja2(self):
    """Returns a Jinja2 renderer cached in the app registry."""
    return jinja2.get_jinja2(app=self.app)

  def _render_template(self, template, **context):
    """Renders a template and returns the result."""
    # setup any necessary default values

    return self._jinja2.render_template(template, **context)

  def _output_template(self, template, **context):
    """Renders a template and writes the result to the response."""
    output = self._render_template(template, **context)
    self.response.write(output)

  def _json_response(self, data={}, callback=None):
    """Serialize a JSON response and write the result to the response.  If
    callback is specified, a JSONP response will be returned."""

    if settings.DEBUG:
      json_options = {
        'separators': (', ', ': '),
        'indent': 2
      }
    else:
      json_options = {}

    json_data = json.encode(data, **json_options)

    if callback:
      self.response.content_type = 'text/javascript'
      output = "%s(%s);" % (callback, json_data)
    else:
      self.response.content_type = 'application/json'
      output = json_data

    self.response.out.write(output)

