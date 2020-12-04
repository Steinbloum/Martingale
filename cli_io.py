class SteinCliIo(object):
  def __init__(self):
    self.stack = []

  def print(self, msg):
    self.stack.append(msg)
    print(msg)
