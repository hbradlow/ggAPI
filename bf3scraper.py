import re
from BeautifulSoup import BeautifulSoup
import urllib
from scraper import Scraper

class bf3scraper(Scraper):

    def __init__(self, name):
        url = "http://battlelog.battlefield.com/bf3/soldier/" + name + "/stats" 
        page = BeautifulSoup(urllib.urlopen(url))

        #general stats
        a = page.find('div', {"class":"col_right c21_2_"})

if __name__ == "__main__":
    

