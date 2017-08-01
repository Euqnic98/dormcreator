from google.appengine.ext import ndb
class User(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    color = ndb.StringProperty()
    theme = ndb.StringProperty()
    gender = ndb.StringProperty()
