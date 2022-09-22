from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView): template_name = 'home.html'
    
class AboutPageView(TemplateView): template_name = 'about.html'

class StructurePageView(TemplateView): template_name = 'htmlstructure.html'

class UpgradePageView(TemplateView): template_name = 'upgrade.html'

class AmazonGiftView(TemplateView): template_name = 'amazon.html' 

class NyTimesView(TemplateView): template_name = 'NyTime.html'
