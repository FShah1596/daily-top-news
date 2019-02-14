from django.db import models
import datetime


class TopHeadlines(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    urlToImage = models.CharField(max_length=500, null=True)
    publishedAt = models.DateTimeField('date_published')
    content = models.CharField(max_length=1000)

    class Meta:
            unique_together = ("name", "description", "url", "urlToImage", "publishedAt")

    def __str__(self):
        return self.description + ',' + str(self.publishedAt)

    def jsonToNewsModel(self, jsonData,i):
        # i=0
        # print (1)
        news = News()
        category = Categories.objects.get(pk='id')
        news.model = category
        news.name = jsonData['articles'][i]['source']['name']
        news.description = jsonData['articles'][i]['description']
        news.url = jsonData['articles'][i]['url']
        news.urlToImage = jsonData['articles'][i]['urlToImage']
        news.publishedAt = jsonData['articles'][i]['publishedAt']
        # print (i)
        return news
        i=i+1

class Everything(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=200)
    urlToImage = models.CharField(max_length=500, null=True)
    publishedAt = models.DateTimeField('date_published')
    content = models.CharField(max_length=1000)

    class Meta:
            unique_together = ("name", "description", "url", "urlToImage", "publishedAt")

    def __str__(self):
        return self.description + ',' + str(self.publishedAt)

class Sources(models.Model):
    # id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    country = models.CharField(max_length=10)


    def jsonToSourcesModel(selfself, jsonData, i):
        source = Sources()
        # source.id = jsonData['sources'][i]['id']
        source.name = jsonData['sources'][i]['name']
        source.description = jsonData['sources'][i]['description']
        source.url = jsonData['sources'][i]['url']
        source.category = jsonData['sources'][i]['category']
        source.language = jsonData['sources'][i]['language']
        source.country = jsonData['sources'][i]['country']

        return source

    def __str__(self):
        return self.language + ',' + str(self.name)+','+self.category


    class Meta:
            unique_together = ("name", "description", "url", "category", "language")
