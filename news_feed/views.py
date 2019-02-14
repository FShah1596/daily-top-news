from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from news_feed.models import Everything, Sources
from news_feed.serializers import NewsFeedSerializer
from newsfeed import settings
import requests
from .forms import SourceForm, EverythingForm
import json
from newsapi import NewsApiClient
# Create your views here.

class IndexView(ListView):
    template_name = 'news_feed/index.html'

    def get_queryset(self):
        return self.template_name

    # context_object_name = 'all_news'
    
class TopHeadLinesView(DetailView):
    form  = TopHeadLineForm
    url=''
    def get(self, request):
        form = self.form(None)
        self.url = 'https://newsapi.org/v2/top-headlines?'
        return render(request, 'news_feed/topheadlines.html', {'form':form})

    def post(self, request):
        form = self.form(request.POST)
        print (form)
        if form.is_valid():
            # user = form.save(commit=False)
            # print ("hi")
            self.url = 'https://newsapi.org/v2/top-headlines?'
            query = form.cleaned_data['q']
            domains = form.cleaned_data['domains']
            country = form.cleaned_data['country']
            category = form.cleaned_data['category']
            sortBy = request.POST.get('radio', None)
            print (type(query),domains,fromDate,toDate,sortBy)
            if query!='':
                self.url = self.url+'q="'+query+'"&'
#             if domains!='':
#                 self.url = self.url+'domains='+domains+'&'
            if country!=None:
                self.url = self.url+'country='+country+'&'
            if category!=None:
                self.url = self.url+'category='+category+'&'
#             if sortBy!=None:
#                 self.url = self.url+'sortBy='+sortBy+'&'
            self.url = self.url+'apiKey='+settings.API_KEY
            print (self.url)
            r = requests.get(self.url)
            jso = r.json()
            
class EverythingView(DetailView):
    form  = EverythingForm
    url=''
    def get(self, request):
        form = self.form(None)
        self.url = 'https://newsapi.org/v2/everything?'
        return render(request, 'news_feed/everything.html', {'form':form})

    def post(self, request):
        form = self.form(request.POST)
        print (form)
        if form.is_valid():
            # user = form.save(commit=False)
            # print ("hi")
            self.url = 'https://newsapi.org/v2/everything?'
            query = form.cleaned_data['q']
            domains = form.cleaned_data['domains']
            fromDate = form.cleaned_data['fromTime']
            toDate = form.cleaned_data['toTime']
            sortBy = request.POST.get('radio', None)
            print (type(query),domains,fromDate,toDate,sortBy)
            if query!='':
                self.url = self.url+'q="'+query+'"&'
            if domains!='':
                self.url = self.url+'domains='+domains+'&'
            if fromDate!=None:
                self.url = self.url+'from='+str(fromDate)+'&'
            if toDate!=None:
                self.url = self.url+'to='+str(toDate)+'&'
            if sortBy!=None:
                self.url = self.url+'sortBy='+sortBy+'&'
            self.url = self.url+'apiKey='+settings.API_KEY
            print (self.url)
            r = requests.get(self.url)
            jso = r.json()
            print (jso)

class SourceView(DetailView):
    form = SourceForm

    def get(self, request):
        form = self.form(None)
        source = Sources()
        r = requests.get('https://newsapi.org/v2/sources?apiKey='+settings.API_KEY)
        jso = r.json()
        i=0

        while (i<len(jso['sources'])):
            try:
                # print (jso)
                m = source.jsonToSourcesModel(jso,i)
                m.save()
                i+=1
            except:
                i+=1
        q = Sources.objects.all()
        return render(request, 'news_feed/sources.html', {'source': source, 'form': form, 'q':q},)

    def post(self, request):
    
        form = self.form(request.POST)
        if form.is_valid():

            q = Sources.objects.all()
            print (request.POST.getlist('category_tag[]', False))
            if request.POST.getlist('category_tag[]', False):

                category_tag = request.POST.getlist('category_tag[]')
                print (category_tag)
                q = q.filter(category__in=category_tag)
                
            print (request.POST.get('lang_tag[]', False))
            if request.POST.get('lang_tag[]', False):
                lang_tag = request.POST.getlist('lang_tag[]')
                print (lang_tag)

                q = q.filter(language__in=lang_tag)
                

            if request.POST.get('country_tag[]', False):
        
                country_tag = request.POST.getlist('country_tag[]')
                print (country_tag)

                q = q.filter(country__in=country_tag)

            if q==[]:
                return render(request,'news_feed/sources.html', {'q': None})
            else:
                return render(request, 'news_feed/sources.html', {'q': q})


            # print (i)


JR59414 - Fidelity Information Services
