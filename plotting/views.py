# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def plotly(request):
    context = {
        'status_plot': 'active',
    }
    return render(request, 'plotting/index.html', context)
