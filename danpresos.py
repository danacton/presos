"""Simple site for storing presentations

Simple site for storing presentations
"""
import webapp2

MAIN_PAGE_HTML = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Dan's presentations</title>
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Open+Sans:regular,semibold,italic,italicsemibold|Droid+Sans+Mono">
    <style>
      body {
        font-family: 'Open Sans', Arial, sans-serif;
        font-size: 12pt;
      }
    </style>
  </head>
  <body>
    <h1>Dan's presentations</h1>
    <ul>
      <li><a href="/namekeepr/index.html">namekeepr: an example application (Scaleconf April 2013, Google I/O Extended May 2013)</a></li>
      <li><a href="/AppEngine101/index.html">Google App Engine 101 (July 2013)</a></li>
      <li><a href="/AppEngine201/index.html">Google App Engine 201 (August 2013)</a></li>
      <li><a href="/HTML5CssResponsive/index.html">Google Cloud Developer Challenge tutorial HTML5, CSS3 and Responsive DEsign(September 2013)</a></li>
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
