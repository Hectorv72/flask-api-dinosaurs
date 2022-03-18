class Dinosaur(object):
  
  def __init__(self,set_name):
    self.name = set_name
  
  def toDict(self):
    return self.__dict__