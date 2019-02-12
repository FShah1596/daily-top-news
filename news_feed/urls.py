from django.urls import path
from . import views
app_name = 'news_feed'

urlpatterns = [
	#news_feed/
    path(r'', views.IndexView.as_view(), name = 'index'),

    #news_feed/sources/
    path(r'sources/', views.SourceView.as_view(), name = 'sources'),

    #news_feed/everything
    path(r'everything/', views.EverythingView.as_view(), name = 'everything')
    ]

