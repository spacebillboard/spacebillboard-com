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

class ShowroomBillboard(Billboard):
  """ Class used for representing a billboard with a single Image in the 
      center and colored squares around it. """
  
  def __init__(self, img):
    super(ShowroomBillboard, self).__init__()
    # place the image and add additional squares for smaller imgs
    if img.width == 2:
      if img.height == 1:
        # 2x1
        self.add(img, 10, 8)
        self.add(empty(1,1,blue), 9,8)
        self.add(empty(3,1,green), 12,8)
      elif img.height == 3:
        # 2x3
        self.add(img, 10, 8)
        self.add(empty(1,1,blue), 9,8)
        self.add(empty(3,1,green), 12,8)
      elif img.height == 4:
        # 2x4
        self.add(img, 10, 8)
        self.add(empty(1,1,blue), 9,8)
        self.add(empty(1,1,green), 12,8)
        self.add(empty(1,2,orange), 9,11)
        self.add(empty(1,1,grey), 10,12)
        self.add(empty(4,1,blue), 12,11) 
    elif img.width == 3:
      if img.height == 1:
        # 3x1
        self.add(img, 9, 8)
        self.add(empty(1,2,green), 12, 8)
        self.add(empty(3,1,grey), 9, 9)
        self.add(empty(4,1,green), 9, 10)
      elif img.height == 2:
        # 3x2
        self.add(img, 9, 8)
        self.add(empty(1,2,green), 12, 8)
        self.add(empty(1,1,grey), 12, 10)
        self.add(empty(3,1,green), 9, 10)
      elif img.height == 3:
        # 3x3
        self.add(img, 9, 8)
        self.add(empty(1,2,green), 12, 8)
        self.add(empty(1,1,grey), 12, 10)
      elif img.height == 4:
        # 3x4
        self.add(img, 9, 7)
        self.add(empty(1,2,green), 12, 8)
        self.add(empty(1,1,grey), 12, 10)  
        self.add(empty(1,1,orange), 8, 7) 
        self.add(empty(1,1,blue), 8, 6)
        self.add(empty(1,1,green), 9, 6)  
        self.add(empty(1,2,blue), 10, 5)  
    if img.width == 4:
      if img.height == 1:
        # 4x1
        self.add(empty(1,1,grey), 9, 8)
        self.add(empty(2,1,green), 10, 8)
        self.add(empty(1,1,orange), 12, 8)
        self.add(img, 9, 9)
        self.add(empty(2,1,orange), 9, 10)
        self.add(empty(2,1,green), 11, 10) 
      elif img.height == 2:
        # 4x2
        self.add(img, 9, 8)
        self.add(empty(2,1,orange), 9, 10)
        self.add(empty(2,1,green), 11, 10) 
      elif img.height == 3:
        # 4x3
        self.add(img, 9, 8) 
      elif img.height == 4:
        # 4x4
        self.add(img, 9, 8)
        self.add(empty(2,1,orange), 9, 12) 
        self.add(empty(2,1,blue), 13, 11)   
      elif img.height == 5:
        # 4x5
        self.add(img, 9, 7) 
        self.add(empty(1,2,orange), 8, 7) 
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 7, 8)  
        self.add(empty(2,1,orange), 9, 12)  
        self.add(empty(1,2,green), 13, 8)  
        self.add(empty(2,1,blue), 13, 11)  
        self.add(empty(2,2,blue), 8, 5)  
        self.add(empty(1,1,grey), 10, 6)  
        self.add(empty(1,2,orange), 12, 5)  
      elif img.height == 6:
        # 4x6
        self.add(img, 9, 6)   
        self.add(empty(2,1,orange), 9, 12) 
        self.add(empty(1,3,orange), 8, 5) 
        self.add(empty(3,1,blue), 9, 5) 
        self.add(empty(1,1,orange), 12, 5) 
        self.add(empty(2,1,grey), 13, 11) 
    elif img.width == 5:
      if img.height == 1:
        # 5x1
        self.add(img, 9, 9)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10)   
      elif img.height == 2:
        # 5x2
        self.add(img, 8, 8)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,grey), 8, 10)  
        self.add(empty(1,2,green), 13, 8) 
      elif img.height == 3:
        # 5x3
        self.add(img, 8, 8)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,1,grey), 8, 11)  
        self.add(empty(1,2,green), 13, 8) 
      elif img.height == 4:
        # 5x4
        self.add(img, 8, 8)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 7, 8)  
        self.add(empty(2,1,orange), 9, 12)  
        self.add(empty(1,2,green), 13, 8)  
        self.add(empty(2,1,blue), 13, 11)  
      elif img.height == 5:
        # 5x5
        self.add(img, 8, 7)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 7, 8)  
        self.add(empty(2,1,orange), 9, 12)  
        self.add(empty(1,2,green), 13, 8)  
        self.add(empty(2,1,blue), 13, 11)  
        self.add(empty(2,2,blue), 8, 5)  
        self.add(empty(1,1,grey), 10, 6)  
        self.add(empty(1,2,orange), 12, 5)  
      elif img.height == 6:
        # 5x6
        self.add(img, 9, 7)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10)  
        self.add(empty(1,2,orange), 8, 6)  
        self.add(empty(2,2,blue), 9, 5)  
        self.add(empty(3,1,green), 12, 6)  
        self.add(empty(2,1,grey), 14, 7)  
        self.add(empty(1,1,grey), 14, 11) 
        self.add(empty(1,1,orange), 8, 13) 
        self.add(empty(4,1,green), 10, 13)   
    elif img.width == 6:
      if img.height == 1:
        # 6x1
        self.add(img, 8, 9)
        self.add(empty(3,1,blue), 9, 8)  
        self.add(empty(2,1,gray), 12, 8)  
        self.add(empty(1,2,blue), 14, 8)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,2,gray), 8, 10) 
      elif img.height == 2:
        # 6x2
        self.add(img, 8, 8)   
        self.add(empty(1,2,blue), 14, 8)
        self.add(empty(1,1,grey), 7, 8)
        self.add(empty(1,2,grey), 8, 10)
        self.add(empty(3,1,green), 9, 10)
        self.add(empty(1,1,grey), 12, 10)
        self.add(empty(1,1,green), 8, 6)
        self.add(empty(1,1,orange), 8, 7)
        self.add(empty(2,2,blue), 9, 6)
        self.add(empty(2,2,grey), 12, 6)
        self.add(empty(2,2,green), 14, 6) 
        self.add(empty(1,2,orange), 8, 9)
        self.add(empty(1,1,green), 13, 9) 
      elif img.height == 3:
        # 6x3
        self.add(img, 8, 7)   
        self.add(empty(1,2,blue), 14, 8)
        self.add(empty(1,1,grey), 7, 8)
        self.add(empty(1,1,grey), 8, 11)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(2,2,green), 14, 6) 
        self.add(empty(2,1,green), 8, 10)
        self.add(empty(3,1,grey), 10, 10)
      if img.height == 4:
        # 6x4
        self.add(img, 8, 7)   
        self.add(empty(1,2,blue), 14, 8)
        self.add(empty(1,1,grey), 7, 8)
        self.add(empty(1,1,grey), 8, 11)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(2,2,green), 14, 6) 
      if img.height == 5:
        # 6x5
        self.add(img, 8, 7)   
        self.add(empty(1,2,blue), 14, 8)
        self.add(empty(1,1,grey), 7, 8)
        self.add(empty(1,1,grey), 8, 11)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(2,2,green), 14, 6)
        self.add(empty(2,1,orange), 9, 12)
        self.add(empty(1,1,blue), 14, 11)
      if img.height == 6:
        # 6x6
        self.add(img, 8, 7)   
        self.add(empty(1,2,blue), 14, 8)
        self.add(empty(1,1,grey), 7, 8)
        self.add(empty(1,1,grey), 8, 11)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(2,2,green), 14, 6)
        self.add(empty(2,1,orange), 9, 12)
        self.add(empty(1,1,blue), 14, 11)
    elif img.width == 9:
      if img.height == 1:
        self.add(img, 6, 8) 
      elif img.height == 2:
        self.add(img, 6, 8)
        self.add(empty(1,2,green), 5, 7)
        self.add(empty(2,2,orange), 4, 9)
        self.add(empty(1,2,grey), 8, 10)
        self.add(empty(4,1,green), 9, 10)
    elif img.width == 7:
      if img.height == 1:
        # 7x1
        self.add(img, 8, 9)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
      elif img.height == 2:
        # 7x2
        self.add(img, 8, 8)
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10)  
      elif img.height == 3:
        # 7x3
        self.add(img, 8, 8)
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 8, 11)  
        self.add(empty(2,2,green), 15, 10)   
      elif img.height == 4:
        # 7x4
        self.add(img, 8, 7)
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 8, 11)  
        self.add(empty(2,2,green), 15, 10)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(4,1,green), 14, 6)
        self.add(empty(2,1,blue), 15, 7) 
      elif img.height == 5:
        # 7x5
        self.add(img, 8, 7)
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(1,1,grey), 8, 11)  
        self.add(empty(2,2,green), 15, 10)
        self.add(empty(1,1,green), 8, 5)
        self.add(empty(1,1,orange), 8, 6)
        self.add(empty(2,2,blue), 9, 5)
        self.add(empty(2,1,grey), 12, 6)
        self.add(empty(4,1,green), 14, 6)
        self.add(empty(2,1,blue), 15, 7)
    elif img.width == 8:
      if img.height == 2:
        # 8x2
        self.add(img, 7, 8)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10)  
        self.add(empty(2,1,green), 5, 9)  
      elif img.height == 3:
        # 8x3
        self.add(img, 7, 8)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(2,2,green), 15, 10)  
        self.add(empty(2,2,blue), 5, 9)  
        self.add(empty(3,1,green), 6, 11)  
      elif img.height == 6:
        # 8x6
        self.add(img, 7, 7)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)  
        self.add(empty(1,2,orange), 8, 10)  
        self.add(empty(4,1,green), 9, 10) 
        self.add(empty(2,2,green), 15, 10)  
        self.add(empty(2,2,blue), 5, 9)  
        self.add(empty(3,1,green), 6, 11) 
    elif img.width == 10:
      if img.height == 2:
        # 10x2
        self.add(img, 6, 8)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)    
        self.add(empty(2,3,blue), 16, 7)   
        self.add(empty(2,2,grey), 4, 9)    
        self.add(empty(1,2,grey), 8, 10)   
        self.add(empty(4,1,green), 9, 10)  
      if img.height == 10:
        # 10x10
        self.add(img, 6, 5)
        self.add(empty(2,1,green), 8, 8) 
        self.add(empty(3,1,orange), 10, 8)  
        self.add(empty(2,1,blue), 13, 8)   
        self.add(empty(4,1,blue), 8, 7)  
        self.add(empty(1,1,gray), 7, 8)    
        self.add(empty(2,3,blue), 16, 7)   
        self.add(empty(2,2,grey), 4, 9)    
        self.add(empty(1,2,grey), 8, 10)   
        self.add(empty(4,1,green), 9, 10)  
    # check whether everything went right  
    if len(self.pimgs) == 0:
      print "WARNING: unknown size given: ({0}, {1})".format(img.width, img.height)
    # add the other imgs
    self.addStdLayout()

  def add(self, img, x, y):
    """Override in order to ignore the overlap error.
       Showroom billboards just add as much as they can."""
    try:    
      super(ShowroomBillboard, self).add(img, x, y)
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
