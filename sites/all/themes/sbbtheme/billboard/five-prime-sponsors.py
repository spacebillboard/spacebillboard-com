from billboard import *

def empty(width, height, color):
  w = width * 30 + (width - 1) * 4
  h = height * 30 + (height - 1) * 4
  return Img(width, height, "empty.png", "#", color, color, "width: {0}px; height: {1}px;".format(w,h))

green = "green"
gray = "gray"
grey = gray
orange = "orange"
blue = "blue"
yellow = "yellow"

class FivePrimeSponsorsBillboard(Billboard):
  """ Class used for representing the example billboard with five
      prime sponsors. """
  
  def __init__(self):
    super(FivePrimeSponsorsBillboard, self).__init__()
    red = Img(5, 5, "example-red-166x166.png", "#", "red-example-company", "red-example-company")    
    blue = Img(5, 5, "example-blue-166x166.png", "#", "blue-example-company", "blue-example-company")
    green = Img(5, 5, "example-166x166.png", "#", "green-example-company", "green-example-company")
    purple = Img(5, 5, "example-purple-166x166.png", "#", "purple-example-company", "purple-example-company")
    yellow = Img(5, 5, "example-yellow-166x166.png", "#", "yellow-example-company", "yellow-example-company")
    self.add(red, 3, 3)
    self.add(green, 13, 3)
    self.add(blue, 8, 8)
    self.add(purple, 3, 13)
    self.add(yellow, 13, 13)
    self.addStdLayout()

  def add(self, img, x, y):
    """Override in order to ignore the overlap error.
       Showroom billboards just add as much as they can."""
    try:    
      super(FivePrimeSponsorsBillboard, self).add(img, x, y)
    except OverlapError:
      pass # ignore

  def addStdLayout(self):
    """ Add the default squares for a 4x3 at (9,8) """
    self.add(empty(3,1,orange), 4, 8)
    self.add(empty(3,1,green), 5, 9)
    self.add(empty(2,2,green), 3, 11)
    self.add(empty(2,2,blue), 6, 10)
    self.add(empty(2,1,green), 7, 8)
    self.add(empty(1,3,gray), 8, 9)
    self.add(empty(1,2,green), 9, 9)
    self.add(empty(2,2,blue), 10, 9)
    self.add(empty(1,2,gray), 12, 9)
    self.add(empty(2,1,green), 7, 12)
    self.add(empty(2,2,orange), 9, 11)
    self.add(empty(1,2,blue), 9, 13)
    self.add(empty(4,1,blue), 11, 11)
    self.add(empty(1,1,grey), 13, 12)
    self.add(empty(2,2,orange), 14, 12)
    self.add(empty(1,1,gray), 17, 12)
    self.add(empty(2,2,blue), 13, 8)
    self.add(empty(3,1,green), 14, 10)
    self.add(empty(1,2,grey), 7, 5)
    self.add(empty(2,1,blue), 6, 7)
    self.add(empty(3,2,orange), 8, 6)
    self.add(empty(1,2,orange), 9, 3)
    self.add(empty(1,1,orange), 13, 10)
    self.add(empty(1,1,gray), 11, 7)
    self.add(empty(1,2,green), 11, 5)
    self.add(empty(1,2,orange), 12, 6)
    self.add(empty(2,1,blue), 13, 5)
    self.add(empty(3,2,grey), 13, 6)
    self.add(empty(1,1,orange), 15, 8)
    self.add(empty(1,1,blue), 16, 4)
    self.add(empty(1,1,green), 4, 5)
    self.add(empty(3,1,orange), 15, 9)
    self.add(empty(2,2,green), 11, 12)
    self.add(empty(1,1,orange), 4, 7)
    self.add(empty(2,1,blue), 13, 9)

five_prime_sponsors_billboard = FivePrimeSponsorsBillboard()
five_prime_sponsors_billboard.generate_html_to("five-prime-sponsors.inc.php")
