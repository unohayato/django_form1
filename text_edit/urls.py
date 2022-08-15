from django.urls import path
from text_edit import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
