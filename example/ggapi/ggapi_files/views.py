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

def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		return profile_view(request,username)
	return render_to_response("ggapi/index.html",context_instance=RequestContext(request))

def profile_view(request,username):
	return render_to_response("ggapi/profile_view.html",{"username":username},context_instance=RequestContext(request))

