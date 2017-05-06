from customer import *

Customer("Stella", "http://www.stella-artois.be/", "Stella slogan")\
  .billboard(4, 3, "stella-artois-126x94.jpg").at(4, 5)\
  .featured("stella-artois.jpg")

Customer("Wired", "http://www.wired.com/", "Wired slogan")\
  .billboard(4, 1, "wired-132x30.jpg").at(7, 8)\
  .featured("wired.jpg") # FIXME correct file name?

Customer("Pizza Hut", "http://www.pizzahut.com/", "Pizza Hut slogan")\
  .billboard(3, 3, "pizzahut-98x98.png").at(4,14)\
  .featured("pizzahut.png")

Customer("Red Planet Hotels", "http://www.redplanethotels.com/", "Red Planet Hotels slogan")\
  .billboard(3, 3, "redplanethotels-98x98.png").at(15,15)\
  .featured("redplanethotels.png")

Customer("Renault", "http://www.renault.com/", "Renault slogan")\
  .billboard(3, 3, "renault-98x98.png").at(15,5)\
  .featured("renault.png")

Customer("Science News", "https://www.sciencenews.org/", "Science News slogan")\
  .billboard(6, 1, "sciencenews-200x30.png").at(4,18)\
  .featured("sciencenews.png")

customers.generate_sources()
