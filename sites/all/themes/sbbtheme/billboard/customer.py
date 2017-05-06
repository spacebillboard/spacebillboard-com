from billboard import *
import sys

class CustomerCollection:
  """ Class used for representing a collection of Customer instances
      which can be generated into the appropriate sources."""
  
  def __init__(self):
    self.customers = []

  def add(self, customer):
    self.customers.append(customer)

  def generate_sources(self):
    """ Generates all the necessary sources based on the customers in this collection."""
    self.generate_billboard_to("billboards/billboard.inc.php") 
    self.generate_php_list_to("customers/customers.inc.php")
    self.generate_json_object_to("customers/customers_js.inc.php")
    self.generate_php_weighted_list_to("customers/customers_weighted.inc.php")

  def generate_billboard_to(self, file_name):    
    sink = open(file_name, "w")
    self.generate_billboard(sink)
    sink.close()

  def generate_billboard(self, sink = sys.stdout):
    billboard = Billboard()
    for customer in self.customers:
      img = Img(customer.billboard_img_width, 
                customer.billboard_img_height, 
                customer.billboard_img_filename, 
                customer.url, 
                customer.name)
      billboard.add(img, customer.billboard_img_x, customer.billboard_img_y)
    billboard.generate_html(sink)

  def generate_php_list_to(self, file_name):    
    sink = open(file_name, "w")
    self.generate_php_list(sink)
    sink.close()

  def generate_php_list(self, sink = sys.stdout):
    first = True
    s = "<?php $sbb_customers = array(\n"
    for c in self.customers:
      if not first:
        s += ",\n"
      else:
        s += "\n"
        first = False
      s += "\"{0}\" => ".format(c.name)
      s += c.toPHP()
    s += "\n"
    s += ");"
    print >> sink, s

  def generate_json_object_to(self, file_name):    
    sink = open(file_name, "w")
    self.generate_json_object(sink)
    sink.close()

  def generate_json_object(self, sink = sys.stdout):
    first = True
    s = "var customers = {\n"
    for c in self.customers:
      if not first:
        s += ",\n"
      else:
        s += "\n"
        first = False
      s += "\"{0}\": ".format(c.name)
      s += c.toJSON()
    s += "\n"
    s += "};"
    print >> sink, s

  def generate_php_weighted_list_to(self, file_name):    
    sink = open(file_name, "w")
    self.generate_php_weighted_list(sink)
    sink.close()

  def generate_php_weighted_list(self, sink = sys.stdout):
    first = True
    s = "<?php $sbb_weighted_customers = array(\n"
    for c in self.customers:
      for i in range(c.nb_squares):
        if not first:
          s += ",\n"
        else:
          s += "\n"
          first = False
        s += "\"{0}\"".format(c.name)
    s += "\n"
    s += ");"
    print >> sink, s

############
# The default customer collection in which each Customer instance registers
# itself.
customers = CustomerCollection()

class IncompleteCustomerError(Exception):
  """ Simple exception to throw in case of processing an incomplete 
      customer instance. """

  def __init__(self, customer_name):
    self.customer_name = customer_name

  def __str__(self):
    return "Incomplete customer with name: {0}".format(self.customer_name)

class Customer:
  """ Class used for representing a Customer of SpaceBillboard.com.
      Every Customer instance contains all the information to generate the
      other appropriate sources. 

      Every Customer adds himself to the customers collection upon creation.

      Example: Customer("Stella", 
        "http://www.stella-artois.be/", "Stella slogan", 
        (4, 5), (3, 4), "stella-artois-126x94.jpg",
        "stella-artois.jpg")"""

  def __init__(self, name, url, slogan):
    self.name = name
    self.url = url
    self.slogan = slogan
    self.billboard_img_x = None
    self.billboard_img_y = None
    self.billboard_img_width = None
    self.billboard_img_height = None
    self.billboard_img_filename = None
    self.featured_img_filename = None
    self.nb_squares = None
    customers.add(self)

  def billboard(self, width, height, filename):
    """ Set the data about the image in the billboard for this customer.
        Returns self to allow chaining. """
    self.billboard_img_width = width
    self.billboard_img_height = height
    self.billboard_img_filename = filename
    self.nb_squares = width * height
    return self

  def at(self, x, y):
    """ Set the position of the billboard image of this customer.
        Returns self to allow chaining. """
    self.billboard_img_x = x
    self.billboard_img_y = y
    return self

  def featured(self, filename):
    """ Set the filename of the featured image for this customer.
        Returns self to allow chaining. """
    self.featured_img_filename = filename
    return self

  def isComplete(self):
    """ Returns whether all the fields of this Customer are set or not. """
    return  self.name is not None and \
            self.url is not None and\
            self.slogan is not None and\
            self.billboard_img_x is not None and\
            self.billboard_img_y is not None and\
            self.billboard_img_width is not None and\
            self.billboard_img_height is not None and\
            self.billboard_img_filename is not None and\
            self.featured_img_filename is not None and\
            self.nb_squares is not None

  def toPHP(self):
    """ Returns this Customer as a PHP array. Throws an exception if
        the customer data is not complete."""
    if not self.isComplete():
      raise IncompleteCustomerException(self.name)
    s = "array(\n"
    s += '  "name" => "{0}",\n'.format(self.name)
    s += '  "url" => "{0}",\n'.format(self.url)
    s += '  "slogan" => "{0}",\n'.format(self.slogan)
    s += '  "nbSquares" => {0},\n'.format(self.nb_squares)
    s += '  "featuredImg" => "{0}"\n'.format(self.featured_img_filename)
    s += ")"
    return s

  def toJSON(self):
    """ Returns this Customer as a JSON object. Throws an exception if
        the customer data is not complete."""
    if not self.isComplete():
      raise IncompleteCustomerException(self.name)
    s = "{\n"
    s += '  "name": "{0}",\n'.format(self.name)
    s += '  "url": "{0}",\n'.format(self.url)
    s += '  "slogan": "{0}",\n'.format(self.slogan)
    s += '  "nbSquares": {0},\n'.format(self.nb_squares)
    s += '  "featuredImg": "{0}"\n'.format(self.featured_img_filename)
    s += "}"
    return s




