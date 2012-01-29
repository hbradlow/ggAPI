import re
from BeautifulSoup import BeautifulSoup
import urllib
from scraper import Scraper

def bf3scraper(scraper):
    def __init__(self, url):
        page = BeautifulSoup(urllib.urlopen(url))

        #general stats
        rightSideStats = {}
        a = page.find('div', {"class":"col_right c21_2"})
        names = a.findAll('h1')
        tables = a.findAll('div', {"class":"cont text"})
        for name, table in zip(names, tables):
            print name
            print table
            tableKeys = table.findAll('dt', text=re.compile('.*'))
            tableVals = table.findAll('dd', text=re.compile('.*'))
            data = {}
            for k, v in zip(tableKeys, tableVals):
                data[k] = v
            rightSideStats[name] = data
        self.rStats = rightSideStats


if __name__ == "__main__":
    b = bf3scraper("http://bf3stats.com/stats_pc/JoeHemi")
    print b.rStats
