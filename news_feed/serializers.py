from rest_framework import serializers
from news_feed.models import Everything

class NewsFeedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Everything
        fields = '__all__'
