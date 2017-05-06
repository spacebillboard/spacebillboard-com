from billboard import *
from showroom import empty, green

billboard = Billboard()

########################
# DEFINE ALL PERSONAL MESSAGE SQUARES
#
# NEVER CHANGE A LINE HERE, ONLY APPEND NEW LINES or the message locations
# of a lot of messages will change
billboard.definePersonalMessageSquare(2,2)
billboard.definePersonalMessageSquare(3,3)
billboard.definePersonalMessageSquare(4,4)

########################
# ADD ALL IMAGES
billboard.add(PersonalMsgsImg("example"), 10, 10)
billboard.add(PersonalMsgsImg("example"), 5, 5)
billboard.add(empty(2,2,green), 13, 13)

########################
# ADD ALL PERSONAL MESSAGES
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")
billboard.addPersonalMessage("Kathleen is cool")

########################
# GENERATE THE BILLBOARD
billboard.generate_html_to("the-billboard.inc.php")
