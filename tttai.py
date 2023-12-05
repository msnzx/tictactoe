import tttlibgpt, random

def randombotmove(mySpaces:set,opponentSpaces:set) -> str:
  """Get a random Tictactoe move"""
  availableMoves=tttlib.getValidMoves(mySpaces|opponentSpaces)
  return random.choice(list(availableMoves))