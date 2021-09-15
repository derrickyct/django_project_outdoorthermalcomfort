# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def PlotGraph(request):
    plot = {
        'title': 'Outdoor Thermal Plotting'
    }
    return render(request, 'plotting/index.html', {'plot_title': plot['title']})
