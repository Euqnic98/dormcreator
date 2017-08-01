#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from model import User
from google.appengine.api import users
import webapp2
import jinja2
import os


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/mainpage.html")
        self.response.write(my_template.render())
class LinkHandler(webapp2.RequestHandler):
    def get(self):
        my_template=jinja_environment.get_template("templates/link.html")
        self.response.write(my_template.render())
class MatchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/matchpage.html")
        self.response.write(template.render())
        render_dict = {}
        render_dict["color"] = "Red"
        Color = self.request.get("color")
        Style = self.request.get("style")
        Gender = self.request.get("gender")



        my_output = User(color = Color, style = Style, gender = Gender)
        my_output.put()
# class SignPage(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             nickname = user.nickname()
#             logout_url = users.create_logout_url('/')
#             greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
#                 nickname, logout_url)
#         else:
#             login_url = users.create_login_url('/')
#             greeting = '<a href="{}">Sign in</a>'.format(login_url)
#
#         self.response.write(
#             '<html><body>{}</body></html>'.format(greeting))
#
#
# class AdminPage(webapp2.RequestHandler):
#     def get(self):
#         user = users.get_current_user()
#         if user:
#             if users.is_current_user_admin():
#                 self.response.write('You are an administrator.')
#             else:
#                 self.response.write('You are not an administrator.')
#         else:
#             self.response.write('You are not logged in.')

    # def Red(self):
# class SubmitHandler(webapp2.RequestHandler):
#     my_template=jinja_environment.get_template("templates/submitpage.html")
#     self.response.write(my_template.render())
app = webapp2.WSGIApplication([
    ('/link', LinkHandler),
    ('/', MainHandler),
    ('/match', MatchHandler)
    # ('/login', SignPage),
    # ('/admin', AdminPage)
], debug=True)
