from __future__ import division
import sys
import pprint
from personalmessages import PersonalMsgsImg

class Img(object):
  
  def __init__(self, width, height, img_name, url, company = "company", klass = "", style = ""):
    """ width and height: at least 1 """
    self.width = width
    self.height = height
    self.img_name = img_name
    self.url = url
    self.company = company
    self.klass = klass
    self.style = style

  def area(self):
    return self.width * self.height

  def html(self, column):
    return ('<!-- {0} --><td colspan="{1}" rowspan="{2}" class="{3}" data-company="{7}">' +\
            '<a href="#"><img src="<?php print $theme_path; ?>/resources/img/customers/{6}" style="{4}"/>' +\
            '</a></td>').format(column, self.width, self.height, self.klass, self.style, self.url, self.img_name, self.company)

class PImg(Img):
  """ Positioned Image"""

  def __init__(self, x, y, img):
    """ @param  img   Img instance """
    super(PImg, self).__init__(
      img.width,
      img.height,
      img.img_name,
      img.url,
      img.company,
      img.klass,
      img.style)
    self.x = x
    self.y = y
    self.img = img

  def x1(self):
    return self.x

  def x2(self):
    return self.x + self.width -1 # -1 because of grid

  def y1(self):
    return self.y
   
  def y2(self):
    return self.y + self.height - 1 # -1 because of grid

  def starts_at(self, x, y):
    return self.x == x and self.y == y

  def contains(self, x, y):
    return x >= self.x1() and x <= self.x2() and y >= self.y1() and y <= self.y2()

  def overlaps(self, pimg):
    return self.x1() <= pimg.x2() and self.x2() >= pimg.x1() and self.y1() <= pimg.y2() and self.y2() >= pimg.y1()

  def cells(self):
    result = []
    for x in range(self.x1(), self.x2()+1):
      for y in range(self.y1(), self.y2()+1):
        result.append({'x': x, 'y': y})
    return result

  def html(self, column):
    return self.img.html(column)

  def __str__(self):
    return "{0} at ({1},{2})".format(self.img_name, self.x, self.y)

class OverlapError(Exception):

  def __init__(self, pimg1, pimg2):
    self.pimg1 = pimg1
    self.pimg2 = pimg2

  def __str__(self):
    return "Overlap between {0} and {1}".format(self.pimg1, self.pimg2)

class OutOfBoundsError(Exception):

  def __init__(self, billboard, pimg):
    self.billboard = billboard
    self.pimg = pimg

  def __str__(self):
    return "{0} falls outside the billboard ({1}x{2})".format(self.pimg, self.billboard.width, self.billboard.height)

def i(s):
  """ Indentation """
  # first cut in lines
  lines = s.split("\n")
  result = []
  for line in lines:
    result.append("          {0}".format(line))
  return "\n".join(result)

def t(s):
  """ Adding tabs """
  return "  {0}".format(s)

