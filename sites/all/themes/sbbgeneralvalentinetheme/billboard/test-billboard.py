from billboard import *

def empty(width, height, color):
  w = width * 30 + (width - 1) * 4
  h = height * 30 + (height - 1) * 4
  return Img(width, height, "empty.png", "#", color, color) # static width would be: "width: {0}px; height: {1}px;".format(w,h)

green = "green"
gray = "gray"
grey = gray
orange = "orange"
blue = "blue"
yellow = "yellow"

class TestBillboard(Billboard):
  """ Class used for representing the testing billboard """
  
  def __init__(self):
    super(TestBillboard, self).__init__()
    self.add(empty(1,1,blue), 9,8)
    self.add(empty(2,2,blue), 12,12)

test_billboard = TestBillboard()
test_billboard.generate_html_to("billboard-test.inc.php")
