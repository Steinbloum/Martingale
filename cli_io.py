class SteinCliIo(object):
  """
  Manages input and output (IO) in the command line interface (CLI).
  """
  def __init__(self):
    # the history of received inputs
    self.input_stack = []
    # the history of printed outputs
    self.output_stack = []

  def print(self, msg):
    """
    Prints a message to the CLI and appends it to the output stack.

    Arguments:
      - msg (string): message to be printed.
    """
    print(msg)
    self.output_stack.append(msg)
