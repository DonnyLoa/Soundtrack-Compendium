import webapp2
# from flask import flask

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World!')

# def main():
#     util.run_wsgi_app(app)
#
# if __name__ == '__main__':
#     main()

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
