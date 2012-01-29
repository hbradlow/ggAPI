from windmill.authoring import WindmillTestClient
from windmill.authoring import setup_module, WindmillTestClient 
from windmill.conf import global_settings 
import sys 
global_settings.START_FIREFOX = True 
setup_module(sys.modules[__name__])

def test():
	client = WindmillTestClient(__name__)
	client.open(url="http://us.playstation.com/publictrophy/index.htm?onlinename=terminator")
	client.waits.forPageLoad(timeout=u'6000')
	print "Test"
	print client.commands.getPageText()

test()
	
