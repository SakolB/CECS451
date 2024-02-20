import random


class Guess_The_Box():
  """
  The game class
  """

  def __init__(self):
    box = ['Empty', 'Empty', 'Prize']
    random.shuffle(box)
    self.boxes = box

  def get_hint(self, guess):
    hints = [i for i, x in enumerate(self.boxes) if x == 'Empty']
    if guess in hints:
      hints.remove(guess)

    return hints[0]



def main():
  
  experiments = 10000
  probabilities = []
  win_count = 0
  
  #10000 run for switching box
  for i in range(experiments):
      win_count+=play_the_game(1)

  probabilities.append(win_count/float(experiments))
  #reset win count
  win_count = 0
  
  #10000 run for holding box
  for i in range(experiments):
      win_count+=play_the_game(0)

  probabilities.append(win_count/float(experiments))

  print('Win probability when switching the choice:', probabilities[0])
  print('Win probability when sticking with the choice:', probabilities[1])
  return


#strategy 1 = switch, 0 = hold
#return 1 if won, return 0 if false
def play_the_game(strategy):
  initial_choice = random.randint(0, 2)
  b1 = Guess_The_Box()
  new_choice = initial_choice
  if(strategy):
    new_choice = 3 - initial_choice - b1.get_hint(initial_choice)
  if b1.boxes[new_choice] == 'Prize':
    return 1
  return 0  



if __name__ == "__main__":
  main()
