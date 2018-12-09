# from django.http import HttpResponse
from django.shortcuts import render



def home(request):
	return render(request, 'home.html')

def count(request):
	text= request.GET['text']
	sort_text={}
	for word in text:
	    if word not in sort_text:
	        sort_text[word]= 1
	    else:
	        sort_text[word]+= 1 
	sort_dict=sorted(sort_text.items(),key=lambda w: w[1], reverse=True)
	return render(request, 'count.html',{'count': text,'sort': sort_dict})