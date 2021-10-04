# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def PlotGraph(request):
    context = {
        'title': 'Data Plot',
        'status_plot': 'active',
    }
    return render(request, 'plotting/index.html', context)

from django.http import JsonResponse

import requests

from bs4 import BeautifulSoup


def shiny(request):
    context = {
        'title': 'Data Plot',
        'status_plot': 'active',
    }
    return render(request, 'plotting/shiny.html', context)


def shiny_contents(request):
    response = requests.get('https://testing-shiny.herokuapp.com/')
    soup = BeautifulSoup(response.content, 'html.parser')
    return JsonResponse({'html_contents': str(soup)})
