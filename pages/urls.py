from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('structure/', views.StructurePageView.as_view(), name='structure'),
    path('upgrade/', views.UpgradePageView.as_view(), name='upgrade'),
    path('gift-redeem/', views.AmazonGiftView.as_view(), name='amazon'),
    path('astros-banned-from-mlb/', views.NyTimesView.as_view(), name='nytimes'),
]
