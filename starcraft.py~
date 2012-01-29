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
			
		##wins
		self.league_wins = soup.find("div",{"class":"module-body campaign-unearned"}).find("h2").string
		self.games = {}
		games = soup.find("div",{"class":"module-body campaign-unearned"}).find("ul").findAll("li")
		self.games['custom_games'] = int(games[0].find("span").string)
		self.games['ffa'] = int(games[1].find("span").string)
		self.games['coop_vs_ai'] = int(games[2].find("span").string)

		##acheivements
		response = br.open(url + "achievements/")
		soup = BeautifulSoup.BeautifulSoup(response.read())

		achievements = soup.find("div",{"id":"recent-achievements"}).findAll("a")
		self.recent_achievements = []
		for a in achievements:
			achievement = {}
			style_list = a.find("span")['style'].split('\'')
			achievement['style'] = style_list[0] + "'" + BASE_URL + style_list[1] + "'".join(style_list[1:])
			self.recent_achievements.append(achievement)


if __name__ == "__main__":
	s = Starcraft2Scraper("http://us.battle.net/sc2/en/profile/2302508/1/ttjf/")
	print "Username: ", s.username
	print "Score: ", s.score
	print "Decals: ",s.decals
	print "League Wins: ", s.league_wins
	print "Games Won: ", s.games
	print "Recent Achievements: ", s.recent_achievements

