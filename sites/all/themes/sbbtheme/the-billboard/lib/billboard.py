from __future__ import division
import sys
import pprint
import os
import subprocess
import math
import cgi

EMPTY_BORDER_WIDTH = 10

def UTF8len(s):
  return len(s)
#  return len(s.decode("utf-8"))

######################################
# IMAGES
######################################

class Img(object):
  
  def __init__(self, width, height, company_label, url, klass = "", style = ""):
    """ width and height: at least 1 """
    self.width = width
    self.height = height
    self.company_label = company_label
    self.url = url
    self.klass = klass
    self.style = style

  def area(self):
    return self.width * self.height

  def html(self, column):
    return ('<!-- {0} --><td colspan="{1}" rowspan="{2}" class="{3}" data-company="{6}">' +\
            '<a href="{5}" target="_new"><img src="<?php sbb_echo_theme_file("resources/img/the-billboard/{6}.png"); ?>" style="{4}"/>' +\
            '</a></td>').format(column, self.width, self.height, self.klass, self.style, self.url, self.company_label)

  def final(self, row, column):
    width = (self.width*30 + (self.width-1)*4)*10
    height = (self.height*30 + (self.height-1)*4)*10
    return """<image xlink:href="file:///home/maartend/htdocs/spacebillboard/docroot/sites/all/themes/sbbtheme/resources/img/the-billboard/{0}.png" x="{1}" y="{2}" width="{3}" height="{4}" id="" />""".format(self.company_label, x(column), y(row), width, height)

class PImg(Img):
  """ Positioned Image"""

  def __init__(self, row, column, img):
    """ @param  img   Img instance """
    super(PImg, self).__init__(
      img.width,
      img.height,
      img.company_label,
      img.url,
      img.klass,
      img.style)
    self.column = column
    self.row = row
    self.img = img

  def column1(self):
    return self.column

  def column2(self):
    return self.column + self.width -1 # -1 because of grid

  def row1(self):
    return self.row
   
  def row2(self):
    return self.row + self.height - 1 # -1 because of grid

  def starts_at(self, row, column):
    return self.column == column and self.row == row

  def contains(self, row, column):
    return column >= self.column1() and column <= self.column2() and row >= self.row1() and row <= self.row2()

  def overlaps(self, pimg):
    return self.column1() <= pimg.column2() and self.column2() >= pimg.column1() and self.row1() <= pimg.row2() and self.row2() >= pimg.row1()

  def cells(self):
    result = []
    for column in range(self.column1(), self.column2()+1):
      for row in range(self.row1(), self.row2()+1):
        result.append({'column': column, 'row': row})
    return result

  def html(self, column):
    return self.img.html(column)

  def final(self, row, column):
    return self.img.final(row, column)

  def __str__(self):
    return "{0} at ({1},{2})".format(self.company_label, self.row, self.column)




######################################
# EXCEPTIONS
######################################

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




######################################
# HELPER METHODS
######################################

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

def x(column):
  """ Returns the coordinates for the left side of a certain column on the billboard. """
  return (column-1) * 34 * 10

def y(row):
  """ Returns the coordinates for *the top* of a certain column on the billboard. """
  return (row-1) * 34 * 10


######################################
# NORMAL BILLBOARD
######################################

