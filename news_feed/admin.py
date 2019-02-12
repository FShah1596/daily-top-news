from django.contrib import admin
from news_feed.models import Everything, Sources
# Register your models here.


admin.site.register(Everything)
# admin.site.register(Categories)
admin.site.register(Sources)
