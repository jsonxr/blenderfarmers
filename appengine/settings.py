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

from google.appengine.api import app_identity

APP_NAME = app_identity.get_application_id()

# if running in the SDK, set debug=true and more verbose logging
if os.environ.get('SERVER_SOFTWARE').startswith('Development'):
  DEBUG = True
  LOGGING_LEVEL = logging.DEBUG
else:
  DEBUG = False
  LOGGING_LEVEL = logging.INFO

# import local_settings at the end to allow them to override above settings
try:
  from local_settings import *
except ImportError:
  pass # ignore