class Billboard(object):

  def __init__(self, width = 20, height = 20):
    # array of PImg instances
    self.pimgs = [] 
    self.width = width
    self.height = height
    # array of Personal Message Imgs to which messages can be added
    self.personal_message_imgs = []
    self.message_to_square = {}

  def add(self, img, row, column):
    pimg = PImg(row, column, img)
    overlapping = self.overlaps(pimg)
    if overlapping is not None:
      raise OverlapError(pimg, overlapping)
    if self.falls_outside(pimg):
      raise OutOfBoundsError(self, pimg)
    # all ok, proceed
    self.pimgs.append(pimg)

  def definePersonalMessageSquare(self, row, column):
    pmi = PersonalMsgsImg("{}-{}".format(row,column))
    self.personal_message_imgs.append(pmi)
    self.add(pmi,row,column)

  def addPersonalMessage(self, msg_id, msg):
    msg = msg.decode('UTF-8')
    for pmi in self.personal_message_imgs:
      if pmi.canTake(msg):
        pmi.addMsg(msg)
        self.message_to_square[msg_id] = pmi.label
        return
    raise Exception("No PersonalMsgsImg found for message \"{}\"".format(msg))

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
    return pimg.column2() > self.width or pimg.row2() > self.height

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
      if pimg.contains(row, column): 
        if pimg.starts_at(row, column): 
          # print the pimg itself
          print >> sink, i(t(t(pimg.html(column))))
          return
        else:
          # leave this cell open for the pimg
          print >> sink, i(t(t('<!-- {0} (left empty for {1}) -->'.format(column, pimg))))
          return
    # this is an empty cell    
    print >> sink, i(t(t(('<!-- {0} --><td column="{1}" class="empty"><img src="<?php sbb_echo_theme_file("resources/img/empty-square-with-border.png"); ?>" class="billboard-square"/></a></td>').format(column, column))))

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

  def generate_personal_message_squares(self):
    """ Generates the HTML for the personal message squares. """
    for pmi in self.personal_message_imgs:
      pmi.generateImage()
      #pmi.generateHTML()

  def generate_personal_messages_list(self):
    """ Returns msg2square.inc.php """
    first = True
    s = "<?php $msg2square = array(\n"
    for msg, square in self.message_to_square.iteritems():
      if not first:
        s += ",\n"
      else:
        first = False
      s += """  "{0}" => "{1}" """.format(msg, square)
    s += "\n);"
    return s

  def generate_personal_messages_squares_list_js(self):
    """ Returns pmsgs_js.inc.php """
    
    first = True
    s = "var personalMessageSquares = [];\n"
    for square in self.personal_message_imgs:
      s += """personalMessageSquares.push("<?php sbb_echo_theme_file('resources/img/personal-msgs/{0}-{1}.png'); ?>");\n""".format(square.label, square.filled())
    return s

  def generate_final(self, sink = sys.stdout):
    self._generate_final_head(sink)
    for row in range(1,self.height+1):
      for column in range(1,self.width+1):
        self._generate_final_cell(row, column, sink)
    self._generate_final_tail(sink)

  def generate_final_to(self, file_name):
    sink = open(file_name, "w")
    self.generate_final(sink)
    sink.close()

  def _generate_final_cell(self, row, column, sink):
    for pimg in self.pimgs:
      if pimg.contains(row, column): 
        if pimg.starts_at(row, column): 
          # print the pimg itself
          print >> sink, t(t(pimg.final(row, column)))
          return
        else:
          # leave this cell open for the pimg
          print >> sink, t(t('<!-- ({0},{1}) (left empty for {2}) -->'.format(column, row, pimg)))
          return
    # this is an empty cell    
    print >> sink, t(t(('<!-- ({0},{1}) --><rect width="{5}" height="{5}" x="{2}" y="{3}" id="" style="fill:none;stroke:#cecece;stroke-opacity:1;stroke-width:{4}" />').format(column, row, x(column)+EMPTY_BORDER_WIDTH/2, y(row)+EMPTY_BORDER_WIDTH/2, EMPTY_BORDER_WIDTH, 300-EMPTY_BORDER_WIDTH)))

  def _generate_final_head(self, sink):
    print >> sink, """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="6760" height="6760" id="svg2">"""

  def _generate_final_tail(self, sink):
    print >> sink, "</svg>"

######################################
# PREFERRED SQUARES BILLBOARD
######################################
      
