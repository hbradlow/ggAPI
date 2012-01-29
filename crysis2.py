from scraper import *
import re
import mechanize
import BeautifulSoup

BASE_URL = "http://www.mycrysis.com"
class Crysis2Scraper(Scraper):
	def __init__(self,name):
		br = mechanize.Browser()
		url = BASE_URL + "/" + name
		br.open(url)
		br.select_form(nr=0)
		br['age'] = "22"
		response = br.submit()
		soup = BeautifulSoup.BeautifulSoup(response.read())

		##overall
		#rank
		self.rank =  {}
		try:
			rank =  soup.findAll("div",{"class":re.compile("overall")})[0].find("div",{"class":"rank"})
			self.rank['icon'] = rank.find("img")['src']
			self.rank['text'] = rank.find("div",{"class":"text"}).contents[0]
		except:
			pass
		#basic_info
		self.basic_info = None
		try:
			list =  soup.findAll("div",{"class":re.compile("overall")})[0].find("dl")
			dts = [c.string for c in list.findAll("dt")]
			dds = [c.string for c in list.findAll("dd")]
			self.basic_info = zip(dts,dds)
		except:
			pass

		##stat
		self.stats = []
		try:
			stats =  soup.findAll("div",{"class":"module profile-stat"})[0].findAll("div",{"class":"content"})[0].findAll("dl")
			for item in stats:
				dts = [c.string.replace(',','') for c in item.findAll("dt")]
				dds = [c.string.replace(',','') for c in item.findAll("dd")]
				self.stats.append(zip(dts,dds))
		except:
			pass

		##awards
		self.awards = []
		try:
			awards = soup.findAll("div",{"class":"module profile-award"})[0].findAll("div",{"class":"content"})[0].find("ul").findAll("li")
			for a in awards:
				award = {}
				style_list = a.find("div")['style'].split('(')
				award['style'] = style_list[0] + "(" + BASE_URL + style_list[1] + ")".join(style_list[2:])
				award['name'] = a.find("div")['title']
				self.awards.append(award)
		except:
			pass

		##nanosuit
		self.nanosuit = None
		try:
			self.nanosuit = soup.findAll("div",{"class":re.compile("module profile-nanousage?")})[0].findAll("div",{"class":"content"})[0]
			titles = [c.find("h2",{"class":"custom-font"}).contents[0] for c in self.nanosuit.findAll("div",{"class":"title"})]
			percents = [c.contents[0] for c in self.nanosuit.findAll("div",{"class":"percent"})]
			self.nanosuit = zip(titles,percents)
		except:
			pass

		##matches
		self.matches = []
		try:
			list = soup.findAll("div",{"class":re.compile("module profile-matches")})[0].find("div",{"class":"content"}).find("ul").findAll("li")
			for item in list:
				match = {}
				match['icon'] = "http://www.mycrysis.com" + item.find("img")['src']
				match['location'] = item.find("h2").string
				match['duration'] = item.findAll("dl")[0].find("dd").string
				match['date'] = item.findAll("dl")[1].find("dd").string
				self.matches.append(match)
		except:
			pass

		##weapons
		self.weapons = []
		try:
			list = soup.findAll("div",{"class":re.compile("module profile-weaponusage")})[0].find("div",{"class":"content"}).find("ul").findAll("li")
			for item in list:
				weapon = {}
				weapon['icon'] = "http://www.mycrysis.com" + item.find("img")['src']
				weapon['name'] = item.find("h2").string
				weapon['shots'] = item.findAll("dl")[0].findAll("dd")[0].string
				weapon['hits'] = item.findAll("dl")[0].findAll("dd")[1].string
				weapon['accuracy'] = item.findAll("dl")[1].findAll("dd")[0].string
				weapon['kills'] = item.findAll("dl")[1].findAll("dd")[1].string
				self.weapons.append(weapon)
		except:
			pass
	def getData(self): 
		return {"Crysis": {"Rank" : self.rank, "Basic Info" : self.basic_info, "Stats" : self.stats, "Awards" : self.awards, "Nanosuit" : self.nanosuit, "Matches" : self.matches, "Weapons" : self.weapons}}

if __name__ == "__main__":
	c = Crysis2Scraper("http://www.mycrysis.com/emre8888")
	print "Rank: ", c.rank
	print "Basic Info: ", c.basic_info
	print "Stats: ", c.stats
	print "Awards: ", c.awards
	print "Nanosuit: ", c.nanosuit
	print "Matches: ", c.matches
	print "Weapons: ", c.weapons
