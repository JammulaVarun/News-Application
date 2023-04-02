from django.shortcuts import render
import os

# Create your views here.

from .utils import *
from dotenv import load_dotenv

from .models import *

load_dotenv()

def home(request):
    url = os.getenv('url')
    get_news_api(url)
    article = articles.objects.all()
    return render(request, 'home.html', locals())