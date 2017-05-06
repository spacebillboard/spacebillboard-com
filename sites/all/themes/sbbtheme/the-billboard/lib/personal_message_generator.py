from data import data_manager, personal_message_squares, brands, personal_messages
from billboard import Billboard, Img, PreferredSquaresBillboard
import pprint
import os
import subprocess
import shutil

class PersonalMessageGenerator:
  """ Class used for generating the files for the personal messages. """
  def __init__(self):
    self.certificates_folder = "../../../../../static/certificates"
    self.folding_folder = "../../../../../static/folding"

  def generateAll(self, id, message, name, url, twitter, show_name, show_url, show_twitter):
    self.generateCertificate(id, message, name, url, twitter, show_name, show_url, show_twitter)
#    self.generateFoldingModel(id, message, name, url, twitter, show_name, show_url, show_twitter)

  def generateCertificate(self, id, message, name, url, twitter, show_name, show_url, show_twitter):
    folder = self.certificates_folder
    qr = "{0}-qr.png".format(id)
    svg = "{0}.svg".format(id)
    svg_for_sharing = "{0}-for-sharing.svg".format(id)
    pdf = "{0}.pdf".format(id)
    png = "{0}.png".format(id)
    png_for_sharing = "{0}-for-sharing.png".format(id)
    jpg = "{0}.jpg".format(id)
    jpg_for_sharing = "{0}-for-sharing.jpg".format(id)
    msgurl = "http://spacebillboard.com/messages/{}".format(id)

    #################################
    # START BY TESTING WHETHER THE CERTIFICATE DOES NOT EXIST ALREADY
    if os.path.isfile("{}/{}.pdf".format(folder, id)):
      raise Exception("The certificate for id #{} already exists".format(id))

    #################################
    # Generate the QR code
    import qrcode
    from qrcode.image.pure import PymagingImage
    img = qrcode.make(msgurl, image_factory=PymagingImage)
    with open(qr, "w+") as out:
      img.save(out)

    #################################
    # Generate the PDF and PNG
    def process_template(path):
      with open(path, 'r') as template_source:
        template = template_source.read()

      template = template.replace("%id%", id)

      import textwrap
      wrapped_message = textwrap.wrap(message, 50)
      # HTML encode here (e.g., again errors with &)
      import cgi
      for i in range(len(wrapped_message)):
        wrapped_message[i] = cgi.escape(wrapped_message[i])
      # now put the message in the svg
      if len(wrapped_message) == 1:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", "")
      elif len(wrapped_message) == 2:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", "")
      elif len(wrapped_message) == 3:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])

      template = template.replace("%name%", cgi.escape(name))
      template = template.replace("%url%", cgi.escape(msgurl))
      return template

    with open(svg, "w+") as sink:
      template = process_template("templates/certificate.svg")
      sink.write(template)

    with open(svg_for_sharing, "w+") as sink:
      template = process_template("templates/certificate-for-sharing.svg")
      sink.write(template)

    subprocess.call("inkscape -f {} --export-pdf {} --export-area-page --export-dpi 600".format(svg, pdf), shell=True)
    subprocess.call("inkscape -f {} --export-png {} --export-area-page --export-dpi 150".format(svg, png), shell=True)
    subprocess.call("inkscape -f {} --export-png {} --export-area-page --export-width 500".format(svg_for_sharing, png_for_sharing), shell=True)
    subprocess.call("mogrify -format jpg -quality 95 {}".format(png), shell=True)
    subprocess.call("mogrify -format jpg -quality 95 {}".format(png_for_sharing), shell=True)

    #################################
    # Move the pdf and pngs
    def move_to_def(f):
      shutil.move(f, "{}/{}".format(folder, f))
    move_to_def(qr)
    move_to_def(svg)
    move_to_def(svg_for_sharing)
    move_to_def(pdf)
    move_to_def(jpg)
    move_to_def(jpg_for_sharing)

    #################################
    # Move the other temp files to trash
    from send2trash import send2trash
    send2trash(png)
    send2trash(png_for_sharing)

  def generateFoldingModel(self, id, message, name, url, twitter, show_name, show_url, show_twitter):
    folder = self.folding_folder
    svg = "{0}.svg".format(id)
    pdf = "{0}.pdf".format(id)

    #################################
    # START BY TESTING WHETHER THE CERTIFICATE DOES NOT EXIST ALREADY
    if os.path.isfile("{}/{}.pdf".format(folder, id)):
      raise Exception("The folding model for id #{} already exists".format(id))

    #################################
    # Generate the PDF and PNG
    def process_template(path):
      with open(path, 'r') as template_source:
        template = template_source.read()

      template = template.replace("%id%", id)

      import textwrap
      wrapped_message = textwrap.wrap(message, 25)
      # HTML encode here (e.g., again errors with &)
      import cgi
      for i in range(len(wrapped_message)):
        wrapped_message[i] = cgi.escape(wrapped_message[i])
      # now put the message in the svg
      if len(wrapped_message) == 1:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", "")
        template = template.replace("%message3%", wrapped_message[0])
        template = template.replace("%message4%", "")
        template = template.replace("%message5%", "")
        template = template.replace("%message6%", "")
      elif len(wrapped_message) == 2:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", "")
        template = template.replace("%message3%", wrapped_message[0])
        template = template.replace("%message4%", wrapped_message[1])
        template = template.replace("%message5%", "")
        template = template.replace("%message6%", "")
      elif len(wrapped_message) == 3:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", wrapped_message[1])
        template = template.replace("%message4%", wrapped_message[2])
        template = template.replace("%message5%", "")
        template = template.replace("%message6%", "")
      elif len(wrapped_message) == 4:
        template = template.replace("%message1%", "")
        template = template.replace("%message2%", wrapped_message[0])
        template = template.replace("%message3%", wrapped_message[1])
        template = template.replace("%message4%", wrapped_message[2])
        template = template.replace("%message5%", wrapped_message[3])
        template = template.replace("%message6%", "")
      elif len(wrapped_message) == 5:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", wrapped_message[3])
        template = template.replace("%message5%", wrapped_message[4])
        template = template.replace("%message6%", "")
      elif len(wrapped_message) == 6:
        template = template.replace("%message1%", wrapped_message[0])
        template = template.replace("%message2%", wrapped_message[1])
        template = template.replace("%message3%", wrapped_message[2])
        template = template.replace("%message4%", wrapped_message[3])
        template = template.replace("%message5%", wrapped_message[4])
        template = template.replace("%message6%", wrapped_message[5])

      wrapped_name = textwrap.wrap(name, 20)
      # HTML encode here
      for i in range(len(wrapped_name)):
        wrapped_name[i] = cgi.escape(wrapped_name[i])
      # now put the message in the svg
      if len(wrapped_name) == 1:
        template = template.replace("%name-short%", wrapped_name[0])
        template = template.replace("%name-long1%", "")
        template = template.replace("%name-long2%", "")
      elif len(wrapped_name) == 2:
        template = template.replace("%name-short%", "")
        template = template.replace("%name-long1%", wrapped_name[0])
        template = template.replace("%name-long2%", wrapped_name[1])    
      template = template.replace("%name%", cgi.escape(name))
      template = template.replace("%url%", cgi.escape(url))
      return template

    with open(svg, "w+") as sink:
      template = process_template("templates/folding-model.svg")
      sink.write(template)

    subprocess.call("inkscape -f {} --export-pdf {} --export-area-page --export-dpi 300".format(svg, pdf), shell=True)

    #################################
    # Move the pdf and pngs
    def move_to_def(f):
      shutil.move(f, "{}/{}".format(folder, f))
    move_to_def(svg)
    move_to_def(pdf)
    
personal_message_generator = PersonalMessageGenerator()