class Billboard(object):

  def __init__(self, width = 20, height = 20):
    # array of PImg instances
    self.pimgs = [] 
    self.width = width
    self.height = height
    # array of Personal Message Imgs to which messages can be added
    self.personal_message_imgs = []

  def add(self, img, x, y):
    pimg = PImg(x, y, img)
    overlapping = self.overlaps(pimg)
    if overlapping is not None:
      raise OverlapError(pimg, overlapping)
    if self.falls_outside(pimg):
      raise OutOfBoundsError(self, pimg)
    # all ok, proceed
    self.pimgs.append(pimg)

  def definePersonalMessageSquare(self, x, y):
    pmi = PersonalMsgsImg("{}-{}".format(x,y))
    self.personal_messsage_imgs.append(pmi)
    self.add(pmi,x,y)

  def addPersonalMessage(self, msg):
    for pmi in self.personal_message_imgs:
      if pmi.canTake(msg):
        pmi.addMsg(msg)
        return
    raise Exception("No PersonalMsgsImg found for message {}".format(img))

  def area(self):
    return self.width * self.height

  def cells_filled(self):
    area = 0
    for pimg in self.pimgs:
      area = area + pimg.area()
    return area

  def percentage_cells_filled(self):
    return self.cells_filled() / self.area() * 100

  def overlaps(self, pimg):
    """ Checks whether the given PImg instance overlaps with any other image
        already on the billboard. """
    for other in self.pimgs:
      if other.overlaps(pimg):
        return other
    return None

  def falls_outside(self, pimg):
    return pimg.x2() > self.width or pimg.y2() > self.height

  def occupied_cells(self):
    result = [] 
    for pimg in self.pimgs:
      result.extend(pimg.cells())
    return result

  def generate_html(self, sink = sys.stdout):
    self._generate_head(sink)
    for row in range(1,self.height+1):
      self._generate_row(row, sink)
    self._generate_tail(sink)
    self._generate_occupied_cells(sink)

  def generate_html_to(self, file_name):
    file_name = "billboards/{0}".format(file_name)
    sink = open(file_name, "w")
    self.generate_html(sink)
    sink.close()

  def _generate_row(self, row, sink):
    self._generate_row_head(row, sink)
    for column in range(1,self.width+1):
      self._generate_cell(row, column, sink)
    self._generate_row_tail(row, sink)

  def _generate_cell(self, row, column, sink):
    for pimg in self.pimgs:
      if pimg.contains(column, row): # x is column, y is row !!
        if pimg.starts_at(column, row): # x is column, y is row !!
          # print the pimg itself
          print >> sink, i(t(t(pimg.html(column))))
          return
        else:
          # leave this cell open for the pimg
          print >> sink, i(t(t('<!-- {0} (left empty for {1}) -->'.format(column, pimg))))
          return
    # this is an empty cell    
    print >> sink, i(t(t(('<!-- {0} --><td column="{1}" class="empty">' +\
      '<a href="#">' +\
      '<img src="<?php print $theme_path; ?>/resources/img/<?php echo($billboardImg); ?>" class="billboard-square"/>' +\
      '</a></td>').format(column, column))))

  def _generate_row_head(self, row, sink):
    print >> sink, i(t("<!-- {0} --><tr row=\"{1}\">".format(row, row)))

  def _generate_row_tail(self, row, sink):
    print >> sink, i(t("</tr>"))

  def _generate_head(self, sink):
    print >> sink, i("""<table class="billboard"><!-- {0} squares filled ({1}%) -->
  <tr class="hideMe">
    <!-- Apparantly, there should be an explicit column or colspan does not work correctly.
         Therefore: use a first row of 10 empty cells and just hide it.
         Note: height: 0px; is the correct way to do this, display: none; actually removes the row. -->
    <!-- 1 --><td></td>
    <!-- 2 --><td></td>
    <!-- 3 --><td></td>
    <!-- 4 --><td></td>
    <!-- 5 --><td></td>
    <!-- 6 --><td></td>
    <!-- 7 --><td></td>
    <!-- 8 --><td></td>
    <!-- 9 --><td></td>
    <!-- 10--><td></td>
    <!-- 11--><td></td>
    <!-- 12--><td></td>
    <!-- 13--><td></td>
    <!-- 14--><td></td>
    <!-- 15--><td></td>
    <!-- 16--><td></td>
    <!-- 17--><td></td>
    <!-- 18--><td></td>
    <!-- 19--><td></td>
    <!-- 20--><td></td>
  </tr>""".format(self.cells_filled(), self.percentage_cells_filled()))

  def _generate_tail(self, sink):
    print >> sink, i("</table>")

  def _generate_occupied_cells(self, sink):
    print >> sink, "<script>"
    print >> sink, "var occupiedCells = {0};".format(pprint.pformat(self.occupied_cells()))
    print >> sink, "</script>"
      






