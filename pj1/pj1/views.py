import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis.p108 import P108


def home(request):

	return render(request, 'home.html')
def c1(request):
	# data = myanalysis.p108.P108.p108()
	return render(request, 'c1.html')
def c1data(request):
	data = P108().p108()
	print(data)
	return HttpResponse(json.dumps(data),content_type='application/json');

def iots(request):
	speed = request.GET['speed'];
	rpm = request.GET['rpm'];
	temp = request.GET['temp'];
	logger = logging.getLogger('users');
	logger.debug( speed +','+rpm+','+temp);
	return render(request, 'iotsresult.html')