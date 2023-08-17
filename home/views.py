from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
