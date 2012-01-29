# Create your views here.
from django.http import HttpResponse
from django.shortcuts import *
from django.http import HttpResponse
from django.shortcuts import *
from django.template import *
from django.db.models import Q
from django.core.files import File
from decimal import * 
import cStringIO
from django.core.files.temp import NamedTemporaryFile
import urllib2
        
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from django.contrib.auth import *

import sys
import os
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(SITE_ROOT, '../../../'))
import main

def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		select = request.POST['select']
		if select=='starcraft':
			id = request.POST['id']
			data = main.getData(username,[select],id=id)
			return profile_view(request,data,select)
		if select=='wow':
			realm = request.POST['realm']
			data = main.getData(username,[select],realm=realm)
			return profile_view(request,data,select)
		if select=='steam':
			data = main.getData(username,[select])
			return profile_view(request,data,select)
		if select=='crysis':
			data = main.getData(username,[select])
			return profile_view(request,data,select)
	return render_to_response("ggapi/index.html",context_instance=RequestContext(request))

def profile_view(request,data,game):
	if game=="starcraft":
		return render_to_response("ggapi/starcraft_profile_view.html",{"data":data},context_instance=RequestContext(request))
	if game=="wow":
		return render_to_response("ggapi/warcraft_profile_view.html",{"data":data},context_instance=RequestContext(request))
	if game=="crysis":
		return render_to_response("ggapi/crysis_profile_view.html",{"data":data},context_instance=RequestContext(request))
	return render_to_response("ggapi/profile_view.html",{"data":data},context_instance=RequestContext(request))

