import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.hat = kwargs
    self.contents = []
    for color, nbr in kwargs.items():
      for i in range(0, nbr):
        self.contents.append(color)

  def draw(self, nbr):
    draw = []
    if (int(nbr) > int(len(self.contents))):
      return self.contents
    else:
      for i in range(0, nbr):
        draw.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
    return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(0, num_experiments):
    hatcopy = copy.deepcopy(hat)
    draw = hatcopy.draw(num_balls_drawn)
    verif = True
    for expected, nbr in expected_balls.items():
      if (draw.count(expected) < nbr):
        verif = False
    if (verif):
      M += 1
  return M/num_experiments