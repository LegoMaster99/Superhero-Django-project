from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import comBatman, comSuperman, comWonderWoman
from .forms import Message, Author

# Create your views here.    
class homeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "./index.html", {})     
    
 #batman View       
class batmanView(View):
    def get(self, request, *args, **kwargs):
        obj = comBatman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,

            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,           
        }        
        return render(request, "./batman.html", context)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Message(request.POST)
            if form.is_valid():
                mess = form.cleaned_data["Mess"]
                
        if request.method == 'POST':
            form = Author(request.POST)
            if form.is_valid():
                auth = form.cleaned_data["Auth"]        
        comBatman.objects.create(comment=mess, author=auth) 
        obj = comBatman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,
            
            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,          
        }       
        return render(request, "./batman.html", context)
    
 #Superman View   
class supermanView(View):
    def get(self, request, *args, **kwargs):
        obj = comSuperman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,

            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,           
        } 
        return render(request, "./superman.html", context)  
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Message(request.POST)
            if form.is_valid():
                mess = form.cleaned_data["Mess"]
                
        if request.method == 'POST':
            form = Author(request.POST)
            if form.is_valid():
                auth = form.cleaned_data["Auth"]        
        comSuperman.objects.create(comment=mess, author=auth) 
        obj = comSuperman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,
            
            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,          
        }       
        return render(request, "./superman.html", context)  
    
 #wonder Woman View   
class wonderWomanView(View):
    def get(self, request, *args, **kwargs):
        obj = comWonderWoman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,

            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,           
        }        
        return render(request, "./wonderwoman.html", context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Message(request.POST)
            if form.is_valid():
                mess = form.cleaned_data["Mess"]
                
        if request.method == 'POST':
            form = Author(request.POST)
            if form.is_valid():
                auth = form.cleaned_data["Auth"]        
        comWonderWoman.objects.create(comment=mess, author=auth) 
        obj = comWonderWoman.objects.all().order_by('-id')[:10]
        context = {
            "auth": Author,
            "mess": Message,
            "obj1C": obj[0].comment,
            "obj2C": obj[1].comment,
            "obj3C": obj[2].comment,
            "obj4C": obj[3].comment,
            "obj5C": obj[4].comment,
            
            "obj1A": obj[0].author,
            "obj2A": obj[1].author,
            "obj3A": obj[2].author,
            "obj4A": obj[3].author,
            "obj5A": obj[4].author,          
        }              
        return render(request, "./wonderwoman.html", context)  