# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from myapp.views import *

# Routing Implement
urlpatterns = [
       path('pricing/', pricing, name='pricing'),
       path('welcome/', welcome, name='welcome'),
       path('dynamic/<int:id>', dynamic, name='dynamic'),
       path('dynamic_delete/<int:id>', dynamic_delete, name='dynamic_delete'),
       path('chatui/', chatui, name='chatui'),
       path('sentimentui/', sentimentui, name='sentimentui'),
       path('faq/', faq, name='faq'),
       path('profile/', profile, name='profile'),
       path('chat_add/', chat_add, name='chat_add'),
       path('sentiment_add/', sentiment_add, name='sentiment_add'),


    
]


