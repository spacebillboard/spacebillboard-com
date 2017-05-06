from data import data_manager, personal_message_squares, brands, personal_messages
from billboard import Billboard, Img, PreferredSquaresBillboard
import pprint
import os
import subprocess

class ArtifactGenerator:
  """ Class used for generating the different artifacts of SpaceBillboard from data.yaml:
      - the-billboard.inc.php
      - preferred-squares-billboard.inc.php
      - percentage-sold.in.php
      - ... """
  def __init__(self):
    pass

  def generateAll(self):
    """ Generates all the artifacts. """
    data = data_manager.load()
    self.generateBillboard(data)
    self.generatePreferredSquaresBillboard(data)
    self.generateCustomersJS(data)
    self.generateCustomersAndMessagesPHP(data)

  def _populateBillboard(self, billboard, data):
    """ Helper method against copy-pasting """    
    for square in data[personal_message_squares]:
      billboard.definePersonalMessageSquare(square['row'], square['column'])
    for label, brand in data[brands].iteritems():
      billboard.add(Img(brand['billboard_size']['width'], brand['billboard_size']['height'], label, brand['url']),brand['billboard_position']['row'],brand['billboard_position']['column'])
    for msg in data[personal_messages]:
      billboard.addPersonalMessage(msg['id'], msg['message'])

  def buildBillboard(self, data):
    billboard = Billboard()
    self._populateBillboard(billboard, data)   
    return billboard

  def generateBillboard(self, data):
    """ Geneate the billboard. """
    billboard = self.buildBillboard(data)
    # generate the personal message images
    billboard.generate_personal_message_squares() 
    # generate the billboard itself
    billboard.generate_html_to("generated/the-billboard.inc.php")
    # generate the percentage sold
    with open("generated/percentage-sold.inc.php", "w") as sink:
      sink.write("<?php $percentageSold = {};".format(int(billboard.percentage_cells_filled())))
    # generate msg2square.inc.php
    with open("generated/msg2square.inc.php", "w") as sink:
      sink.write(billboard.generate_personal_messages_list())
    with open("generated/pmsgs_js.inc.php", "w") as sink:
      sink.write(billboard.generate_personal_messages_squares_list_js())

  def generateFinal(self):
    data = data_manager.load()
    billboard = self.buildBillboard(data)
    with open("generated/final.svg", "w+") as sink:
      billboard.generate_final(sink)
    # we are not empty => generate SVG and PNG
    cwd = os.getcwd()
    os.chdir("generated/")
    # convert SVG to other formats
    subprocess.call("inkscape -f final.svg --export-png final.png --export-width 6760 --export-height 6760", shell=True)
    subprocess.call("inkscape -f final.svg --export-pdf final.pdf --export-area-page --export-dpi 600", shell=True)
    # revert cwd
    os.chdir(cwd)

  def generatePreferredSquaresBillboard(self, data):
    """ Geneate the billboard to show on Buy Squares to select preferres squares. """
    billboard = PreferredSquaresBillboard()
    self._populateBillboard(billboard, data)
    billboard.generate_html_to("generated/preferred-squares-billboard.inc.php")

  def generateCustomersAndMessagesPHP(self, data):
    first = True
    s = "<?php\n$sbb_customers = array(\n"
    for label, brand in data['brands'].iteritems():
      if not first:
        s += ",\n"
      else:
        first = False
      s += self._brand_to_php(label, brand)
    s += "\n);\n"
    s += "$sbb_personal_messages = array(\n"
    first = True
    for msg in data['personal-messages']:
      if not first:
        s += ",\n"
      else:
        first = False
      s += self._message_to_php(msg)
    s += "\n);"
    with open("generated/customers_and_personal_messages.inc.php", "w") as sink:
      sink.write(s)

  def _brand_to_php(self, label, brand):
    """ Helper function to convert a brand to a PHP array. """
    return """  "{0}" => array(
    "name" => "{1}",
    "url" => "{2}",
    "nbSquares" => {3},
    "added" => '{4}'
  )""".format(label, brand['name'], brand['url'], brand['billboard_size']['height'] * brand['billboard_size']['width'], brand['added'])
    return s

  def _message_to_php(self, msg):
    """ Helper function to convert a message to a PHP array. """
    to = ''
    if 'to' in msg and msg['to'] is not None:
      to = msg['to']
    type_ = ''
    if 'type' in msg and msg['type'] is not None:
      type_ = msg['type']
    to_is_plural = False
    if 'to_is_plural' in msg and msg['to_is_plural'] is not None:
      to_is_plural = msg['to_is_plural']
    from_is_plural = False
    if 'from_is_plural' in msg and msg['from_is_plural'] is not None:
      from_is_plural = msg['from_is_plural']
    source = 'null'
    if 'source' in msg and msg['source'] is not None:
      source = '"{}"'.format(msg['source'])
    design = 'null'
    if 'design' in msg and msg['design'] is not None:
      design = '"{}"'.format(msg['design'])
    return """  array(
    "added" => "{0}",
    "id" => "{1}",
    "message" => "{2}",
    "name" => "{3}",
    "show_name_on_thankyou" => {4},
    "show_twitter_on_thankyou" => {5},
    "twitter_username" => "{6}",
    "url" => "{7}",
    "show_url_on_thankyou" => {8},
    "to" => '{9}',
    "to_is_plural" => {10},
    "type" => '{11}',
    "from_is_plural" => {12},
    "source" => {13},
    "design" => {14}
  )""".format(msg['added'], msg['id'],msg['message'],msg['name'],msg['show_name_on_thankyou'],msg['show_twitter_on_thankyou'],msg['twitter_username'] if msg['twitter_username'] else '',msg['url'] if msg['url'] else '',msg['show_url_on_thankyou'],to,to_is_plural,type_,from_is_plural,source,design)
    return s

  def generateCustomersJS(self, data):
    """ Generate customers_js.inc.php. """
    first = True
    s = "var customers = {\n"
    for label, brand in data['brands'].iteritems():
      if not first:
        s += ",\n"
      else:
        first = False
      s += self._brand_to_json(label, brand)
    s += "\n"
    s += "};"
    with open("generated/customers_js.inc.php", "w") as sink:
      sink.write(s)

  def _brand_to_json(self, label, brand):
    json = """  "{0}": {{
    "name": "{1}",
    "url": "{2}",
    "nbSquares": {3}""".format(label, brand['name'], brand['url'], brand['billboard_size']['height'] * brand['billboard_size']['width'])
    if "featured_sponsors" in brand:
      json = json + ',\n    "featuredSponsors": ['
      first = True
      for featured_sponsor in brand['featured_sponsors']:
        if not first:
          json = json + ", "
        json = json + """
      {{
       "name": "{}",
       "url": "{}",
       "image": "{}"
      }}""".format(featured_sponsor['name'],featured_sponsor['url'],featured_sponsor['image'])
        first = False
      json = json + '\n    ]'
    json += "\n  }"
    return json    

artifact_generator = ArtifactGenerator()
