from django.urls import path
from . import views

# patternleri buraya yazdım

urlpatterns = [path('', views.post_list, name = 'post_list')]