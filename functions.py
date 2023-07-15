def teams(range1, range2):
  
  import random

  numr1 = random.randint(1, range1)
  numr2 = random.randint(1, range2)
  numr3 = random.randint(1, range1)
  numr4 = random.randint(1, range2)

  r = print(f'R: {numr1}x{numr2} vs. {numr3}x{numr4}==')
  print()

  numl1 = random.randint(1, range1)
  numl2 = random.randint(1, range2)
  numl3 = random.randint(1, range1)
  numl4 = random.randint(1, range2)

  l = print(f'L: {numl1}x{numl2} vs. {numl3}x{numl4}==')
  print()

  numu1 = random.randint(1, range1)
  numu2 = random.randint(1, range2)
  numu3 = random.randint(1, range1)
  numu4 = random.randint(1, range2)

  u = print(f'U: {numu1}x{numu2} vs. {numu3}x{numu4}==')
  print()

  numd1 = random.randint(1, range1)
  numd2 = random.randint(1, range2)
  numd3 = random.randint(1, range1)
  numd4 = random.randint(1, range2)

  d = print(f'D: {numd1}x{numd2} vs. {numd3}x{numd4}==')

  return r, l, u, d

def winners(text):
  
  list = text.split('=')

  r = print(f'R: {list[1]} vs. {list[9]}==')
  print()
  l = print(f'L: {list[3]} vs. {list[11]}==')
  print()
  u = print(f'U: {list[5]} vs. {list[13]}==')
  print()
  d = print(f'D: {list[7]} vs. {list[15]}==')
  print()

  return r, l, u, d

def quarter(text):

  list = text.split('=')

  fight1 = print(f'R: {list[1]} vs. L: {list[3]}=')
  print()
  fight2 = print(f'U: {list[5]} vs. D: {list[7]}=')
  print()

  return fight1, fight2

# Functions alternativas:

'''
def winners(text):
  
  positions = ('R', 'L', 'U', 'D')
  list = text.split('=')
  
  num1 = 0
  num2 = 1
  num3 = 9
  
  for winners in list:

    try:
      print(f'{positions[num1]}: {list[num2]} vs. {list[num3]}=')
      num1 += 1
      num2 += 2
      num3 += 2
    except IndexError:
      break
'''