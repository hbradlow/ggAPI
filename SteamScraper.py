import mechanize
import BeautifulSoup
import urllib
import re
from scraper import Scraper


class SteamScraper(Scraper):
		"""
		fields: 
	gameAchievements: a dictionary mapping game names to a string "x of y Achievements Earned"
	gameHours: a dictionary mapping game names to a tuple (hours last 2 weeks, hours total)

		TF2 fields:
			achievements: a list of the special acheivements earned "achievement: value"
			class achievements: a list of (class achievements earned:, x of y (%)

		"""
	
	#url argument should be to the player's game list page
	def __init__(self, username):
		# Should take a username as argument and then gather data for all of the games that user has played
		url = "http://steamcommunity.com/id/"+username+"/games"
		page = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
		tf2 = False

		#total hours
		a = page.findAll('div', {"class":"gameListRowItem"})
		gameHours = {}
		gameAchievements = {}
		for block in a:
			gName = block.find('h4').find(text=re.compile('.*'))
			if gName == "Team Fortress 2":
	tf2 = True
			wHours = block.find('h5', text=re.compile('.* hrs last')).split()[0]
			t = block.find('h5', text=re.compile('.*hrs .*')).split()
			tHours = t[len(t)-4]
			gameHours[gName] = (wHours, tHours)
			achieved = block.find({"class":"recentAchievements"}, text=re.compile('.*Achievements Earned'))	 
			if achieved != None:
	achieved = ' '.join(achieved.split())
			gameAchievements[gName] = achieved
		self.gameAchievements = gameAchievements
		self.gameHours = gameHours

		if tf2:
			page = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
	  

		#achievements
		a = page.findAll('div', id=re.compile('achievementStats_.*'))
		achievementNames = []
		achievementScores = []
		for block in a:
			achievementNames.append(block.find('div', text=re.compile('.*Earned:'))) 
			achievementScores.append(' '.join(block.contents[1].contents[2].split()))
		self.classAchievements = zip(achievementNames, achievementScores)

		self.achievements = []
		a = page.findAll('div', {"class":"achieveTxt"})
		for block in a:
			self.achievements.append(block.find('h3').find(text=re.compile('.*')))

		#stats
		a = page.findAll('div', {"class":"personalRecordStat"})
		self.personalRecords = []
		recs = []
		scores = []
		for block in a:
			r = block.find({"class":"recordStatLabel"}, text=re.compile('.*:'))
			if r != None:
	recs.append(r)
			s = block.find('span')
			if s != None:
	print s
	s = s.find(text=re.compile('.*'))
	scores.append(s)
		self.personalRecords = zip(recs, scores)

		#class stats
		a = page.findAll


		def getData(self):
			data = {}
			keys = self.gameHours.keys() 
			for item in keys: 
	data = {}
	data[item]["Hours"] = self.gameHours[item]
	data[item]["Achievements"] = self.gameAchievements[item]
	if item == "Team Fortress 2": 
		data[item]["Class Achievements"] = self.classAchievements
		data[item]["TF2 Achievements"] = self.achievements
		data[item]["Personal Records"] = self.personalRecords
			return data


if __name__ == "__main__":
	
	s = SteamScraper("http://steamcommunity.com/id/deiterbomber/stats/TF2/?tab=stats")
	for tup in s.classAchievements:
		print tup[0] + ' ' + tup[1]

	for a in s.achievements:
		print a

	for pr in s.personalRecords:
		print pr[0] + ' ' + pr[1]

	print s.gameHours

	print s.gameAchievements
