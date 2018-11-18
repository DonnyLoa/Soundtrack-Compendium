import webapp2

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
