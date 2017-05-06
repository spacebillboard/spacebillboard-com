from data import data_manager, personal_message_squares, brands, personal_messages
from billboard import Billboard, Img, PreferredSquaresBillboard
import pprint
import os
import subprocess
import shutil

my = {
  'single': {
    'en': 'My',
    'nl': 'Mijn'
  },
  'plural': {
    'en': 'Our',
    'nl': 'Onze'
  } 
}
you = {
  'single': {
    'en': 'you',
    'nl': 'jou'
  },
  'plural': {
    'en': 'you',
    'nl': 'jullie'
  } 
}
your = {
  'single': {
    'en': 'your',
    'nl': 'jouw'
  },
  'plural': {
    'en': 'your',
    'nl': 'jullie'
  } 
}


class ValentineCardGenerator:
  """ Class used for generating the files for the Christmas cards. """
  def __init__(self):
    self.card_folder = "../../../../../static/valentine"

  def generateAll(self, id, message, to, from_, source, design):
    self.generateValentineCard(id, message, to, from_, source, design)
    # no valentine e-cards
    #self.generateValentineECard(id, message, to, from_, source, design)

  def generateValentineCard(self, id, message, to, from_, source, design):

    language = "nl"
    if source == "com":
      language = "en"

    folder = self.card_folder
#    qr = "{0}-qr.png".format(id)
    svg = "valentine-{0}-2.svg".format(id)
    pdf = "valentine-{0}-2.pdf".format(id)
    page1 = "valentine-card-{0}-1-{1}.pdf".format(design, language)
    total = "valentine-{0}.pdf".format(id)
    if source == "com":
      msgurl = "http://writeitinthestars.com/wish/{}".format(id)
    elif source == "be":
      msgurl = "http://schrijfhetindesterren.be/wens/{}".format(id)
    elif source == "nl":
      msgurl = "http://schrijfhetindesterren.nl/wens/{}".format(id)
    else:
      raise Exception("Unknown source given: {}".format(source))

    #################################
    # START BY TESTING WHETHER THE CARD DOES NOT EXIST ALREADY
    if os.path.isfile("{}/{}".format(folder, total)):
      raise Exception("The Valentine card for id #{} already exists".format(id))

    #################################
    # Generate the QR code
#    import qrcode
#    from qrcode.image.pure import PymagingImage
#    img = qrcode.make(msgurl, image_factory=PymagingImage)
#    with open(qr, "w+") as out:
#      img.save(out)

    #################################
    # Generate the PDF
    def process_template(path):
      with open(path, 'r') as template_source:
        template = template_source.read()

      template = template.replace("%id%", id)

      import textwrap
      wrapped_message = textwrap.wrap(message, 40)
      # HTML encode here (e.g., again errors with &)
      import cgi
      for i in range(len(wrapped_message)):
        wrapped_message[i] = cgi.escape(wrapped_message[i])
      # now put the message in the svg
      # Note: this is too much, but just leave it this way for now (it should not harm)
      if len(wrapped_message) == 1:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", "")
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 2:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", wrapped_message[1])
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 3:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 4:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", wrapped_message[3])

      template = template.replace("%to%", cgi.escape(to))
      template = template.replace("%from%", cgi.escape(from_))
      template = template.replace("%url%", cgi.escape(msgurl))
      return template

    with open(svg, "w+") as sink:
      template = process_template("templates/valentine-card-2-{}.svg".format(source))
      sink.write(template)

    subprocess.call("inkscape -f {} --export-pdf {} --export-area-page --export-dpi 600".format(svg, pdf), shell=True)
    join_command = "pdfunite {} {} {}".format("templates/valentine-card-1-{}-{}.pdf".format(design, source), pdf, total)
    subprocess.call(join_command, shell=True)

    #################################
    # Move the pdf and pngs
    def move_to_def(f):
      shutil.move(f, "{}/{}".format(folder, f))
#    move_to_def(qr) # do not move the qr code because the Ecard still needs it (not the best solution, but hey...)
    move_to_def(svg) 
    move_to_def(pdf)
    move_to_def(total)

    #################################
    # Move the other temp files to trash
    # nothing to do

  def generateValentineECard(self, id, message, to, from_, source, design):

    language = "nl"
    if source == "com":
      language = "en"

    folder = self.card_folder
#    qr = "{0}-qr.png".format(id)
    svg = "valentine-{0}-ecard.svg".format(id)
    pdf = "valentine-{0}-ecard.pdf".format(id)
    png = "valentine-{0}-ecard.png".format(id)
    jpg = "valentine-{0}-ecard.jpg".format(id)
    if source == "com":
      msgurl = "http://writeitinthestars.com/wish/{}".format(id)
    elif source == "be":
      msgurl = "http://schrijfhetindesterren.be/wens/{}".format(id)
    elif source == "be":
      msgurl = "http://schrijfhetindesterren.nl/wens/{}".format(id)
    else:
      raise Exception("Unknown source given: {}".format(source))

    #################################
    # START BY TESTING WHETHER THE CERTIFICATE DOES NOT EXIST ALREADY
    if os.path.isfile("{}/{}".format(folder, pdf)):
      raise Exception("The Valentine e-card for id #{} already exists".format(id))

    #################################
    # Generate the QR code

    # the normal card has already done this

    #################################
    # Generate the PDF
    def process_template(path):
      with open(path, 'r') as template_source:
        template = template_source.read()

      template = template.replace("%id%", id)

      import textwrap
      wrapped_message = textwrap.wrap(message, 40)
      # HTML encode here (e.g., again errors with &)
      import cgi
      for i in range(len(wrapped_message)):
        wrapped_message[i] = cgi.escape(wrapped_message[i])
      # now put the message in the svg
      # Note: this is too much, but just leave it this way for now (it should not harm)
      if len(wrapped_message) == 1:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", "")
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 2:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", wrapped_message[1])
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 3:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", "")
      elif len(wrapped_message) == 4:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", wrapped_message[3])

      template = template.replace("%to%", cgi.escape(to))
      template = template.replace("%from%", cgi.escape(from_))
      template = template.replace("%url%", cgi.escape(msgurl))
        
      return template

    with open(svg, "w+") as sink:
      template = process_template("templates/valentine-ecard-{}-{}.svg".format(design, language))
      sink.write(template)

    subprocess.call("inkscape -f {} --export-pdf {} --export-area-page --export-dpi 600".format(svg, pdf), shell=True)
    subprocess.call("inkscape -f {} --export-png {} --export-area-page --export-dpi 150".format(svg, png), shell=True)
    subprocess.call("mogrify -format jpg -quality 95 {}".format(png), shell=True)

    #################################
    # Move the pdf and pngs
    def move_to_def(f):
      shutil.move(f, "{}/{}".format(folder, f))
#    move_to_def(qr) 
    move_to_def(svg)
    move_to_def(pdf)
    move_to_def(jpg)

    #################################
    # Move the other temp files to trash
    from send2trash import send2trash
    send2trash(png)
   
valentine_card_generator = ValentineCardGenerator()
