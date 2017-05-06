import yaml
from datetime import datetime

# some labels
personal_message_squares = "personal-message-squares"
brands = "brands"
personal_messages = "personal-messages"
christmas_messages = "christmas-messages"

class DataManager:
  """ A class used for representing the manager of the SpaceBillboard data. 
      This actually is a singleton, the different instances
      behave exactly the same. """
  def __init__(self):
    pass

  def load(self):
    """ Loads and returns the SpaceBillboard data. """
    with open("data.yaml", "r") as source:
      return yaml.load(source)

  def _save(self, data):
    """ Saves the given data in data.yaml. THIS WILL OVERWRITE
        ALL DATA PRESENT IN DATA.YAML, so be careful with this. """
    with open("data.yaml", "w") as sink:
       yaml.dump(data, sink, default_flow_style=False)

  def getPersonalMessage(self, id):
    data = self.load()
    for msg in data['personal-messages']:
      if msg['id'] == id:
        return msg
    return None

  def addPersonalMessageSquare(self, row, column):
    data = self.load()
    data[personal_message_squares].append({'row': row, 'column': column, 'added': datetime.now()})
    self._save(data)

  def addBrand(self, label, name, url, billboard_size, billboard_position):
    """ Add a new brand to the SpaceBillboard data. 
        @param  label String  A label for this new brand. No spaces, only alphanumerical characters and _
        @param  name  String  The name of this new brand
        @param  url   String  The URL of the website of this new brand
        @param  billboard_size (width: int, height: int) The width and height of the billboard image of this new brand
        @param  billboard_position (row: int, column: int) The position of the billboard image of this new brand """
    data = self.load()
    data[brands][label] = {
      'name': name,
      'url': url,
      'billboard_size': {
        'width': billboard_size[0],
        'height': billboard_size[1]
      },
      'billboard_position': {
        'row': billboard_position[0],
        'column': billboard_position[1]
      },
      'added': datetime.now()
    }
    self._save(data)

  def addPersonalMessage(self, id_, name, message, url, twitter_username, show_name_on_thankyou, show_url_on_thankyou, show_twitter_on_thankyou):
    """ Add a new peronal message to the SpaceBillboard data. 
        @param  name  String  The name of the person that posted the personal message
        @param  message String  The message itself
        @param  url String  The URL of the homepage of the poster of the message
        @param  twitter_username  String  The twitter username of the person that posted the personal message
        @param  show_name_on_thankyou Boolean Whether or not to show the name of the person on the thank-you page
        @param  show_url_on_thankyou Boolean Whether or not to show the URL of the homepage of the person on the thank-you page
        @param  show_twitter_on_thankyou  Boolean Whetehr or not to show the Twitter ysername of the person on the thank-you page """
    data = self.load()
    data[personal_messages].append({
      'id': id_,
      'name': name,
      'message': message,
      'url': url,
      'twitter_username': twitter_username,
      'show_name_on_thankyou': show_name_on_thankyou,
      'show_url_on_thankyou': show_url_on_thankyou,
      'show_twitter_on_thankyou': show_twitter_on_thankyou,
      'added': datetime.now()
    })
    self._save(data)

  def addChristmasMessage(self, id_, message, to, to_is_plural, from_, from_is_plural, language, url, twitter_username, show_name_on_thankyou, show_url_on_thankyou, show_twitter_on_thankyou):
    """ Add a new peronal message to the SpaceBillboard data. """
    data = self.load()
    data[personal_messages].append({
      'id': id_,
      'message': message,
      'to': to,
      'to_is_plural': to_is_plural,
      'name': from_,
      'from_is_plural': from_is_plural,
      'language': language,
      'url': url,
      'twitter_username': twitter_username,
      'show_name_on_thankyou': show_name_on_thankyou,
      'show_url_on_thankyou': show_url_on_thankyou,
      'show_twitter_on_thankyou': show_twitter_on_thankyou,
      'added': datetime.now(),
      'type': 'christmas'
    })
    self._save(data)

  def addValentineMessage(self, id_, message, to, from_, source, design, show_name_on_thankyou):
    """ Add a new peronal message to the SpaceBillboard data. """
    language = "nl"
    if source == "com":
      language = "en"
    data = self.load()
    data[personal_messages].append({
      'id': id_,
      'message': message,
      'to': to,
      'to_is_plural': False,
      'name': from_,
      'from_is_plural': False,
      'language': language,
      'url': None,
      'twitter_username': None,
      'show_name_on_thankyou': show_name_on_thankyou,
      'show_url_on_thankyou': False,
      'show_twitter_on_thankyou': False,
      'added': datetime.now(),
      'type': 'valentine',
      'design': design
    })
    self._save(data)
    
data_manager = DataManager()
