import webapp2
import jinja2
import os
from webapp2_extras import sessions
# from flask import Flask, render_template, request
# from flask import flask

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(BaseHandler):
    def get(self):
        main_template = jinja_env.get_template('templates/index.html')
        self.response.write('Hello, World!')

        name = self.request.get("name")    # name
        self.session['name'] = name

        self.response.write(main_template.render(name=name))

    def post(self):
        main_template = jinja_env.get_template('templates/index.html')
        self.response.write('Inputted text: ' % self.request.get('name'))

        name = self.request.get("name")    # Category
        self.session['name'] = name

        self.response.write(main_template.render(name=name))

class Results(BaseHandler):
    def get(self):
        results_template = jinja_env.get_template('templates/submitted_form.html')
        self.response.write('Inputted text: ' % self.request.get('name')')

        name = self.request.get("name")    # Category
        self.session['name'] = name

        self.response.write(results_template.render(name=name))
    def post(self):
        results_template = jinja_env.get_template('templates/submitted_form.html')
        self.response.write('Inputted text: ' % self.request.get('name'))

        name = self.request.get("name")    # Category
        self.session['name'] = name

        self.response.write(results_template.render(name=name))

# def main():
#     util.run_wsgi_app(app)
#
# if __name__ == '__main__':
#     main()
# app = Flask(__name__)
# @app.route('/')
# def form():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)

# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']
#
#     return render_template(
#         'submitted_form.html',
#         name=name,
#         email=email,
#         site=site,
#         comments=comments)
#
# @app.route('/submitted', methods=['GET'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']
#
#     return render_template(
#         'submitted_form.html',
#         name=name,
#         email=email,
#         site=site,
#         comments=comments)

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/results', Results)
], config=config,
   debug=True)
