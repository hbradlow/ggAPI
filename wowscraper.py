from scraper import * 
import re 
import mechanize 
import BeautifulSoup
import urllib
class WoWScraper(Scraper): 
    def __init__(self,name,realm):
        url = "http://us.battle.net/wow/en/character/" + realm + "/" + name + "/advanced"
        response = urllib.urlopen(url) 
        soup = BeautifulSoup.BeautifulSoup(response.read()) 
        self.data = {}
        if soup.find("div", {"class" : "server-error"}) == None: 
            self.data['guild'] = soup.find("div", {"class" : "guild"}).find("a").string 
            self.data['title'] = soup.find("div", {"class" : "title"}).string
            self.data['race'] = soup.find("a", {"class" : "race"}).string
            self.data['class'] = soup.find("a", {"class" : "class"}).string
            self.data['spec'] = soup.find("a", {"class" : "spec tip"}).string
            self.data['averageItemLvl'] = soup.find("span", {"class" : "equipped"}).string         
    def getData(self):
        return {"World Of Warcraft" : self.data}
