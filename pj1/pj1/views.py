import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis.p108 import P108
from myanalysis.part4 import P109
from myanalysis.ws import WS01


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
def maps(request):
	P109().mat07()
	return render(request, 'gyonggi.html')
def chart1(request):

	return render(request, 'home.html')
def chart1(request):

	return render(request, 'chart1.html')
def chart2(request):

	return render(request, 'chart2.html')
def chart3(request):

	return render(request, 'chart3.html')
def chart4(request):

	return render(request, 'chart4.html')
# def chart5(request):
#
# 	return render(request, 'chart5.html')
# def chart5s(request):
# 	year = request.GET['year'];
# 	WS01().chart04(year)
# 	return render(request, 'gyonggi.html')
def tran(request):
	tran_place = request.GET['tran_place'];
	data = WS01().chart01(tran_place);
	return HttpResponse(json.dumps(data),content_type='application/json');
def genarating(request):
	first = request.GET['first'];
	end = request.GET['end'];
	data = WS01().chart02(first,end)
	return HttpResponse(json.dumps(data),content_type='application/json');
def pop(request):
	year = request.GET['year'];
	data = WS01().chart04(year)
	return HttpResponse(json.dumps(data),content_type='application/json');
