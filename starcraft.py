from scraper import *
import re
import mechanize
import BeautifulSoup

BASE_URL = "http://us.battle.net"
class Starcraft2Scraper(Scraper):
	def __init__(self,url):
		br = mechanize.Browser()
		response = br.open(url)
		soup = BeautifulSoup.BeautifulSoup(response.read())
	
		##basic info
		self.username = soup.find("div",{"id":"profile-header"}).find("h2").find("a").string
		self.score = soup.find("div",{"id":"profile-header"}).find("h3").string

		##decals
		decals = soup.find("div",{"id":"current-decals"}).findAll("div",{"class":"current-decal"})
		self.decals = []
		for d in decals:
			decal = {}
			decal['type'] = d['data-tooltip']
			decal['style'] = str(d.find("span")['style'].split('\'')[0]) + "'" + BASE_URL + str(d.find("span")['style'].split('\'')[1]) + "'".join(d.find("span")['style'].split('\'')[1:])
			self.decals.append(decal)
			

if __name__ == "__main__":
	s = Starcraft2Scraper("http://us.battle.net/sc2/en/profile/2302508/1/ttjf/")
	print "Username: ", s.username
	print "Score: ", s.score
	print "Decals: ",s.decals

