from scraper import *
import re
import mechanize
import BeautifulSoup
import time

from windmill.authoring import WindmillTestClient
from windmill.authoring import setup_module, WindmillTestClient 
from windmill.conf import global_settings 
import sys 
global_settings.START_CHROME = True 
setup_module(sys.modules[__name__])

class PlaystationScraper(Scraper):
	def __init__(self,url):
		client = WindmillTestClient(__name__)
		client.open(url=url)
		client.waits.sleep(milliseconds=u'5000')
		time.sleep(5)
		client.waits.forElement(id="id-handle",timeout="5000")
		self.soup = BeautifulSoup.BeautifulSoup(client.commands.getPageText()['result'])

		#username
		self.username = self.soup.find("id-handle").string
		print self.username

if __name__ == "__main__":
	p = PlaystationScraper("http://us.playstation.com/publictrophy/index.htm?onlinename=terminator")
	print "Soup: ", p.soup
	#print "Username: ", p.username


