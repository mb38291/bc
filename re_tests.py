import re, unittest

aTOM_RE = r"(^(.* )|^|^[',\.\"?])[tT][oO][mM]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
MATT_RE = r"(^(.* )|^|^[',\.\"?])[mM][aA][tT][tT]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
JIM_RE = r"(^(.* )|^|^[',\.\"?])[jJ][iI][mM]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
WADE_RE = r"(^(.* )|^|^[',\.\"?])[wW][aA][dD][eE]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
SHANNON_RE = r"(^(.* )|^|^[',\.\"?])[sS][hH][aA][nN][nN][oO][nN]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
TAYLOR_RE = r"(^(.* )|^|^[',\.\"?])[tT][aA][yY][lL][oO][rR]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"
BUEMI_RE = r"(^(.* )|^|^[',\.\"?])[bB][uU][eE][mM][iI]([',\.\"? ])*(s)*(( .*)$|$|[',\.\"?]+$)"

class TestNamedMentions(unittest.TestCase):
  def test_tom(self):
    name = 'tom'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True,
      f"{name} hit rock bottom.": True,
      f"Has {name} hit rock bottom?": True,
      f"\"to the bottom\"": False,
      f"bottom": False,
      f"tomboy": False,
      f"scuba steve tomson.": False
    }

    for t in tests:
      if tests[t]:
        self.assertRegex(t, TOM_RE)
      else:
        self.assertNotRegex(t, TOM_RE)
  
  def test_matt(self):
    name = 'matt'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True,
      f"{name} says it doesn't matter.": True,
      f"But does it matter?": False,
      f"\"to the dark matter thing\"": False,
      f"Mattock": False,
      f"smatter": False
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, MATT_RE)
      else:
        self.assertNotRegex(t, MATT_RE)

  def test_jim(self):
    name = 'jim'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True,
      f"Don't jimm the camera.": False,
      f"That's thinking with your dipstick Jimmy!": False,
      f"Jimming": False,
      f"jimmy": False
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, JIM_RE)
      else:
        self.assertNotRegex(t, JIM_RE)

  def test_wade(self):
    name = 'wade'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True,
      f"He waded into the water.": False,
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, WADE_RE)
      else:
        self.assertNotRegex(t, WADE_RE)

  def test_shannon(self):
    name = 'shannon'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, SHANNON_RE)
      else:
        self.assertNotRegex(t, SHANNON_RE)

  def test_taylor(self):
    name = 'taylor'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"words {name}'s words": True,
      f"words {name} words": True,
      f"{name}s words": True,
      f"{name}'s words": True,
      f"words {name}s": True,
      f"words {name}'s": True,
      f"words {name}": True
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, TAYLOR_RE)
      else:
        self.assertNotRegex(t, TAYLOR_RE)

  def test_buemi(self):
    name = 'buemi'
    tests = {
      f"{name}": True,
      f"{name}'s": True,
      f"{name}s": True,
      f"{name}?": True,
      f"{name}'s?": True,
      f"{name}'s...?": True,
      f"\"{name}'s?\"": True,
      f"\"To the {name}\"": True,
      f"mom {name} mom": True,
      f"mom {name}'s mom": True,
      f"mom {name} mom": True,
      f"{name}s mom": True,
      f"{name}'s mom": True,
      f"mom {name}s": True,
      f"mom {name}'s": True,
      f"mom {name}": True,
    }
    
    for t in tests:
      if tests[t]:
        self.assertRegex(t, BUEMI_RE)
      else:
        self.assertNotRegex(t, BUEMI_RE)


if __name__ == '__main__':
  unittest.main()
