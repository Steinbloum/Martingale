class SteinCliIo(object):
  """
  Manages input and output (IO) in the command line interface (CLI).
  """
  def __init__(self):
    # the history of received inputs
    self.input_stack = []
    # the history of printed outputs
    self.output_stack = []

  def print(self, msg, to_stack=True):
    """
    Prints a message to the CLI and appends it to the output stack.

    Parameters:
      - msg (string): message to be printed.
      - to_stack (boolean): whether to append to output_stack
                            defaults to True
    """
    print(msg)
    if to_stack:
      self.output_stack.append(msg)

  def display_welcome(self):
    """
    Displays the welcome text.
    """
    intro = "Hello gambler, you are playing roulette Martingale.\n\n" \
      "Rules are simple, you change colors when you win, you double down if you loose.\n" \
      "Get rich or get rekt trying, can you beat the odds ?\n\n" \
      "Choose an objective, game will continue until objective is met or until you have nothing left.\n"
    self.print(intro)
    self.print_separator()

  def print_separator(self, character="*", length=32, padding=1):
    """
    Prints a visual separator in the CLI.

    Parameters:
      - character (string): the symbol to use as a separator
      - length (integer): the length of the separator
      - padding (integer): number of blank lines above/below separator
    """
    for i in range(padding):
      self.print("", to_stack=True)
    self.print(character * length, to_stack=True)
    for i in range(padding):
      self.print("", to_stack=True)
