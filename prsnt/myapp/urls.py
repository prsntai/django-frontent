from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs', views.docs, name='docs'),
    path('ai', views.ai, name='ai'),
    path('transcribe', views.transcribe, name='transcribe'),
]
