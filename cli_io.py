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

  def display_welcome(self):
    intro = "Hello gambler, you are playing roulette Martingale.\n\n" \
      "Rules are simple, you change colors when you win, you double down if you loose.\n" \
      "Get rich or get rekt trying, can you beat the odds ?\n\n" \
      "Choose an objective, game will continue until objective is met or until you have nothing left.\n" \
      "******************************************"
    self.print(intro)
