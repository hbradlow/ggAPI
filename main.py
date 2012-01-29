from wowscraper import *
from crysis2 import * 
from starcraft import * 
from steamscraper import * 

def getData(name, games="", id=0, realm=""):
    data = {} 
    game = games.lower() 
    if games == "wow":
        scraper = WoWScraper(name=name,realm=realm)
        print scraper.getData()
        return scraper.getData() 
    elif games == "crysis": 
        scraper = Crysis2Scraper(name) 
        print scraper.getData()
        return scraper.getData() 
    elif games == "starcraft": 
        scraper = Starcraft2Scraper(name=name, id=id) 
        print scraper.getData() 
        return scraper.getData()
    elif game == "steam": 
        scraper = SteamScraper(name)
        print scraper.getData() 
        return scraper.getData() 
    elif game == "xbox": 
        return data
