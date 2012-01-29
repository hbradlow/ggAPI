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
            s = soup.find('li', {"data-id":"stamina"})
            self.data['stamina'] = s.find("span", {"class":"value color-q2"}).string
            s = soup.find('li', {"data-id":"strength"})
            self.data['strength'] = s.find("span", {"class":"value color-q2"}).string
            s = soup.find('li', {"data-id":"mastery"})
            self.data['mastery'] = s.find("span", {"class":"value"}).string
            s = soup.find('li', {"data-id":"intellect"})
            self.data['intellect'] = s.find("span", {"class":"value"}).string
            s = soup.find('li', {"data-id":"spirit"})
            self.data['spirit'] = s.find("span", {"class":"value"}).string
            s = soup.find('li', {"data-id":"agility"})
            self.data['agility'] = s.find("span", {"class":"value"}).string




    def getData(self):
        return {"wow" : self.data}

if __name__ == "__main__":
    w = WoWScraper("Kungen", "aegwynn")
    print "Data: ", w.getData()

