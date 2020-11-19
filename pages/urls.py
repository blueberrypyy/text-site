from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('structure/', views.StructurePageView.as_view(), name='structure'),
    path('upgrade/', views.UpgradePageView.as_view(), name='upgrade'),
]