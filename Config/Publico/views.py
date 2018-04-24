# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Publico.models import *

def index(request):
    return render(request, 'base.html')
