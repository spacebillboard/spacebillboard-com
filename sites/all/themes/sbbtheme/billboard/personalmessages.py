from billboard import Img

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
    return sum(map(len, self.msgs))

  def capacityLeft(self):
    """ Returns the number of empty characters left in this PMI """
    return self.totalCapacity() - self.filled()

  def canTake(self, msg):
    """ Returns whether this PMI can take in the given message, i.e.,
        returns whether this PMI has enough capacity left to add the
        given message. """
    return self.capacityLeft() >= len(msg)

  def isEmpty(self):
    """ Returns whether this PMI is still empty """
    return self.filled() == 0

  def addMsg(self, msg):
    """ Adds a message to this PMI """
    if(not self.canTake(msg)):
      raise OutOfCapacityError(self, msg)
    self.msgs.append(msg)

  def html(self, column):
    # TODO output empty square if this PMI is empty
    return ('<!-- {0} --><td class="personal-msg {1}" data-msg-label="{2}" data-zoom-image="<?php print $theme_path; ?>/resources/img/personal-msgs/{2}.png">' +\
            '<a href="#"><img src="<?php print $theme_path; ?>/resources/img/personal-msgs/{2}-small.png"/>' +\
            '</a></td>').format(column, self.klass, self.label)

  def generateSVG(self):
    raise Exception()

class LineSegment:
  """ Class used for representing a text segment in a line in the SVG.
      This results in an unpositioned <tspan> of a certain color in the SVG. """
  
  def __init__(self, text, color):
    self.color = color
    self.text = text

  def toSVG(self):
    return '<tspan style="fill:{0};fill-opacity:1" id="tspan4499">{1}</tspan>'.format(self.color, self.text)

class Line:
  """ Class used for building a line in the SVG.
      This results in a positioned <tspan> without color in the SVG. """

  def __init__(self, x, y):
    self.segments = []
    self.x = x
    self.y = y
    self.total = 0

  def addText(self, text, color):
    """ Adds a segment with the containing text of the containing color to this line. """
    self.segments.append(LineSegment(text, color))
    self.total += len(text)

  def toSVG(self):
    svg = '<tspan sodipodi:role="line" x="{0}" y="{1}" style="text-align:start;line-height:100%;text-anchor:start">'.format(self.x, self.y)
    for segment in self.segments:
      svg += segment.toSVG()
    svg += '</tspan>'
    return svg

class PersonalMessageSVG:
  """ Class used for building the SVG showing multiple personal messages """

  def __init__(self):
    self.color1 = "#ff7f2a"
    self.color2 = "#0086d7"
    self.active_color = self.color1
    self.msgs = []

  def nbCharacters(self):
    return sum(map(len, self.msgs))

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
      if line.total + len(msg) <= 50:
        # add the complete message
        line.addText(msg, self.active_color)
      else:
        # split the message and start a new line
        capacity = 50 - line.total
        line.addText(msg[:capacity], self.active_color)
        # create the new line
        y += 20
        line = Line(x,y)
        lines.append(line)
        line.addText(msg[capacity:], self.active_color)
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



