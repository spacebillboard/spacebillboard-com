import urllib2
import json

base = 'http://beta.spacebillboard.com/'
anonymous_pages = [
  "<front>"
]
company_pages = [
  "<front>",
#  "mission",     seems that the regular expression is too big now...
#  "buy",
#  "for-advertisers",
#  "contest",
#  "follow"
]

response = urllib2.urlopen('http://beta.spacebillboard.com/company-list-json?company=example')
urls = json.load(response)
companies = [url[11:] for url in urls["urls"]]

for p in anonymous_pages:
  print p
for c in companies:
  for p in company_pages:
    print p + "?company=" + c
