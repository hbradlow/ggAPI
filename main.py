import crysis2
import wowscraper

def getData(name, game, id=0, realm="", service=""): 
    if type(game) != "list": 
        return "Error: Must send a list of games, even for single game searces"
    data = {} 
    game = game.lower() 
    service = service.lower() 
    if game == "wow": 
        return data 
    elif game == "crysis": 
        return data 
    elif game == "starcraft": 
        return data
    elif service == "steam": 
        return data 
    elif service = "xbox": 
        return data
