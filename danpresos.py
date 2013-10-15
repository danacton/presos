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
      <li><b><a href="/namekeepr/index.html">namekeepr: an example application</a></b> (<a href="http://www.scaleconf.org">Scaleconf</a> April 2013, Google I/O Extended May 2013)</li>
      <li><b><a href="/AppEngine101/index.html">Google App Engine 101</a></b> (<a href="https://developers.google.com/groups/chapter/106505752730493822675/">Wits Google Developer Group</a>, July 2013)</li>
      <li><b><a href="/AppEngine201/index.html">Google App Engine 201</a></b> (<a href="https://developers.google.com/groups/chapter/106505752730493822675/">Wits Google Developer Group</a>, August 2013)</li>
      <li><b><a href="/HTML5CssResponsive/index.html">HTML5, CSS3 and Responsive Design</a></b> (<a href="http://www.google.com/events/gcdc2013/">Google Cloud Developer Challenge</a>, September 2013)</li>
      <li><b><a href="/IntroToAppEngine/index.html">Introduction to App Engine</a></b> (<a href="http://www.google.com/events/gcdc2013/">Google Cloud Developer Challenge</a>, September 2013)</li>
      <li><b><a href="/AppEnginePHP/index.html">A quick start guid to PHP on App Engine</a></b> (<a href="http://www.google.com/events/gcdc2013/">Google Cloud Developer Challenge</a>, September 2013)</li>
      <li><b><a href="/AppEngineForStartups/index.html">App Engine for startups</a></b> (<a href="http://www.88mph.ac/">88mph</a> Nairobi Startup Bootcamp, October 2013)</li>
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
