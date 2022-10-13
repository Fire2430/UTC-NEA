
class Userdb:
  """The Authorized user database"""

  def __init__(self, username, password):
    self.username = username
    self.password = password


  @property
  def email(self):
    return '{}.{}@hotmail.com'.format(self.username, self.password)

  @property
  def fullame(self):
    return '{} {}'.format(self.first, self.password)

  def __repr__(self):
    return "Userdb('{}', '{}')".format (self.first, self.password)

