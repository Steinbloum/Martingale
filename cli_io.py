from time import sleep

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


  def display_game_start(self, initial_bet):
    """
    Displays the game start text.

    Parameters:
      - initial_bet (object): an object containing the bankroll, objective
                              bet value and bet color
    """
    self.print_separator()
    self.print(
      "You sit at the table with {}$, your objective is to make {}$." \
      " Your first bet is {}$ on {}".format(
        initial_bet.get_bankroll(),
        initial_bet.get_objective(),
        initial_bet.get_value(),
        initial_bet.get_color()
      )
    )
    self.print_separator()
    sleep(3)
    self.print_countdown(3)
    self.print("*********HERE WE GO*********", to_stack=False)

  def print_countdown(self, duration):
    """
    Prints a countdown.

    Parameters:
      - duration (integer): the amount of seconds for the countdown.
    """
    for i in range(duration):
      self.print(duration - i, to_stack=False)
      sleep(1)


  def print_separator(self, character="*", length=32, padding=1):
    """
    Prints a visual separator in the CLI.

    Parameters:
      - character (string): the symbol to use as a separator
      - length (integer): the length of the separator
      - padding (integer): number of blank lines above/below separator
    """
    for i in range(padding):
      self.print("", to_stack=False)
    self.print(character * length, to_stack=False)
    for i in range(padding):
      self.print("", to_stack=False)

class Betsetup:

  """set the initial bet"""

  def __init__(self):
    self.stack = 0
    self.objective = 0
    self.color = 0
    self.value = 0

  def get_stack(self):
    return self.stack

  def set_stack(self, amount):
    self.stack = amount

  def get_objective(self):
    return self.objective

  def set_objective(self, amount):
    self.objective = amount

  def get_color(self):
    return self.color

  def set_color(self, color):
    self.color = color

  def get_value(self):
    return self.value

  def set_value(self, amount):
    self.value = amount

