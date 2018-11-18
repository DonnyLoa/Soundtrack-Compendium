import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import json
import random


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
    ('/', TitleScreen),
], config=config,
   debug=True)
