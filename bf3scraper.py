import re
from BeautifulSoup import BeautifulSoup
import urllib
from scraper import Scraper

class bf3scraper(Scraper):

    def __init__(self, url):
        page = BeautifulSoup(urllib.urlopen(url))

        #general stats
        rightSideStats = []
        a = page.find('div', {"class":"col_right c21_2"})
        names = a.findAll('h1', text=re.compile('..*'))
        tables = a.findAll('div', {"class":"cont text"})
        for name, table in zip(names, tables):
            tableKeys = table.findAll('dt', text=re.compile('.*'))
            tableVals = table.findAll('dd', text=re.compile('.*'))
            data = {}
            i = 0
            while i<len(tableKeys)-1:
                data[tableKeys[i]] = tableKeys[i+1]
                i += 2
            rightSideStats.append(data)

            while i<len(tableVals)-1:
                data[tableVals[i]] = tableVals[i+1]
                i += 2
            rightSideStats.append(data)

            
        self.rStats = rightSideStats


if __name__ == "__main__":
    b = bf3scraper("http://bf3stats.com/stats_pc/JoeHemi")
    for item in b.rStats:
        print item
    

