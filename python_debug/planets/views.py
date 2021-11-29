from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import logging
logger = logging.getLogger(__name__)

def planet_template(request):
    planet_list = ['Mercury', 'Venue', 'Earth', 'Mars']
    # from Python3.7
    # breakpoint() ---> you can then check the variable planet_list from the console/terminal
    context = {
        'planet_list': planet_list
    }

    return render(request, 'planet.html', context)

def planet_name(request):
    return HttpResponse('Loading Earth')