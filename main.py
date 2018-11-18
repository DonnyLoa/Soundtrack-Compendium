import webapp2
# import jinja2
# import os
# from google.appengine.api import urlfetch
# import json
# import random
# # Copyright 2018 Google LLC
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
#
# # [START gae_python37_app]
# from flask import Flask
#
#
# # If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# # called `app` in `main.py`.
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     # This is used when running locally only. When deploying to Google App
#     # Engine, a webserver process such as Gunicorn will serve the app. This
#     # can be configured by adding an `entrypoint` to app.yaml.
#     app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

#the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a GET request
        self.response.write('Hello, World!') #the response

#the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the MainPage Handler
], debug=True)

def main():
    util.run_wsgi_app(app)

if __name__ == '__main__':
    main()
# import webapp2
# import jinja2
# import os
# from google.appengine.api import urlfetch
# import json
# import random
#
#
# config = {}
# config['webapp2_extras.sessions'] = {
#     'secret_key': 'my-super-secret-key',
# }
#
# app = webapp2.WSGIApplication([
#     ('/', TitleScreen),
# ], config=config,
#    debug=True)
