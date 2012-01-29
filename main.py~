from wowscraper import *
from crysis2 import * 
from starcraft import * 
from SteamScraper import * 

def getData(name, games=[], id=0, realm="", service=""): 
    data = {} 
    games[0] = games[0].lower() 
    service = service.lower() 
    if games[0] == "wow":
        scraper = WoWScraper(name=name,realm=realm)
        print scraper.getData()
        return scraper.getData() 
    elif games[0] == "crysis": 
        scraper = Crysis2Scraper(name) 
        print scraper.getData()
        return scraper.getData() 
    elif games[0] == "starcraft": 
        scraper = Starcraft2Scraper(name=name, id=id) 
        print scraper.getData() 
        return scraper.getData()
    elif service == "steam": 
        scraper = SteamScraper(name)
        print scraper.getData() 
        return scraper.getData() 
    elif service == "xbox": 
        return data
