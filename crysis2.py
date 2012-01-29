from scraper import *
import re
import mechanize
import BeautifulSoup

class Crysis2Scraper(Scraper):
	def __init__(self,url):
		br = mechanize.Browser()
		br.open(url)
		br.select_form(nr=0)
		br['age'] = "22"
		response = br.submit()
		soup = BeautifulSoup.BeautifulSoup(response.read())

		#overall
		rank =  soup.findAll("div",{"class":re.compile("?overall")})[0].find("div",{"class":"rank"})
		self.rank.icon = rank.find("img")['src']
		self.rank.text = rank.find("div",{"class":"text"}).contents[0]

		#stats
		stats =  soup.findAll("div",{"class":"module profile-stat"})[0].findAll("div",{"class":"content"})[0].findAll("dl")
		self.stats = []
		for item in stats:
			dts = [c.contents[0].replace(',','') for c in item.findAll("dt")]
			dds = [c.contents[0].replace(',','') for c in item.findAll("dd")]
			self.stats.append(zip(dts,dds))

		#awards
		self.awards = [c.find("div")['title'] for c in soup.findAll("div",{"class":"module profile-award"})[0].findAll("div",{"class":"content"})[0].find("ul").findAll("li")]

		#nanosuit
		self.nanosuit = soup.findAll("div",{"class":re.compile("module profile-nanousage?")})[0].findAll("div",{"class":"content"})[0]
		titles = [c.find("h2",{"class":"custom-font"}).contents[0] for c in self.nanosuit.findAll("div",{"class":"title"})]
		percents = [c.contents[0] for c in self.nanosuit.findAll("div",{"class":"percent"})]
		self.nanosuit = zip(titles,percents)

if __name__ == "__main__":
	c = Crysis2Scraper("http://www.mycrysis.com/emre8888")
	print "Rank: ", c.rank
	print "Stats: ", c.stats
	print "Awards: ", c.awards
	print "Nanosuit: ", c.nanosuit

