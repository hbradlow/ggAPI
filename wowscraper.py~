from scraper import * 
import re 
import mechanize 
import BeautifulSoup
import urllib
class WoWScraper(Scraper): 
    def __init__(self,url):  
        response = urllib.urlopen(url) 
        soup = BeautifulSoup.BeautifulSoup(response.read()) 
        data = {}
        if soup.find("div", {"class" : "server-error"}) == None: 
            data['guild'] = soup.find("div", {"class" : "guild"}).find("a").string 
            data['title'] = soup.find("div", {"class" : "title"}).string
            data['race'] = soup.find("a", {"class" : "race"}).string
            data['class'] = soup.find("a", {"class" : "class"}).string
            data['spec'] = soup.find("a", {"class" : "spec tip"}).string
            data['averageItemLvl'] = soup.find("span", {"class" : "equipped"}).string         
