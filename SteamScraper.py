import mechanize
import BeautifulSoup
import urllib
import re
from scraper import Scraper


class SteamScraper(Scraper):
    
    def __init__(self, url):
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

    
        



if __name__ == "__main__":
    s = SteamScraper("http://steamcommunity.com/id/deiterbomber/stats/TF2/?tab=stats")
    for tup in s.classAchievements:
        print tup[0] + ' ' + tup[1]

    for a in s.achievements:
        print a

    print "Printing Records: "

    for pr in s.personalRecords:
        print pr[0] + ' ' + pr[1]
