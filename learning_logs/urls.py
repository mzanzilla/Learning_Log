"""Defines URL patterns for learning_logs"""
from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^topics/$', views.topics, name = 'topics'),
    # Detail page for a single topic
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #page for adding a new  topic
    url(r'^new_topic/$', views.new_topic, name='new_topic')
]
