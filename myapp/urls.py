# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from myapp.views import welcome,chatui,pricing,faq,profile

# Routing Implement
urlpatterns = [
       path('pricing/', pricing, name='pricing'),
       path('welcome/', welcome, name='welcome'),
       path('chatui/', chatui, name='chatui'),
       path('faq/', faq, name='faq'),
       path('profile/', profile, name='profile'),

    
]


