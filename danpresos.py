"""Simple site for storing presentations

Simple site for storing presentations
"""
import webapp2

MAIN_PAGE_HTML = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Dan's presentations</title>
  </head>
  <body>
    <h1>Dan's presentations</h1>
    <ul>
      <li><a href="/AppEngine101/index.html">Google App Engine 101</a></li>
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(MAIN_PAGE_HTML)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