class PreferredSquaresBillboard(Billboard):
  """ Class used for representing the billboard to select preferred squares in the Buy Squares form."""

  def _generate_cell(self, row, column, sink):
    for pimg in self.pimgs:
      if pimg.contains(row, column):
        print >> sink, i(t(t(('<!-- {0} --><td column="{0}" class="taken"></td>').format(column))))
        return 
    # this is an empty cell    
    print >> sink, i(t(t(('<!-- {0} --><td column="{0}" class="empty"></td>').format(column,))))

  def _generate_head(self, sink):
    print >> sink, i("""<table class="preferred-squares"><!-- {0} squares filled ({1}%) -->
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

  def generate_personal_message_squares(self):
    raise Exception("This should never be called")



######################################
# PERSONAL MESSAGES
######################################

class PersonalMsgsImg(Img):
    
  def __init__(self, label):
    """ label: the label of this personal-msg-square, which will be used to generate
        the svg and png into <label>.svg and <label>.png """
    super(PersonalMsgsImg, self).__init__(1,1,"","")
    self.label = label
    self.msgs = []

  def totalCapacity(self):
    """ Returns the maximum capacity of this PMI in #characters """
    return 50 * 50

  def filled(self):
    """ Returns the amount of characters already in this PMI """
    # map each message to its length and take the sum of the resulting array
    total = sum(map(UTF8len, self.msgs))
    return total

  def capacityLeft(self):
    """ Returns the number of empty characters left in this PMI """
    capacity = self.totalCapacity() - self.filled()
    return capacity

  def canTake(self, msg):
    """ Returns whether this PMI can take in the given message, i.e.,
        returns whether this PMI has enough capacity left to add the
        given message. """
    return self.capacityLeft() >= UTF8len(msg) and not self.capacityLeft() == 106 # hard-coded for the error with UTF8...

  def isEmpty(self):
    """ Returns whether this PMI is still empty """
    return self.filled() == 0

  def addMsg(self, msg):
    """ Adds a message to this PMI """
    if(not self.canTake(msg)):
      raise OutOfCapacityError(self, msg)
    self.msgs.append(msg)

  def html(self, column):
    if self.isEmpty():
      return ('<!-- {0} --><td column="{1}" class="empty">' +\
      '<a href="#">' +\
      '<img src="<?php sbb_echo_theme_file("resources/img/empty-square-with-border.png"); ?>" class="billboard-square"/>' +\
      '</a></td>').format(column, column)
    else:
      percentage = (self.filled() / self.totalCapacity()) * 100
      rounded = int(math.ceil(percentage / 20) * 20) # for five levels
      return ('<!-- {0} --><td class="personal-msg {1}" data-msg-label="{2}" data-zoom-image="<?php sbb_echo_theme_file("resources/img/personal-msgs/{2}-{4}.png"); ?>">' +\
            '<a href="#"><img src="<?php sbb_echo_theme_file("resources/img/personal-msgs/small-{3}.png"); ?>"/>' +\
            '</a></td>').format(column, self.klass, self.label, rounded, self.filled())

  def generateImage(self):
    self.generateImageTo("../resources/img/personal-msgs/")

  def generateImageTo(self, path):
    """ @param path String  The path of the FOLDER in which to generate the SVG. """
    if self.isEmpty():
      return
    # we are not empty => generate SVG and PNG
    cwd = os.getcwd()
    os.chdir(path)
    svg = PersonalMessageSVG()
    for msg in self.msgs:
      svg.addMsg(msg)
    # output SVG
    with open("{}.svg".format(self.label), 'w+') as sink:
      sink.write(svg.toSVG())
    # convert SVG to PNG
    subprocess.call("inkscape -f {}.svg --export-png {}-{}.png --export-width 1000 --export-height 1000".format(self.label, self.label, self.filled()), shell=True)
    # revert cwd
    os.chdir(cwd)

  def generateHTML(self):
    self.generateHTMLTo("generated/pmsg-squares/")

  def generateHTMLTo(self, path):
    """ @param path String  The path of the FOLDER in which to generate the SVG. """
    if self.isEmpty():
      return
    # we are not empty => generate HTML
    cwd = os.getcwd()
    os.chdir(path)
    svg = PersonalMessageSVG()
    for msg in self.msgs:
      svg.addMsg(msg)
    # output HTML
    with open("{}.inc".format(self.label), 'w+') as sink:
      sink.write(svg.toHTML())
    # revert cwd
    os.chdir(cwd)

  def generateSVGTo(self, path):
    raise Exception()

  def final(self, row, column):
    if self.isEmpty():
      print >> sink, i(t(t(('<!-- ({0},{1}) --><rect width="{5}" height="{5}" x="{2}" y="{3}" id="" style="fill:none;stroke:#cecece;stroke-opacity:1;stroke-width:{4}" />').format(column, row, x(column)+EMPTY_BORDER_WIDTH/2, y(row)+EMPTY_BORDER_WIDTH/2, EMPTY_BORDER_WIDTH, 300-EMPTY_BORDER_WIDTH))))
    # we are not empty
    svg = PersonalMessageSVG()
    for msg in self.msgs:
      svg.addMsg(msg)
    return svg.toFinalSVG(row, column)

class LineSegment:
  """ Class used for representing a text segment in a line in the SVG.
      This results in an unpositioned <tspan> of a certain color in the SVG. """
  
  def __init__(self, text, color):
    self.color = color
    self.text = text

  def toSVG(self):
    text = cgi.escape(self.text)
    return '<tspan style="fill:{0};fill-opacity:1" id="tspan4499">{1}</tspan>'.format(self.color, text.encode('ascii', 'xmlcharrefreplace'))

  def toHTML(self):
    text = cgi.escape(self.text)
    return '<span style="color: {0};">{1}</span>'.format(self.color, text)

class Line:
  """ Class used for building a line in the SVG.
      This results in a positioned <tspan> without color in the SVG. """

  def __init__(self, x, y):
    self.segments = []
    self.x = x
    self.y = y
    self.total = 0

  def addText(self, text, color = "#000000"):
    """ Adds a segment with the containing text of the containing color to this line. """
    self.segments.append(LineSegment(text, color))
    self.total += UTF8len(text)

  def toSVG(self):
    svg = '<tspan sodipodi:role="line" x="{0}" y="{1}" style="text-align:start;line-height:100%;text-anchor:start">'.format(self.x, self.y)
    for segment in self.segments:
      svg += segment.toSVG()
    svg += '</tspan>'
    return svg

  def toHTML(self):
    html = '<div>'
    for segment in self.segments:
      html += segment.toHTML()
    html += '</div>\n'
    return html

  def toFinalSVG(self):
    allText = ''.join(map(lambda x: x.text, self.segments))
    allText = cgi.escape(allText)
    svg = """    <tspan x="{0}" y="{1}" style="font-size:7px;text-align:start;line-height:86.00000143%;letter-spacing:-1px;text-anchor:start;fill:#000000">{2}</tspan>
""".format(self.x, self.y, allText)
    return svg

class PersonalMessageSVG:
  """ Class used for building the SVG showing multiple personal messages """

  def __init__(self):
    self.color1 = "#ff7f2a"
    self.color2 = "#0086d7"
    self.active_color = self.color1
    self.msgs = []

  def nbCharacters(self):
    return sum(map(UTF8len, self.msgs))

  def switchColor(self):
    if self.active_color == self.color1:
      self.active_color = self.color2
    else:
      self.active_color = self.color1

  def addMsg(self, msg):
    self.msgs.append(msg)

  def toSVG(self):
    # check to be sure
    if self.nbCharacters() > 2500:
      raise Exception("This PersonalMessageSVG has been filled too much: {0}".format(self.nbCharacters()))
    # build the lines according to the messages
    lines = []
    x = -3.3159637
    y = 119.12654
    if len(self.msgs) > 0:
      lines.append(Line(x,y))
    for msg in self.msgs:
      line = lines[-1]
      while True:
        if line.total + UTF8len(msg) <= 50: 
          # add the complete message
          line.addText(msg, self.active_color)
          break
        else:
          # split the message and start a new line
          capacity = 50 - line.total
          line.addText(msg[:capacity], self.active_color) 
          # create the new line
          y += 20
          line = Line(x,y)
          lines.append(line)
          msg = msg[capacity:]
          # the rest will be added in the new iteration
      self.switchColor()
    # now build and return the SVG representing these lines
    s = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:svg="http://www.w3.org/2000/svg" width="1000" height="1000" id="svg3801" version="1.1" inkscape:version="0.48.5 r10040" sodipodi:docname="drawing.svg">
  <defs id="defs3803" />
  <sodipodi:namedview id="base" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="0.49497475" inkscape:cx="619.53984" inkscape:cy="383.01384" inkscape:document-units="px" inkscape:current-layer="layer1" showgrid="false" inkscape:window-width="1600" inkscape:window-height="834" inkscape:window-x="0" inkscape:window-y="27" inkscape:window-maximized="1" />
  <metadata id="metadata3806">
    <rdf:RDF>
      <cc:Work rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g inkscape:label="Layer 1" inkscape:groupmode="layer" id="layer1" transform="translate(3.3159637,-101.00154)">
    <text xml:space="preserve" style="font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:100%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Square;-inkscape-font-specification:Square" x="-3.3159637" y="119.12654" id="text3809" sodipodi:linespacing="100%">
"""
    for line in lines:
      s += line.toSVG()
    s += """</text>
  </g>
</svg>"""
    return s

  def toHTML(self):
    # check to be sure
    if self.nbCharacters() > 2500:
      raise Exception("This PersonalMessageSVG has been filled too much: {0}".format(self.nbCharacters()))
    # build the lines according to the messages
    lines = []
    if len(self.msgs) > 0:
      lines.append(Line(0,0)) # coordinates do not matter for HTML
    for msg in self.msgs:
      line = lines[-1]
      while True:
        if line.total + len(msg) <= 50:
          # add the complete message
          line.addText(msg, self.active_color)
          break
        else:
          # split the message and start a new line
          capacity = 50 - line.total
          line.addText(msg[:capacity], self.active_color) 
          # create the new line
          line = Line(0,0) # coordinates do not matter for HTML
          lines.append(line)
          msg = msg[capacity:]
          # the rest will be added in the new iteration
      self.switchColor()
    # now build and return the HTML representing these lines
    s = '<div class="pmsg-contents">\n'
    for line in lines:
      s += "  " + line.toHTML()
    s += "</div>"
    return s

  def toFinalSVG(self, row, column):
    # check to be sure
    if self.nbCharacters() > 2500:
      raise Exception("This PersonalMessageSVG has been filled too much: {0}".format(self.nbCharacters()))
    # build the lines according to the messages
    lines = []
    _x = 0
    _y = 6
    if len(self.msgs) > 0:
      lines.append(Line(_x,_y))
    for msg in self.msgs:
      line = lines[-1]
      while True:
        if line.total + len(msg) <= 50:
          # add the complete message
          line.addText(msg)
          break
        else:
          # split the message and start a new line
          capacity = 50 - line.total
          line.addText(msg[:capacity]) 
          # create the new line
          _y += 6
          line = Line(_x,_y)
          lines.append(line)
          msg = msg[capacity:]
          # the rest will be added in the new iteration
    # now build and return the SVG representing these lines
    s = """<g transform="translate({0},{1})" id="">
  <text xml:space="preserve" style="font-size:20px;font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;text-align:center;line-height:86.00000143%;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;font-family:Square;-inkscape-font-specification:Square">""".format(x(column),y(row))
    for line in lines:
      s += line.toFinalSVG()
    s += """  </text>
</g>"""
    return s






